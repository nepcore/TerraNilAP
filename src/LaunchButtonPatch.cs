using Global;
using HarmonyLib;
using Utils;

namespace TerraNilAP;

[HarmonyPatch(typeof(View.UiHelpers.ProgressUIs.Tier3ProgressUI), "Create")]
class LaunchButtonPatch
{
    public static void Postfix(View.UiHelpers.ProgressUIs.Tier3ProgressUI __instance)
    {
        TerraNilAP.Logger.LogInfo($"hooking launch button");
        __instance.LaunchButton().onClick.AddListener(() => {
            var mission = MonoSingleton<CampaignStateManager>.Instance.GameState.missionKey;
            TerraNilAP.Logger.LogInfo("Launch button pressed");
            TerraNilAP.MissionCompleted(mission);
        });
    }
}
