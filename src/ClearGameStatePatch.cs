using Global;
using HarmonyLib;

namespace TerraNilAP;

[HarmonyPatch(typeof(CampaignStateManager), "ClearGameState")]
class ClearGameStatePatch
{
    public static bool Prefix()
    {
        return false;
    }
}
