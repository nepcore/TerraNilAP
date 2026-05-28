using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Helpers;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Models;
using Global;
using UnityEngine;
using UnityEngine.UI;
using Utils;
using View.Handlers;
using HarmonyLib;
using System;
using System.Threading;
using System.Threading.Tasks;
using System.Collections.Generic;
using System.Collections.ObjectModel;

namespace TerraNilAP;

public class DummyLocations : ILocationCheckHelper
{
    public ReadOnlyCollection<long> AllLocations => new(new List<long>());
    public ReadOnlyCollection<long> AllLocationsChecked => new(new List<long>());
    public ReadOnlyCollection<long> AllMissingLocations => new(new List<long>());
    public event LocationCheckHelper.CheckedLocationsUpdatedHandler CheckedLocationsUpdated;
    public void CompleteLocationChecks(params long[] ids) {}
    public async Task CompleteLocationChecksAsync(params long[] ids) {
        return;
    }
    public async Task<Dictionary<long, ScoutedItemInfo>> ScoutLocationsAsync(HintCreationPolicy hcp, params long[] ids) {
        return new Dictionary<long, ScoutedItemInfo>();
    }
    public async Task<Dictionary<long, ScoutedItemInfo>> ScoutLocationsAsync(bool createHint, params long[] ids) {
        return new Dictionary<long, ScoutedItemInfo>();
    }
    public async Task<Dictionary<long, ScoutedItemInfo>> ScoutLocationsAsync(params long[] ids) {
        return new Dictionary<long, ScoutedItemInfo>();
    }
    public long GetLocationIdFromName(string game, string name) {
        return -1;
    }
    public string GetLocationNameFromId(long id, string game) {
        return null;
    }
}

public class DummyItems : IReceivedItemsHelper
{
    public int Index => 0;
    public ReadOnlyCollection<ItemInfo> AllItemsReceived => new(new List<ItemInfo>());
    public event ReceivedItemsHelper.ItemReceivedHandler ItemReceived;
    public string GetItemName(long id, string game) {
        return null;
    }
    public bool Any()
    {
        return false;
    }
    public ItemInfo PeekItem()
    {
        return null;
    }
    public ItemInfo DequeueItem()
    {
        return null;
    }
}

public class APConnection
{
    private string host;
    private string port;
    private string slot;
    private string pass;

    private ArchipelagoSession session;
    private GameObject cutsceneSkipper;
    private bool isInjected = false;
    private bool shouldDisconnect = false;

    private int backoff = 5;
    private CancellationTokenSource reconnectTask;

    public bool Connected => session != null && session.Socket != null && session.Socket.Connected;

    public ILocationCheckHelper Locations => Connected ? session.Locations : new DummyLocations();
    public IReceivedItemsHelper Items => Connected ? session.Items : new DummyItems();

    public APConnection(string host, string port, string slot, string pass)
    {
        this.host = host;
        this.port = port;
        this.slot = slot;
        this.pass = pass;
        Application.quitting += delegate {
            TerraNilAP.Logger.LogInfo("Application quitting");
            if (cutsceneSkipper != null) UnityEngine.Object.DestroyImmediate(cutsceneSkipper);
            if (TerraNilAP.Console != null) TerraNilAP.Console.Destroy();
            Disconnect().Wait();
        };
    }

    public Task Connect()
    {
        return Connect(false);
    }

