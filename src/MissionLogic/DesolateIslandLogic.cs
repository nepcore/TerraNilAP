using Data;
using HarmonyLib;
using Model;
using Model.State;
using System.Collections.Generic;
using System.Reflection;

namespace TerraNilAP.MissionLogic;

class DesolateIslandLogic : IMissionLogic
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
        t2beach1,
        t2beach100,
        t2mangrove1,
        t2mangrove100,
        t2rainforest1,
        t2rainforest100,
        t2coralreef1,
        t2coralreef100,
        t3recycle1,
        t3recycle100,
        t3photo3,
        t3photo10;

    public DesolateIslandLogic()
    {
        firstPower = this.Location(1);
        firstPollution = this.Location(2);
        firstGreenery = this.Location(3);
        firstWater = this.Location(4);
        t1p25 = this.Location(5);
        t1p50 = this.Location(6);
        t1p75 = this.Location(7);
        t1p100 = this.Location(8);
        t2beach1 = this.Location(10);
        t2beach100 = this.Location(14);
        t2mangrove1 = this.Location(11);
        t2mangrove100 = this.Location(15);
        t2rainforest1 = this.Location(12);
        t2rainforest100 = this.Location(16);
        t2coralreef1 = this.Location(13);
        t2coralreef100 = this.Location(17);
        t3recycle1 = this.Location(18);
        t3recycle100 = this.Location(19);
        t3photo3 = this.Location(20);
        t3photo10 = this.Location(21);

        names.Add("IvyOnBuildings", this.Location(33));
        names.Add("Jellyfish", this.Location(31));
        names.Add("Crabs", this.Location(28));
        names.Add("PalmsOnBeaches", this.Location(29));
        names.Add("SpawnOverheadBirds", this.Location(27));
        names.Add("Ferns", this.Location(32));
        names.Add("VinesOnMonorail", this.Location(34));
        names.Add("Lilypads", this.Location(35));
        names.Add("Dragonflies", this.Location(30));
        names.Add("MossyCliffs", this.Location(26));
        names.Add("WeatherRestored", this.Location(36));
    }

    public Mission Target()
    {
        return Mission.TropicalIsland;
    }

    public void Update(GameState state)
    {
        var beachTarget = state.progressionState.Tier2SingleTarget(Type.Beach);
        var mangroveTarget = state.progressionState.Tier2SingleTarget(Type.Mangroves);
        var rainforestTarget = state.progressionState.Tier2SingleTarget(Type.TropicalForest);
        var coralreefTarget = state.progressionState.Tier2SingleTarget(Type.Coral);

        foreach (var tile in state.mapState.map)
        {
            if (TerraNilAP.Connection.Locations.AllMissingLocations.Contains(firstPower))
            {
                if (tile.HasResource(Resource.Power))
                {
                    TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {firstPower});
                }
            }

            if (TerraNilAP.Connection.Locations.AllMissingLocations.Contains(firstPollution))
            {
                if (tile.type == Type.Soil)
                {
                    TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {firstPollution});
                }
            }

            if (TerraNilAP.Connection.Locations.AllMissingLocations.Contains(firstGreenery))
            {
                if (tile.type == Type.Greenery)
                {
                    TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {firstGreenery});
                }
            }

            if (TerraNilAP.Connection.Locations.AllMissingLocations.Contains(firstWater))
            {
                if (tile.type == Type.River)
                {
                    TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {firstWater});
                }
            }
        }

        if (state.progressionState.Tier1Progress >= 0.25 && TerraNilAP.Connection.Locations.AllMissingLocations.Contains(t1p25))
        {
            TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {t1p25});
        }

        if (state.progressionState.Tier1Progress >= 0.5 && TerraNilAP.Connection.Locations.AllMissingLocations.Contains(t1p50))
        {
            TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {t1p50});
        }

        if (state.progressionState.Tier1Progress >= 0.75 && TerraNilAP.Connection.Locations.AllMissingLocations.Contains(t1p75))
        {
            TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {t1p75});
        }

        if (state.progressionState.Tier1Progress >= 1 && TerraNilAP.Connection.Locations.AllMissingLocations.Contains(t1p100))
        {
            TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {t1p100});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Beach) >= (beachTarget * 0.02) && TerraNilAP.Connection.Locations.AllMissingLocations.Contains(t2beach1))
        {
            TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {t2beach1});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Beach) >= beachTarget && TerraNilAP.Connection.Locations.AllMissingLocations.Contains(t2beach100))
        {
            TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {t2beach100});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Mangroves) >= (mangroveTarget * 0.02) && TerraNilAP.Connection.Locations.AllMissingLocations.Contains(t2mangrove1))
        {
            TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {t2mangrove1});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Mangroves) >= mangroveTarget && TerraNilAP.Connection.Locations.AllMissingLocations.Contains(t2mangrove100))
        {
            TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {t2mangrove100});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.TropicalForest) >= (rainforestTarget * 0.02) && TerraNilAP.Connection.Locations.AllMissingLocations.Contains(t2rainforest1))
        {
            TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {t2rainforest1});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.TropicalForest) >= rainforestTarget && TerraNilAP.Connection.Locations.AllMissingLocations.Contains(t2rainforest100))
        {
            TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {t2rainforest100});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Coral) >= (coralreefTarget * 0.02) && TerraNilAP.Connection.Locations.AllMissingLocations.Contains(t2coralreef1))
        {
            TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {t2coralreef1});
        }

        if (state.progressionState.Tier2ProgressDict.GetValueSafe(Type.Coral) >= coralreefTarget && TerraNilAP.Connection.Locations.AllMissingLocations.Contains(t2coralreef100))
        {
            TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {t2coralreef100});
        }

        if (state.progressionState.ProgressionTier == 3 && state.progressionState.Tier3RecyclingProgress >= 0.01 && TerraNilAP.Connection.Locations.AllMissingLocations.Contains(t3recycle1))
        {
            TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {t3recycle1});
        }

        if (state.progressionState.ProgressionTier == 3 && state.progressionState.Tier3RecyclingProgress >= 1 && TerraNilAP.Connection.Locations.AllMissingLocations.Contains(t3recycle100))
        {
            TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {t3recycle100});
        }

        if (state.progressionState.missionPhotoStarScorecard.GetStarProgressAsAPercentage >= 0.29 && TerraNilAP.Connection.Locations.AllMissingLocations.Contains(t3photo3))
        {
            TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {t3photo3});
        }

        if (state.progressionState.missionPhotoStarScorecard.GetStarProgressAsAPercentage >= .99 && TerraNilAP.Connection.Locations.AllMissingLocations.Contains(t3photo10))
        {
            TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] {t3photo10});
        }

        var missionData = (MissionData)state.climateState.GetType().GetField("_mission", BindingFlags.Instance | BindingFlags.NonPublic).GetValue(state.climateState);
        foreach (var cond in missionData.climateData.climateConditions)
        {
            if (state.climateState.ClimateBlackboard.GetValue(cond.keyWhenTrue))
            {
                var id = names.GetValueSafe(cond.keyWhenTrue);
                if (TerraNilAP.Connection.Locations.AllMissingLocations.Contains(id))
                {
                    TerraNilAP.Connection.Locations.CompleteLocationChecks(new long[] { id });
                }
            }
        }
    }
}
