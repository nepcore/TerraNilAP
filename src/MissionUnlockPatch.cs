using Global;
using HarmonyLib;
using Model;
using Utils;
using WorldMap;

namespace TerraNilAP;

[HarmonyPatch(typeof(WorldMapSceneHandler), "LateStart")]
class MissionUnlockPatch
{
    public static void Postfix(WorldMapSceneHandler __instance)
    {
        foreach (var mission in (Mission[])System.Enum.GetValues(typeof(Mission)))
        {
            var missionid = (long) mission;
            var id = (1L << 31) | (1L << 30) | (missionid << 12);
            var hasItem = false;
            foreach (var item in TerraNilAP.Connection.Items.AllItemsReceived)
            {
                hasItem = id == item.ItemId;
                if (hasItem) break;
            }

            if (hasItem)
            {
                MonoSingleton<CampaignStateManager>.Instance.PlayerProfileState.metaProgressState.UnlockMission(mission);
            }
            else
            {
                MonoSingleton<CampaignStateManager>.Instance.PlayerProfileState.metaProgressState.unlockedMissions.Remove(mission);
            }

            MonoSingleton<WorldMapSelectionHandler>.Instance.SetMissionInteractable(mission, hasItem);
            MonoSingleton<WorldMapSelectionHandler>.Instance.SetMissionLightBeam(mission, hasItem);
            MonoSingleton<WorldMapSelectionHandler>.Instance.SetMissionLocked(mission, !hasItem);
        }

        MonoSingleton<CampaignStateManager>.Instance.SaveCurrentPlayerProfile();
        __instance.DebugUpdateAll();
    }
}
