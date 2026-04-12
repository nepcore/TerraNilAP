using Global;
using HarmonyLib;
using UnityEngine.SceneManagement;
using Utils;
using View.Handlers;

namespace TerraNilAP;

[HarmonyPatch(typeof(CampaignStateManager), "StartMission")]
class MissionStartPatch
{
    public static void Postfix(CampaignStateManager __instance)
    {
        TerraNilAP.Logger.LogInfo("Mission started, hooking launch button");
        SceneManager.activeSceneChanged += delegate (Scene current, Scene next)
        {
            if (next.name == "Main")
            {
                MonoSingleton<UIHandler>.Instance.Tier3ProgressUI.LaunchButton().onClick.AddListener(delegate {
                    TerraNilAP.Logger.LogInfo("Launch button pressed");
                    TerraNilAP.Session.SetGoalAchieved();
                });
            }
        };
    }
}
