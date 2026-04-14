using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Helpers;
using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using Model;
using Newtonsoft.Json.Linq;
using System.Collections.Generic;
using System.Reflection;
using TerraNilAP.MissionLogic;
using TMPro;
using UnityEngine;

namespace TerraNilAP;

[BepInPlugin(MyPluginInfo.PLUGIN_GUID, MyPluginInfo.PLUGIN_NAME, MyPluginInfo.PLUGIN_VERSION)]
public class TerraNilAP : BaseUnityPlugin
{
    public const string GameName = "Terra Nil";

    internal static new ManualLogSource Logger;

    public static Harmony Harmony;
    public static ArchipelagoSession Session;
    public static Dictionary<Mission, IMissionLogic> MissionLogic = new Dictionary<Mission, IMissionLogic>();
    public static TMP_FontAsset Font;

    private void Awake()
    {
        Logger = base.Logger;
        Harmony = new Harmony("terranilap.gameplay");

        Logger.LogInfo($"Loading resources");
        var fontObj = UnityEngine.Resources.Load<UnityEngine.Font>("default/KorolevRoundedMedium");
        Font = TMP_FontAsset.CreateFontAsset(fontObj);
        if (MissionLogic.Count == 0)
        {
            MissionLogic.Add(Mission.TemperateRiver, new RiverValleyLogic());
        }

        Logger.LogInfo($"Injecting essential patches");
        var harmony = new Harmony("terranilap.essential");
        harmony.PatchAll(typeof(ProfileSelectionPatch));

        Logger.LogInfo($"Initialization completed");
    }

    public static void ReceivedItem(ReceivedItemsHelper items)
    {
        while (items.Any())
        {
            var item = items.DequeueItem();
            TerraNilAP.Logger.LogInfo($"Received {item.ItemDisplayName} from {item.Player.Alias}'s {item.LocationDisplayName}");
        }
    }

    public static void MissionCompleted(Mission mission)
    {
        Session.SetGoalAchieved();
    }

    public static Sprite SpriteFromResource(string name)
    {
        var tex = new Texture2D(2, 2);
        var res = Assembly.GetExecutingAssembly().GetManifestResourceStream(name);
        var bytes = new byte[res.Length];
        res.Read(bytes, 0, bytes.Length);
        ImageConversion.LoadImage(tex, bytes);
        return Sprite.Create(tex, new Rect(0, 0, tex.width, tex.height), Vector2.zero);
    }
}
