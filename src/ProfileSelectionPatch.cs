using Archipelago.MultiClient.Net;
using Global;
using HarmonyLib;
using RTLTMPro;
using TMPro;
using UnityEngine;
using UnityEngine.UI;
using Utils;
using View.Handlers;
using View.UiHelpers;

namespace TerraNilAP;

[HarmonyPatch(typeof(ProfileSelectionHandler), "Start")]
class ProfileSelectionPatch
{
    private static GameObject cutsceneSkipper;

    private static void RenderInput(GameObject input, Transform parent, string label, string initial = "")
    {
        var wrapper = new GameObject("InputWrapper");
        wrapper.AddComponent<LayoutElement>();
        var layout = wrapper.AddComponent<HorizontalLayoutGroup>();
        layout.padding = new RectOffset(128, 128, 16, 16);
        layout.childForceExpandWidth = false;
        wrapper.transform.SetParent(parent);
        var hostLabel = TMP_DefaultControls.CreateText(new TMP_DefaultControls.Resources());
        hostLabel.GetComponent<TextMeshProUGUI>().font = TerraNilAP.Font;
        hostLabel.GetComponent<TextMeshProUGUI>().fontSize = 18;
        hostLabel.GetComponent<TextMeshProUGUI>().SetText(label + ":");
        hostLabel.GetComponent<TextMeshProUGUI>().alignment = TextAlignmentOptions.Left;
        hostLabel.AddComponent<LayoutElement>().minWidth = 100;
        hostLabel.transform.SetParent(wrapper.transform);
        input.GetComponent<TMP_InputField>().placeholder.GetComponent<TextMeshProUGUI>().text = label;
        input.GetComponent<TMP_InputField>().placeholder.GetComponent<TextMeshProUGUI>().fontStyle = FontStyles.Normal;
        input.GetComponent<TMP_InputField>().placeholder.GetComponent<TextMeshProUGUI>().color = new Color(1, 1, 1, .25f);
        input.GetComponent<TMP_InputField>().textComponent.font = TerraNilAP.Font;
        input.GetComponent<TMP_InputField>().textComponent.color = new Color(1, 1, 1);
        input.GetComponent<TMP_InputField>().text = initial;
        input.GetComponent<TMP_InputField>().fontAsset = TerraNilAP.Font;
        input.GetComponent<TMP_InputField>().caretColor = new Color(1, 1, 1);
        input.GetComponent<TMP_InputField>().selectionColor = new Color(.35f, .4f, .5f);
        input.GetComponent<Image>().color = new Color(0, 0, 0, 0);
        input.AddComponent<LayoutElement>().flexibleWidth = 10;
        GameObject.Instantiate(parent.parent.Find("Border"), input.transform);
        input.transform.SetParent(wrapper.transform);

        // disable and reenable text field to get the caret working...
        input.GetComponent<TMP_InputField>().enabled = false;
        input.GetComponent<TMP_InputField>().enabled = true;
    }

    public static async void OnSwitchProfile()
    {
        try {
            if (TerraNilAP.Session.Socket != null && TerraNilAP.Session.Socket.Connected) await TerraNilAP.Session.Socket.DisconnectAsync();
        } catch {} // ignore exceptions
        Unpatch();
        GameObject.Find("/Canvas/Buttons/SwitchProfileButton").GetComponent<Button>().onClick.RemoveListener(OnSwitchProfile);
    }

    public static void InjectPatches()
    {
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
        TerraNilAP.Harmony.PatchAll(typeof(PauseMenuWorldMapPatch));
        cutsceneSkipper = new GameObject("CutsceneSkipper");
        cutsceneSkipper.AddComponent<CutscenePatch>();
    }

    public static void Unpatch()
    {
        TerraNilAP.Harmony.UnpatchSelf();
        Object.DestroyImmediate(cutsceneSkipper);
    }