    private async Task Connect(bool isReconnect)
    {
        TerraNilAP.Logger.LogInfo("Connecting to archipelago");
        TerraNilAP.Logger.LogInfo("Creating session");
        session = ArchipelagoSessionFactory.CreateSession(host + ":" + port);
        TerraNilAP.Completed = new System.Collections.Generic.HashSet<Model.Mission>();
        if (TerraNilAP.Console == null)
        {
            TerraNilAP.Console = new APConsole.APConsole(
                TerraNilAP.ConsoleAssets,
                (_, to) =>
                {
                    return to.name == "WorldMap" || to.name == "Main";
                }
            );
            TerraNilAP.Console.SetFont(TerraNilAP.Font);
            TerraNilAP.Console.AddText("<color=green>You can toggle this console by pressing F1</color>");
        }
        session.MessageLog.OnMessageReceived += TerraNilAP.Console.AddAPMessage;
        try
        {
            TerraNilAP.Logger.LogInfo("Initiating connection");
            var roomInfo = await session.ConnectAsync();
            TerraNilAP.Logger.LogInfo("Logging in");
            var loginResult = await session.LoginAsync(
                TerraNilAP.GameName,
                slot,
                Archipelago.MultiClient.Net.Enums.ItemsHandlingFlags.AllItems,
                password: pass,
                requestSlotData: true
            );

            switch (loginResult)
            {
                case LoginFailure fail:
                    TerraNilAP.Logger.LogError(fail.Errors.Join(delimiter: "\n"));
                    MonoSingleton<MessageHandler>.Instance.CreateConfirmationDialog("Login failed", fail.Errors.Join(delimiter: "\n"));
                    return;
                case LoginSuccessful login:
                    TerraNilAP.Logger.LogInfo("Setting up archipelago profile");
                    var profileName = $"Archipelago {roomInfo.SeedName} {login.Team} {login.Slot}";
                    if (MonoSingleton<CampaignStateManager>.Instance.LoadPlayerProfile(profileName) == null)
                    {
                        MonoSingleton<CampaignStateManager>.Instance.CreateAndAssignNewProfile(profileName);
                    }
                    MonoSingleton<ProfileSelectionHandler>.Instance.UpdateAllProfileLanguages();
                    var profileState = MonoSingleton<CampaignStateManager>.Instance.LoadPlayerProfile(profileName);
                    profileState.difficultyState.hasSelectedDifficulty = true;
                    profileState.hasPlayedTutorial = true;
                    profileState.hasPlayedClimateTutorial = true;
                    profileState.hasPlayedAnimalTutorialIntro = true;
                    profileState.hasPlayedAnimalTutorialGoal = true;
                    profileState.hasPlayedAbilityTutorial = true;
                    MonoSingleton<CampaignStateManager>.Instance.SetProfileState(profileState);
                    TerraNilAP.Logger.LogInfo("Setting up handlers");
                    session.Items.ItemReceived += TerraNilAP.ReceivedItem;
                    MonoSingleton<ProfileSelectionHandler>.Instance.Hide();
                    TerraNilAP.Logger.LogInfo("Applying patches");
                    GameObject.Find("/Canvas/Buttons/SwitchProfileButton").GetComponent<Button>().onClick.AddListener(ProfileSelectionPatch.OnSwitchProfile);
                    session.Socket.ErrorReceived += async delegate {
                        await Reconnect();
                    };
                    InjectPatches();
                    TerraNilAP.Logger.LogInfo("Connection successful");

                    long clearsNeeded = 7;
                    switch (login.SlotData.GetValueSafe("levels_cleared_to_goal"))
                    {
                        case long n:
                            clearsNeeded = n;
                            break;
                        default:
                            MonoSingleton<MessageHandler>.Instance.CreateConfirmationDialog(
                                "Warning",
                                $"Failed to find the number of levels cleared to goal in slot data, assuming {clearsNeeded} instead"
                            );
                            break;
                    }
                    TerraNilAP.MissionsCompletedToGoal = clearsNeeded;

                    var diff = 2L;
                    switch (login.SlotData.GetValueSafe("game_difficulty"))
                    {
                        case long n:
                            diff = n;
                            break;
                        default:
                            MonoSingleton<MessageHandler>.Instance.CreateConfirmationDialog(
                                "Warning",
                                $"Failed to find the selected difficulty in slot data, assuming Ecologist"
                            );
                            break;
                    }
                    TerraNilAP.Logger.LogInfo($"difficulty is {diff}");
                    DifficultySelectionPatch.Difficulty = (int) diff;

                    var platform = MonoSingleton<CampaignStateManager>.Instance.Platform;
                    TerraNilAP.Completed = new();
                    if (System.IO.File.Exists(System.IO.Path.Combine(platform.ProfileDirectory, "missions.ap")))
                    {
                        var loaded = System.IO.File.ReadAllText(System.IO.Path.Combine(platform.ProfileDirectory, "missions.ap"));
                        foreach (var m in loaded.Split(','))
                        {
                            try {
                                TerraNilAP.Completed.Add((Model.Mission) int.Parse(m));
                            }
                            catch (System.Exception e)
                            {
                                TerraNilAP.Logger.LogError($"Failed parsing {m} as mission: {e.Message}\n{e.StackTrace}");
                            }
                        }
                    }
                    TerraNilAP.Logger.LogInfo($"{TerraNilAP.Completed.Count} missions already completed");
                    return;
            }
        }
        catch (System.Threading.Tasks.TaskCanceledException ex)
        {
            if (isReconnect)
            {
                await Reconnect();
            }
            else
            {
                TerraNilAP.Logger.LogError($"Failed connecting to archipelago: {ex.InnerException}");
                MonoSingleton<MessageHandler>.Instance.CreateConfirmationDialog("Error", "Connection failed. Are host and port correct?");
            }
        }
        catch (System.Exception ex)
        {
            if (isReconnect)
            {
                await Reconnect();
            }
            else
            {
                TerraNilAP.Logger.LogError($"Failed connecting to archipelago: {ex}");
                MonoSingleton<MessageHandler>.Instance.CreateConfirmationDialog("Error", "Connection failed. Are host and port correct?");
            }
        }
    }

