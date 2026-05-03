using Global;
using HarmonyLib;

namespace TerraNilAP;

[HarmonyPatch(typeof(CampaignStateManager), "AutosaveCurrentGameState")]
class AutosavePatch
{
    public static void Postfix(CampaignStateManager __instance)
    {
        if (__instance.GameState != null)
        {
            var mission = (int) __instance.GameState.missionKey;
            __instance.SaveCurrentGameState($"{mission}_autosave.save");
        }
    }
}
