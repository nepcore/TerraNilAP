using Controller;
using HarmonyLib;
using Utils;
using View.UiHelpers.Panels;

namespace TerraNilAP;

[HarmonyPatch(typeof(TutorialController), "StartTutorial")]
class TutorialPatch
{
    public static void Postfix(TutorialController __instance)
    {
        TerraNilAP.Logger.LogInfo("Ending tutorial");
        MonoSingleton<TutorialPanel>.Instance.Hide();
        __instance.TriggerEndOfTutorial(true);
    }
}
