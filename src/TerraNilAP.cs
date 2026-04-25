using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Helpers;
using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using Model;
using System.Collections.Generic;
using System.Reflection;
using System.Linq;
using TerraNilAP.MissionLogic;
using TMPro;
using UnityEngine;

namespace TerraNilAP;

[BepInPlugin(MyPluginInfo.PLUGIN_GUID, MyPluginInfo.PLUGIN_NAME, MyPluginInfo.PLUGIN_VERSION)]
public class TerraNilAP : BaseUnityPlugin
{
    public const string GameName = "TerraNil";

    internal static new ManualLogSource Logger;

    public static Harmony Harmony;
    public static ArchipelagoSession Session;
    public static HashSet<Mission> Completed;
    public static Dictionary<Mission, IMissionLogic> MissionLogic = new Dictionary<Mission, IMissionLogic>();
    public static TMP_FontAsset Font;
    public static APConsole.APConsole Console;
    public static AssetBundle ConsoleAssets;

    private void Awake()
    {
        Logger = base.Logger;
        Harmony = new Harmony("terranilap.gameplay");

        Logger.LogInfo($"Loading resources");
        var fontObj = UnityEngine.Resources.Load<UnityEngine.Font>("default/KorolevRoundedMedium");
        Font = TMP_FontAsset.CreateFontAsset(fontObj);
        ConsoleAssets = AssetBundle.LoadFromStream(TerraNilAP.GetResource("TerraNilAP.assets.console"));
        if (MissionLogic.Count == 0)
        {
            MissionLogic.Add(Mission.TemperateRiver, new RiverValleyLogic());
            MissionLogic.Add(Mission.TropicalIsland, new DesolateIslandLogic());
        }

        Logger.LogInfo($"Injecting essential patches");
        var harmony = new Harmony("terranilap.essential");
        harmony.PatchAll(typeof(ProfileSelectionPatch));

        Logger.LogInfo($"Initialization completed");
    }

    private static void GiveMoney(int amount)
    {
        try
        {
            var cmd = new Model.Commands.Command(new System.Collections.Generic.List<Model.Commands.Delta>());
            cmd.currencyDelta = amount;
            Utils.MonoSingleton<Controller.GameController>.Instance.ExecuteCommand(cmd);
        }
        catch
        {
            Logger.LogInfo("Cannot grant money");
        }
    }

    public static void ReceivedItem(ReceivedItemsHelper items)
    {
        while (items.Any())
        {
            var item = items.DequeueItem();
            Logger.LogInfo($"Received {item.ItemDisplayName} from {item.Player.Alias}'s {item.LocationDisplayName}");
            if (item.ItemId == 2)
            {
                GiveMoney(10);
            }
            else if (item.ItemId == 3)
            {
                GiveMoney(25);
            }
            else if (item.ItemId == 4)
            {
                GiveMoney(50);
            }
            else if (item.ItemId == 5)
            {
                GiveMoney(75);
            }
        }
    }

    public static void MissionCompleted(Mission mission)
    {
        Completed.Add(mission);
        if (Completed.Count == 2) Session.SetGoalAchieved();
        var toSave = Completed.Select(m => (int) m).Select(m => m.ToString()).Join(delimiter: ",");
        var platform = Utils.MonoSingleton<Global.CampaignStateManager>.Instance.Platform;
        System.IO.File.WriteAllText(System.IO.Path.Combine(platform.ProfileDirectory, "missions.ap"), toSave);
    }

    public static System.IO.Stream GetResource(string name)
    {
        return Assembly.GetExecutingAssembly().GetManifestResourceStream(name);
    }

    public static Sprite SpriteFromResource(string name)
    {
        var tex = new Texture2D(2, 2);
        var res = GetResource(name);
        var bytes = new byte[res.Length];
        res.Read(bytes, 0, bytes.Length);
        ImageConversion.LoadImage(tex, bytes);
        return Sprite.Create(tex, new Rect(0, 0, tex.width, tex.height), Vector2.zero);
    }
}
