using Global;
using HarmonyLib;
using Utils;
using View.UiHelpers.Panels;

namespace TerraNilAP;

[HarmonyPatch(typeof(DifficultySelectPanel), "UpdateCampaignStateWithChosenDifficulty")]
class DifficultyPatch
{
    public static void Postfix()
    {
        TerraNilAP.Logger.LogInfo("Patching difficulty settings");
        var diff = MonoSingleton<CampaignStateManager>.Instance.PlayerProfileState.difficultyState;
        diff.enableBuildingUnlocks = true;
    }
}
