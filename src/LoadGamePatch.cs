using Global;
using HarmonyLib;

namespace TerraNilAP;

[HarmonyPatch(typeof(CampaignStateManager), "LoadGameState")]
class LoadGamePatch
{
    public static bool Prefix(ref string __0, CampaignStateManager __instance)
    {
        if (__instance.GameState != null && __0 == $"start_of_{__instance.GameState.progressionState.ProgressionTier}.save")
        {
            var mission = (int) __instance.GameState.missionKey;
            __0 = $"{mission}_start_of_{__instance.GameState.progressionState.ProgressionTier}.save";
        }
        return true;
    }
}
