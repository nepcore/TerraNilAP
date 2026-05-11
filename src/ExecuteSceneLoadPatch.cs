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
    public static void Postfix(LoadingScreenManager __instance)
    {
        var operation = (LoadingScreenManager.LoadOperationData) __instance.GetType().GetField("_loadOperationData", BindingFlags.Instance | BindingFlags.NonPublic).GetValue(__instance);
        if (operation.LoadOperation == LoadingScreenManager.LoadOperation.LoadInProgressCampaign)
        {
            MonoSingleton<CampaignStateManager>.Instance.PlayerProfileState.metaProgressState.unlockedBuildings = new();
            var missionData = (MissionData)typeof(ProgressionState).GetField("_missionData", BindingFlags.Instance | BindingFlags.NonPublic).GetValue(MonoSingleton<CampaignStateManager>.Instance.GameState.progressionState);
            missionData.toForceUnlockWhenMissionStarts = [];
            missionData.toForceUnlockWhenTier2Starts = [];
            missionData.toForceUnlockWhenTier3Starts = [];
        }
    }
}
