using Data;
using HarmonyLib;
using Model;
using Model.State;
using System.Collections.Generic;
using System.Reflection;

namespace TerraNilAP;

[HarmonyPatch(typeof(GameState), "ExecuteCommand")]
class GameStateSyncPatch
{
    private static Dictionary<string, long> names = new Dictionary<string, long>();
    private static long
	firstPower = location(1),
	firstPollution = location(2),
	firstGreenery = location(3),
	firstWater = location(4),
	firstFire = location(13),
	t1p25 = location(5),
	t1p50 = location(6),
	t1p75 = location(7),
	t1p100 = location(8),
	t2fynbos1 = location(10),
	t2fynbos100 = location(14),
	t2wetland1 = location(11),
	t2wetland100 = location(15),
	t2forest1 = location(12),
	t2forest100 = location(16),
	t3recycle1 = location(18),
	t3recycle100 = location(19),
	t3photo3 = location(20),
	t3photo10 = location(21);

    private static long location(int id)
    {
        return (1u << 31) | (((uint)Mission.TemperateRiver) << 12) | id;
    }

    public static void Postfix(GameState __instance)
    {
        if (names.Count == 0) {
            names.Add("Wildflowers", location(26));
            names.Add("SpawnOverheadBirds", location(27));
            names.Add("Mushrooms", location(29));
            names.Add("Ferns", location(28));
            names.Add("Lilypads", location(31));
            names.Add("Salmon", location(32));
            names.Add("WeatherRestored", location(30));
        }

        var fynbosTarget = __instance.progressionState.Tier2SingleTarget(Type.Fynbos);
        var wetlandTarget = __instance.progressionState.Tier2SingleTarget(Type.Wetland);
        var forestTarget = __instance.progressionState.Tier2SingleTarget(Type.Forest);

	foreach (var tile in __instance.mapState.map)
	{
	    if (TerraNilAP.Session.Locations.AllMissingLocations.Contains(firstPower))
	    {
                if (tile.HasResource(Resource.Power))
                {
                    TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {firstPower});
                }
            }

	    if (TerraNilAP.Session.Locations.AllMissingLocations.Contains(firstPollution))
	    {
		if (tile.type == Type.Soil)
		{
		    TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {firstPollution});
		}
	    }

	    if (TerraNilAP.Session.Locations.AllMissingLocations.Contains(firstGreenery))
	    {
		if (tile.type == Type.Greenery)
		{
		    TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {firstGreenery});
		}
	    }

	    if (TerraNilAP.Session.Locations.AllMissingLocations.Contains(firstWater))
	    {
		if (tile.type == Type.River)
		{
		    TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {firstWater});
		}
	    }

	    if (TerraNilAP.Session.Locations.AllMissingLocations.Contains(firstFire))
	    {
                if (tile.isOnFire)
                {
                    TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {firstFire});
                }
	    }
        }

        if (__instance.progressionState.Tier1Progress >= 0.25 && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t1p25))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t1p25});
        }

        if (__instance.progressionState.Tier1Progress >= 0.5 && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t1p50))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t1p50});
        }

        if (__instance.progressionState.Tier1Progress >= 0.75 && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t1p75))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t1p75});
        }

        if (__instance.progressionState.Tier1Progress >= 1 && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t1p100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t1p100});
        }

        if (__instance.progressionState.Tier2ProgressDict.GetValueSafe(Type.Fynbos) >= (fynbosTarget * 0.02) && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2fynbos1))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2fynbos1});
        }

        if (__instance.progressionState.Tier2ProgressDict.GetValueSafe(Type.Fynbos) >= fynbosTarget && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2fynbos100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2fynbos100});
        }

        if (__instance.progressionState.Tier2ProgressDict.GetValueSafe(Type.Wetland) >= (wetlandTarget * 0.02) && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2wetland1))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2wetland1});
        }

        if (__instance.progressionState.Tier2ProgressDict.GetValueSafe(Type.Wetland) >= wetlandTarget && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2wetland100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2wetland100});
        }

        if (__instance.progressionState.Tier2ProgressDict.GetValueSafe(Type.Forest) >= (forestTarget * 0.02) && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2forest1))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2forest1});
        }

        if (__instance.progressionState.Tier2ProgressDict.GetValueSafe(Type.Forest) >= forestTarget && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2forest100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2forest100});
        }

        if (__instance.progressionState.ProgressionTier == 3 && __instance.progressionState.Tier3RecyclingProgress >= 0.01 && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t3recycle1))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t3recycle1});
        }

        if (__instance.progressionState.ProgressionTier == 3 && __instance.progressionState.Tier3RecyclingProgress >= 1 && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t3recycle100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t3recycle100});
        }

        if (__instance.progressionState.missionPhotoStarScorecard.GetStarProgressAsAPercentage >= 0.3 && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t3photo3))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t3photo3});
        }

        if (__instance.progressionState.missionPhotoStarScorecard.GetStarProgressAsAPercentage >= 1 && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t3photo10))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t3photo10});
        }

        if (__instance.hasResearchCenterBeenPlaced)
        {
            var missionData = (MissionData)__instance.climateState.GetType().GetField("_mission", BindingFlags.Instance | BindingFlags.NonPublic).GetValue(__instance.climateState);
            foreach (var cond in missionData.climateData.climateConditions)
            {
                if (cond.Evaluate(__instance.climateState))
                {
                    var id = names.GetValueSafe(cond.keyWhenTrue);
                    if (TerraNilAP.Session.Locations.AllMissingLocations.Contains(id))
                    {
                        TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] { id });
                    }
                }
            }
        }
    }
}
