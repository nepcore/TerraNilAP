using Data;
using HarmonyLib;
using Model;
using Model.State;
using System.Collections.Generic;
using System.Reflection;

namespace TerraNilAP.MissionLogic;

class VolcanicGlacierLogic : IMissionLogic
{
    private Dictionary<string, long> names = new Dictionary<string, long>();
    private long
        firstPower,
        firstLava,
        firstGreenery,
        firstFire,
        t1p25,
        t1p50,
        t1p75,
        t1p100,
        t2tundra1,
        t2tundra100,
        t2forest1,
        t2forest100,
        t2lichen1,
        t2lichen100,
        t2kelpForest1,
        t2kelpForest100,
        t3recycle1,
        t3recycle100,
        t3photo3,
        t3photo10;

    public VolcanicGlacierLogic()
    {
        firstPower = this.Location(1);
        firstLava = this.Location(2);
        firstGreenery = this.Location(3);
        firstFire = this.Location(10);
        t1p25 = this.Location(4);
        t1p50 = this.Location(5);
        t1p75 = this.Location(6);
        t1p100 = this.Location(7);
        t2tundra1 = this.Location(11);
        t2tundra100 = this.Location(15);
        t2forest1 = this.Location(12);
        t2forest100 = this.Location(16);
        t2lichen1 = this.Location(13);
        t2lichen100 = this.Location(17);
        t2kelpForest1 = this.Location(14);
        t2kelpForest100 = this.Location(18);
        t3recycle1 = this.Location(20);
        t3recycle100 = this.Location(21);
        t3photo3 = this.Location(22);
        t3photo10 = this.Location(23);

        names.Add("SnowMelts", this.Location(30));
        names.Add("Mushrooms", this.Location(31));
        names.Add("IceForms", this.Location(32));
        names.Add("MossyRocks", this.Location(33));
        names.Add("IvyOnBuildings", this.Location(34));
        names.Add("Butterflies", this.Location(35));
        names.Add("SpawnOverheadBirds", this.Location(36));
        names.Add("MossyCliffs", this.Location(37));
        names.Add("FishInOcean", this.Location(38));
        names.Add("WeatherRestored", this.Location(39));
        names.Add("Aurora", this.Location(40));
    }

    public Mission Target()
    {
        return Mission.PolarVolcano;
    }

    public void Update(GameState state)
    {
        var tundraTarget = state.progressionState.Tier2SingleTarget(Type.Tundra);
        var forestTarget = state.progressionState.Tier2SingleTarget(Type.BorealForest);
        var lichenTarget = state.progressionState.Tier2SingleTarget(Type.Lichen);
        var kelpForestTarget = state.progressionState.Tier2SingleTarget(Type.Kelp);

        foreach (var tile in state.mapState.map)
        {
            if (TerraNilAP.Session.Locations.AllMissingLocations.Contains(firstPower))
            {
                if (tile.HasResource(Resource.Power))
                {
                    TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {firstPower});
                }
            }

            if (TerraNilAP.Session.Locations.AllMissingLocations.Contains(firstGreenery))
            {
                if (tile.type == Type.Greenery)
                {
                    TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {firstGreenery});
                }
            }

            if (TerraNilAP.Session.Locations.AllMissingLocations.Contains(firstLava))
            {
                if (tile.type == Type.Lava)
                {
                    TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {firstLava});
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

        if (state.progressionState.Tier1Progress >= 0.25 && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t1p25))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t1p25});
        }

        if (state.progressionState.Tier1Progress >= 0.5 && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t1p50))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t1p50});
        }

        if (state.progressionState.Tier1Progress >= 0.75 && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t1p75))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t1p75});
        }

        if (state.progressionState.Tier1Progress >= 1 && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t1p100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t1p100});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Tundra) >= (tundraTarget * 0.02) && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2tundra1))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2tundra1});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Tundra) >= tundraTarget && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2tundra100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2tundra100});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.BorealForest) >= (forestTarget * 0.02) && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2forest1))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2forest1});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.BorealForest) >= forestTarget && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2forest100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2forest100});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Lichen) >= (lichenTarget * 0.02) && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2lichen1))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2lichen1});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Lichen) >= lichenTarget && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2lichen100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2lichen100});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Kelp) >= (kelpForestTarget * 0.02) && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2kelpForest1))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2kelpForest1});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Kelp) >= kelpForestTarget && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2kelpForest100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2kelpForest100});
        }

        if (state.progressionState.ProgressionTier == 3 && state.progressionState.Tier3RecyclingProgress >= 0.01 && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t3recycle1))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t3recycle1});
        }

        if (state.progressionState.ProgressionTier == 3 && state.progressionState.Tier3RecyclingProgress >= 1 && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t3recycle100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t3recycle100});
        }

        if (state.progressionState.missionPhotoStarScorecard.GetStarProgressAsAPercentage >= 0.29 && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t3photo3))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t3photo3});
        }

        if (state.progressionState.missionPhotoStarScorecard.GetStarProgressAsAPercentage >= .99 && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t3photo10))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t3photo10});
        }

        var missionData = (MissionData)state.climateState.GetType().GetField("_mission", BindingFlags.Instance | BindingFlags.NonPublic).GetValue(state.climateState);
        foreach (var cond in missionData.climateData.climateConditions)
        {
            if (cond.Evaluate(state.climateState))
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