    public static async void OnSelectArchipelago()
    {
        TerraNilAP.Logger.LogInfo("Archipelago profile selected");

        try
        {
            if (TerraNilAP.Session != null && TerraNilAP.Session.Socket.Connected) await TerraNilAP.Session.Socket.DisconnectAsync();
        }
        catch {} // ignore exceptions

        var parent = GameObject.Find("/Canvas/DialogParent");

        var host = TMP_DefaultControls.CreateInputField(new TMP_DefaultControls.Resources());
        var port = TMP_DefaultControls.CreateInputField(new TMP_DefaultControls.Resources());
        var slot = TMP_DefaultControls.CreateInputField(new TMP_DefaultControls.Resources());
        var pass = TMP_DefaultControls.CreateInputField(new TMP_DefaultControls.Resources());

        MonoSingleton<MessageHandler>.Instance.CreateConfirmationDialog(
            "Archipelago Connection",
            "Loading...",
            "",
            async delegate
            {
                TerraNilAP.Logger.LogInfo("Connecting to archipelago");
                TerraNilAP.Logger.LogInfo("Creating session");
                TerraNilAP.Session = ArchipelagoSessionFactory.CreateSession(host.GetComponent<TMPro.TMP_InputField>().text + ":" + port.GetComponent<TMPro.TMP_InputField>().text);
                TerraNilAP.Completed = new System.Collections.Generic.HashSet<Model.Mission>();
                try
                {
                    TerraNilAP.Logger.LogInfo("Initiating connecting");
                    var roomInfo = await TerraNilAP.Session.ConnectAsync();
                    TerraNilAP.Logger.LogInfo("Logging in");
                    var loginResult = await TerraNilAP.Session.LoginAsync(
                        TerraNilAP.GameName,
                        slot.GetComponent<TMPro.TMP_InputField>().text,
                        Archipelago.MultiClient.Net.Enums.ItemsHandlingFlags.AllItems,
                        password: pass.GetComponent<TMPro.TMP_InputField>().text,
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
                            //MonoSingleton<CampaignStateManager>.Instance.DeletePlayerProfileFiles(profileName);
                            if (MonoSingleton<CampaignStateManager>.Instance.LoadPlayerProfile(profileName) == null)
                                MonoSingleton<CampaignStateManager>.Instance.CreateAndAssignNewProfile(profileName);
                            MonoSingleton<ProfileSelectionHandler>.Instance.UpdateAllProfileLanguages();
                            var profileState = MonoSingleton<CampaignStateManager>.Instance.LoadPlayerProfile(profileName);
                            //profileState.difficultyState.hasSelectedDifficulty = true;
                            profileState.hasPlayedTutorial = true;
                            profileState.hasPlayedClimateTutorial = true;
                            profileState.hasPlayedAnimalTutorialIntro = true;
                            profileState.hasPlayedAnimalTutorialGoal = true;
                            profileState.hasPlayedAbilityTutorial = true;
                            MonoSingleton<CampaignStateManager>.Instance.SetProfileState(profileState);
                            TerraNilAP.Logger.LogInfo("Setting up handlers");
                            TerraNilAP.Session.Items.ItemReceived += TerraNilAP.ReceivedItem;
                            MonoSingleton<ProfileSelectionHandler>.Instance.Hide();
                            TerraNilAP.Logger.LogInfo("Applying patches");
                            GameObject.Find("/Canvas/Buttons/SwitchProfileButton").GetComponent<Button>().onClick.AddListener(OnSwitchProfile);
                            TerraNilAP.Session.Socket.ErrorReceived += delegate {
                                TerraNilAP.Logger.LogInfo("Connection lost");
                                Unpatch();
                            };
                            InjectPatches();
                            TerraNilAP.Logger.LogInfo("Connection successful");
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
                catch (System.Exception ex)
                {
                    TerraNilAP.Logger.LogError($"Failed connecting to archipelago: {ex}");
                    MonoSingleton<MessageHandler>.Instance.CreateConfirmationDialog("Error", "Connection failed. Are host and port correct?");
                }
            },
            delegate { TerraNilAP.Logger.LogInfo("Cancelled"); }
        );

        var btnLabel = GameObject.Find("/Canvas/DialogParent/TextDialogFlexible(Clone)/BottomPanel/GlyphButtonText(Clone)/Text");
        btnLabel.GetComponent<RTLTextMeshPro>().SetText("Connect");

        var dialogContent = UnityEngine.GameObject.Find("/Canvas/DialogParent/TextDialogFlexible(Clone)/ContentPanel");

        var horizontal = dialogContent.GetComponent<HorizontalLayoutGroup>();
        if (horizontal != null) GameObject.DestroyImmediate(horizontal);
        var vertical = dialogContent.GetComponent<VerticalLayoutGroup>();
        if (vertical == null) vertical = dialogContent.AddComponent<VerticalLayoutGroup>();
        vertical.padding = new RectOffset(0, 0, 8, 0);

        RenderInput(host, dialogContent.transform, "Host", "archipelago.gg");
        RenderInput(port, dialogContent.transform, "Port", "38281");
        RenderInput(slot, dialogContent.transform, "Slot");
        RenderInput(pass, dialogContent.transform, "Password");

        dialogContent.transform.Find("Content").gameObject.SetActive(false);
    }

    public static void Postfix()
    {
        TerraNilAP.Logger.LogInfo("Injecting archipelago entry into profile selector");

        var slot = GameObject.Instantiate(GameObject.Find("SaveHolder/1"));
        slot.name = "Archipelago";
        slot.transform.Find("NewSlot").gameObject.SetActive(true);
        slot.transform.Find("ExistingSlot").gameObject.SetActive(false);
        slot.transform.Find("NewSlot/Inner/Label").gameObject.SetActive(false);
        var btn = slot.GetComponent<Button>();
        btn.onClick = new Button.ButtonClickedEvent();
        btn.onClick.AddListener(OnSelectArchipelago);

        var preSpacer = new GameObject("Spacer");
        preSpacer.AddComponent<LayoutElement>().flexibleWidth = 25;
        preSpacer.transform.SetParent(slot.transform.Find("NewSlot/Inner"));

        var iconWrapper = new GameObject("IconWrapper");
        var iconLayout = iconWrapper.AddComponent<LayoutElement>();
        iconLayout.preferredHeight = iconLayout.minHeight = iconLayout.preferredWidth = iconLayout.minWidth = 80;
        iconWrapper.AddComponent<HorizontalLayoutGroup>().padding = new RectOffset(12, 12, 12, 12);
        iconWrapper.transform.SetParent(slot.transform.Find("NewSlot/Inner"));

        var icon = new GameObject("Icon");
        icon.AddComponent<Image>().sprite = TerraNilAP.SpriteFromResource("TerraNilAP.assets.archipelago.png");
        icon.transform.SetParent(iconWrapper.transform);

        var label = new GameObject("Label");
        label.AddComponent<RTLTextMeshPro>().text = "Archipelago";
        label.GetComponent<RTLTextMeshPro>().alignment = TMPro.TextAlignmentOptions.Center;
        label.AddComponent<FontLookup>();
        label.transform.SetParent(slot.transform.Find("NewSlot/Inner"));

        var postSpacer = new GameObject("Spacer");
        postSpacer.AddComponent<LayoutElement>().flexibleWidth = 25;
        postSpacer.transform.SetParent(slot.transform.Find("NewSlot/Inner"));

        var saves = GameObject.Find("SaveHolder");
        slot.SetActive(true);
        slot.transform.SetParent(saves.transform);

        TerraNilAP.Logger.LogInfo("Archipelago entry injected");
    }
}
