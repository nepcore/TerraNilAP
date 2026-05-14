using Data;
using HarmonyLib;
using Model;
using Model.State;
using System.Collections.Generic;
using System.Reflection;

namespace TerraNilAP.MissionLogic;

class ScorchedCalderaLogic : IMissionLogic
{
    private Dictionary<string, long> names = new Dictionary<string, long>();
    private long
        firstPower,
        firstPollution,
        firstGreenery,
        firstWater,
        t1p25,
        t1p50,
        t1p75,
        t1p100,
        t2lakeVegetation1,
        t2lakeVegetation100,
        t2bamboo1,
        t2bamboo100,
        t2tropicalForest1,
        t2tropicalForest100,
        t3recycle1,
        t3recycle100,
        t3photo3,
        t3photo10;

    public ScorchedCalderaLogic()
    {
        firstPower = this.Location(1);
        firstPollution = this.Location(2);
        firstGreenery = this.Location(3);
        firstWater = this.Location(10);
        t1p25 = this.Location(4);
        t1p50 = this.Location(5);
        t1p75 = this.Location(6);
        t1p100 = this.Location(7);
        t2lakeVegetation1 = this.Location(11);
        t2lakeVegetation100 = this.Location(14);
        t2bamboo1 = this.Location(12);
        t2bamboo100 = this.Location(15);
        t2tropicalForest1 = this.Location(13);
        t2tropicalForest100 = this.Location(16);
        t3recycle1 = this.Location(20);
        t3recycle100 = this.Location(21);
        t3photo3 = this.Location(22);
        t3photo10 = this.Location(23);

        names.Add("IvyOnBuildings", this.Location(30));
        names.Add("SpawnOverheadBirds", this.Location(31));
        names.Add("Ferns", this.Location(32));
        names.Add("VinesOnMonorail", this.Location(33));
        names.Add("Lilypads", this.Location(34));
        names.Add("Dragonflies", this.Location(35));
        names.Add("CloudForest", this.Location(36));
        names.Add("MossyCliffs", this.Location(37));
        names.Add("WeatherRestored", this.Location(38));
    }

    public Mission Target()
    {
        return Mission.TropicalCaldera;
    }

    public void Update(GameState state)
    {
        var lakeVegetationTarget = state.progressionState.Tier2SingleTarget(Type.LakeFloorVegetation);
        var bambooTarget = state.progressionState.Tier2SingleTarget(Type.Bamboo);
        var tropicalForestTarget = state.progressionState.Tier2SingleTarget(Type.TropicalForest);

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

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.LakeFloorVegetation) >= (lakeVegetationTarget * 0.02) && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2lakeVegetation1))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2lakeVegetation1});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.LakeFloorVegetation) >= lakeVegetationTarget && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2lakeVegetation100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2lakeVegetation100});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Bamboo) >= (bambooTarget * 0.02) && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2bamboo1))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2bamboo1});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Bamboo) >= bambooTarget && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2bamboo100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2bamboo100});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.TropicalForest) >= (tropicalForestTarget * 0.02) && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2tropicalForest1))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2tropicalForest1});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.TropicalForest) >= tropicalForestTarget && TerraNilAP.Session.Locations.AllMissingLocations.Contains(t2tropicalForest100))
        {
            TerraNilAP.Session.Locations.CompleteLocationChecks(new long[] {t2tropicalForest100});
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
