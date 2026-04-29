using Global;
using HarmonyLib;

namespace TerraNilAP;

[HarmonyPatch(typeof(CampaignStateManager), "SaveCurrentGameState")]
class SaveGamePatch
{
    public static bool Prefix(ref string __0, CampaignStateManager __instance)
    {
        if (__instance.GameState != null && !__0.EndsWith("autosave.save"))
        {
            var mission = (int) __instance.GameState.missionKey;
            __0 = $"{mission}_{__0}";
        }
        return true;
    }
}
