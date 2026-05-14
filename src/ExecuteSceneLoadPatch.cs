using Data;
using Global;
using HarmonyLib;
using Model.State;
using System.Reflection;
using Utils;

namespace TerraNilAP;

[HarmonyPatch(typeof(LoadingScreenManager), "ExecuteLoadOperation")]
class ExecuteSceneLoadPatch
{
    public static void Postfix()
    {
        MonoSingleton<CampaignStateManager>.Instance.PlayerProfileState.metaProgressState.unlockedBuildings = new();
        var missionData = (MissionData) typeof(ProgressionState)
            .GetField("_missionData", BindingFlags.Instance | BindingFlags.NonPublic)
            .GetValue(MonoSingleton<CampaignStateManager>.Instance.GameState.progressionState);
        missionData.toForceUnlockWhenMissionStarts = [];
        missionData.toForceUnlockWhenTier2Starts = [];
        missionData.toForceUnlockWhenTier3Starts = [];
    }
}