    private async Task Reconnect()
    {
        if (shouldDisconnect) return;
        TerraNilAP.Logger.LogInfo("Connection lost");
        if (reconnectTask != null && !reconnectTask.IsCancellationRequested) reconnectTask.Cancel();
        var msg = $"Connection to Archipelago server failed, reconnecting in {backoff} seconds...";
        TerraNilAP.Console.AddText($"<color=\"orange\">{msg}</color>");
        reconnectTask = new();
        Task.Delay(backoff * 1000, reconnectTask.Token).Wait();
        if (reconnectTask.IsCancellationRequested) return;
        backoff = Math.Min(backoff + 5, 60);
        Connect(true).Wait();
        await Task.Run(() => {
            // reset backoff if the connection hasn't dropped for a minute
            var ownToken = reconnectTask;
            Task.Delay(60000, ownToken.Token).Wait();
            if (!ownToken.IsCancellationRequested)
            {
                backoff = 5;
            }
        }, reconnectTask.Token);
    }

    public void InjectPatches()
    {
        if (isInjected) return;
        TerraNilAP.Harmony.PatchAll(typeof(TutorialPatch));
        TerraNilAP.Harmony.PatchAll(typeof(GetBuldingDataPatch));
        TerraNilAP.Harmony.PatchAll(typeof(CreateBuildingPatch));
        TerraNilAP.Harmony.PatchAll(typeof(GameStateSyncPatch));
        TerraNilAP.Harmony.PatchAll(typeof(LaunchButtonPatch));
        TerraNilAP.Harmony.PatchAll(typeof(DifficultyPatch));
        TerraNilAP.Harmony.PatchAll(typeof(PhotoTakerPatch));
        TerraNilAP.Harmony.PatchAll(typeof(NewGamePatch));
        TerraNilAP.Harmony.PatchAll(typeof(MissionUnlockPatch));
        TerraNilAP.Harmony.PatchAll(typeof(MissionSceneDataPatch));
        TerraNilAP.Harmony.PatchAll(typeof(StartMissionPatch));
        TerraNilAP.Harmony.PatchAll(typeof(LoadScenePatch));
        TerraNilAP.Harmony.PatchAll(typeof(ProgressionInterfaceHandlerPatch));
        TerraNilAP.Harmony.PatchAll(typeof(PauseMenuPatch));
        TerraNilAP.Harmony.PatchAll(typeof(SaveGamePatch));
        TerraNilAP.Harmony.PatchAll(typeof(AutosavePatch));
        TerraNilAP.Harmony.PatchAll(typeof(LoadGamePatch));
        TerraNilAP.Harmony.PatchAll(typeof(WorldMapLoadMissionPatch));
        TerraNilAP.Harmony.PatchAll(typeof(ClearGameStatePatch));
        TerraNilAP.Harmony.PatchAll(typeof(ExecuteSceneLoadPatch));
        TerraNilAP.Harmony.PatchAll(typeof(AirshipIntroPatch));
        TerraNilAP.Harmony.PatchAll(typeof(DifficultySelectionPatch));
        cutsceneSkipper = new GameObject("CutsceneSkipper");
        cutsceneSkipper.AddComponent<CutscenePatch>();
        isInjected = true;
    }

    public void Unpatch()
    {
        if (!isInjected) return;
        TerraNilAP.Harmony.UnpatchSelf();
        UnityEngine.Object.DestroyImmediate(cutsceneSkipper);
        if (TerraNilAP.Console != null)
        {
            session.MessageLog.OnMessageReceived -= TerraNilAP.Console.AddAPMessage;
            TerraNilAP.Console.Destroy();
            TerraNilAP.Console = null;
        }
        isInjected = false;
    }

    public void SetGoalAchieved()
    {
        session.SetGoalAchieved();
    }

    public async Task Disconnect()
    {
        shouldDisconnect = true;
        if (reconnectTask != null && !reconnectTask.IsCancellationRequested) reconnectTask.Cancel();
        Unpatch();
        if (session == null || session.Socket == null || !session.Socket.Connected) return;
        await session.Socket.DisconnectAsync();
    }
}
