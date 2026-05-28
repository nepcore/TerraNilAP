using Global;
using HarmonyLib;
using System.Reflection;
using Utils;
using View.Photo;

namespace TerraNilAP;

[HarmonyPatch(typeof(PhotoTaker), "DisplayPhotoScore")]
class PhotoTakerPatch
{
    public static void Postfix(PhotoTaker __instance)
    {
        TerraNilAP.Logger.LogInfo("Checking photo score");
        var medal = (PhotoScoreCalculator.Medal) __instance
            .GetType()
            .GetField("_lastPhotoMedal", BindingFlags.Instance | BindingFlags.NonPublic)
            .GetValue(__instance);
        var mission = (uint) MonoSingleton<CampaignStateManager>.Instance.GameState.missionKey;
        uint bronze = (1u << 31) | (mission << 12) | 100u;
        uint silver = (1u << 31) | (mission << 12) | 101u;
        uint gold = (1u << 31) | (mission << 12) | 102u;
        if (medal == PhotoScoreCalculator.Medal.Bronze)
        {
            if (TerraNilAP.Connection.Locations.AllMissingLocations.Contains(bronze))
            {
                TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {bronze});
            }
        }
        else if (medal == PhotoScoreCalculator.Medal.Silver)
        {
            if (TerraNilAP.Connection.Locations.AllMissingLocations.Contains(silver))
            {
                TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {bronze, silver});
            }
        }
        else if (medal == PhotoScoreCalculator.Medal.Gold)
        {
            if (TerraNilAP.Connection.Locations.AllMissingLocations.Contains(gold))
            {
                TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {bronze, silver, gold});
            }
        }
    }
}
