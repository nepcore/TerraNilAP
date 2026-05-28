using HarmonyLib;
using WorldMap;

namespace TerraNilAP;

[HarmonyPatch(typeof(WorldMapSceneHandler.MissionSceneData), "IsUnlocked")]
[HarmonyPatch(typeof(WorldMapSceneHandler.MissionSceneData), "IsInteractable")]
class MissionSceneDataPatch
{
    public static void Postfix(WorldMapSceneHandler.MissionSceneData __instance, ref bool __result)
    {
        var missionid = (uint) __instance.mission;
        var id = (1u << 31) | (1u << 30) | (missionid << 12);
        var hasItem = false;
        foreach (var item in TerraNilAP.Connection.Items.AllItemsReceived)
        {
            hasItem = id == item.ItemId;
            if (hasItem) break;
        }

        if (hasItem)
        {
            __result = true;
        }
        else
        {
            __result = false;
        }
    }
}
