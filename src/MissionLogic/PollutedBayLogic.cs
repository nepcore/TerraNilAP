using Data;
using HarmonyLib;
using Model;
using Model.State;
using System.Collections.Generic;
using System.Reflection;

namespace TerraNilAP.MissionLogic;

class PollutedBayLogic : IMissionLogic
{
    private Dictionary<string, long> names = new Dictionary<string, long>();
    private long
        firstPower,
        firstPollution,
        firstGreenery,
        firstWater,
        firstFire,
        t1p25,
        t1p50,
        t1p75,
        t1p100,
        t2fynbos1,
        t2fynbos100,
        t2wetland1,
        t2wetland100,
        t2forest1,
        t2forest100,
        t2deciduousForest1,
        t2deciduousForest100,
        t3recycle1,
        t3recycle100,
        t3photo3,
        t3photo10;

    public PollutedBayLogic()
    {
        firstPower = this.Location(1);
        firstPollution = this.Location(2);
        firstGreenery = this.Location(3);
        firstWater = this.Location(4);
        firstFire = this.Location(13);
        t1p25 = this.Location(5);
        t1p50 = this.Location(6);
        t1p75 = this.Location(7);
        t1p100 = this.Location(8);
        t2fynbos1 = this.Location(10);
        t2fynbos100 = this.Location(14);
        t2wetland1 = this.Location(11);
        t2wetland100 = this.Location(15);
        t2forest1 = this.Location(12);
        t2forest100 = this.Location(16);
        t2deciduousForest1 = this.Location(17);
        t2deciduousForest100 = this.Location(18);
        t3recycle1 = this.Location(20);
        t3recycle100 = this.Location(21);
        t3photo3 = this.Location(22);
        t3photo10 = this.Location(23);

        names.Add("Wildflowers", this.Location(30));
        names.Add("SpawnOverheadBirds", this.Location(31));
        names.Add("Mushrooms", this.Location(32));
        names.Add("Ferns", this.Location(33));
        names.Add("CliffFoliage", this.Location(34));
        names.Add("Lilypads", this.Location(35));
        names.Add("Salmon", this.Location(36));
        names.Add("FernsOnConcrete", this.Location(37));
        names.Add("WeatherRestored", this.Location(38));
    }

    public Mission Target()
    {
        return Mission.TemperateBay;
    }

    public void Update(GameState state)
    {
        var fynbosTarget = state.progressionState.Tier2SingleTarget(Type.Fynbos);
        var wetlandTarget = state.progressionState.Tier2SingleTarget(Type.Wetland);
        var forestTarget = state.progressionState.Tier2SingleTarget(Type.Forest);
        var deciduousForestTarget = state.progressionState.Tier2SingleTarget(Type.DeciduousForest);

        foreach (var tile in state.mapState.map)
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

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Fynbos) >= (fynbosTarget * 0.02) && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2fynbos1))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2fynbos1});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Fynbos) >= fynbosTarget && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2fynbos100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2fynbos100});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Wetland) >= (wetlandTarget * 0.02) && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2wetland1))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2wetland1});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Wetland) >= wetlandTarget && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2wetland100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2wetland100});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Forest) >= (forestTarget * 0.02) && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2forest1))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2forest1});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Forest) >= forestTarget && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2forest100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2forest100});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.DeciduousForest) >= (deciduousForestTarget * 0.02) && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2deciduousForest1))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2deciduousForest1});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.DeciduousForest) >= deciduousForestTarget && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2deciduousForest100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2deciduousForest100});
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
