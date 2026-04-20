from enum import Enum

class BuildingEnum(Enum):
    def get_internalID(self, ignore_missing_ids = False) -> int:
        internal_id = self.value[0]
        if internal_id == 999 and not ignore_missing_ids:
            raise NotImplementedError(f"The building {str(self)} is not implemented yet.")
        return internal_id
    
    def get_displayName(self) -> str:
        return self.value[1]
    
    def get_tier(self) -> int:
        return self.value[2]
    
    def __int__(self) -> int: 
        return self.get_internalID()

    def __str__(self) -> str:
        return self.get_displayName()


## Region Temperate

class RiverValleyBuildings(BuildingEnum):
    "The building IDs for all buildings in River Valley"
    Turbine =           (100, "Turbine", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    Excavator =         (103, "Excavator", 1)
    WaterPump =         (104, "Water Pump", 1)
    Calcifier =         (105, "Calcifier", 1)
    
    ResearchCenter =    (200, "Research Center", 2)
    Hydroponium =       (201, "Hydroponium", 2)
    Beehive =           (202, "Beehive", 2)
    Arboretum =         (203, "Arboretum", 2)
    SolarAmplifier =    (205, "Solar Amplifier", 2)
    
    Airship =           (300, "Airship", 3)
    LoadingDock =       (301, "Loading Dock", 3)
    PoundLock =         (302, "Pound Lock", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 2)


class HillAndDaleBuildings(BuildingEnum):
    "The building IDs for all buildings in Hill and Dale"
    Turbine =           (100, "Wind Turbine", 1)
    ConeFilterInternalName = (999, "Cone Filter", 1)
    Irrigator =         (102, "Irrigator", 1)
    Excavator =         (103, "Excavator", 1)
    WaterPump =         (104, "Water Pump", 1)
    Calcifier =         (105, "Calcifier", 1)
    
    ResearchCenter =    (200, "Research Center", 2)
    Hydroponium =       (201, "Hydroponium", 2)
    Beehive =           (202, "Beehive", 2)
    Arboretum =         (203, "Arboretum", 2)
    SolarAmplifier =    (205, "Solar Amplifier", 2)
    ChaparrallumInternalName = (999, "Chaparrallum", 2)
    
    Airship =           (300, "Airship", 3)
    LoadingDock =       (301, "Loading Dock", 3)
    PoundLock =         (302, "Pound Lock", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    CombustorInternalName = (999, "Combustor", 4)


class PollutedBayBuildings(BuildingEnum):
    "The building IDs for all buildings in Polluted Bay"
    TidalTurbineInternalName = (999, "Tidal Turbine", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    PylonInternalName = (999, "Pylon", 1)
    Excavator =         (103, "Excavator", 1)
    WaterPump =         (104, "Water Pump", 1)
    Calcifier =         (105, "Calcifier", 1)
    
    ResearchCenter =    (200, "Research Center", 2)
    Hydroponium =       (201, "Hydroponium", 2)
    Beehive =           (202, "Beehive", 2)
    Arboretum =         (203, "Arboretum", 2)
    SolarAmplifier =    (205, "Solar Amplifier", 2)
    ConservatoryInternalName = (999, "Conservatory", 2)
    
    Airship =           (300, "Airship", 3)
    LoadingDock =       (301, "Loading Dock", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)


class AbandonedQuarryBuildings(BuildingEnum):
    "The building IDs for all buildings in Abandoned Quarry"
    Turbine =           (100, "Wind Turbine", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    Excavator =         (103, "Excavator", 1)
    WaterPump =         (104, "Water Pump", 1)
    SeismicDetonatorInternalName = (999, "Seismic Detonator", 1)
    
    ResearchCenter =    (200, "Research Center", 2)
    Hydroponium =       (201, "Hydroponium", 2)
    Beehive =           (202, "Beehive", 2)
    Arboretum =         (203, "Arboretum", 2)
    SolarAmplifier =    (205, "Solar Amplifier", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    FlyingRecyclingDroneInternalName = (999, "Flying Recycling Drone", 3)
    StandaloneBeaconInternalName = (999, "Standalone Beacon", 3)
    RockHopperInternalName = (999, "Rock Hopper", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    DehumidifierInternalName = (999, "Dehumidifier", 4)



## Region Tropical

class DesolateIslandBuildings(BuildingEnum):
    "The building IDs for all buildings in Desolate Island"
    Turbine =           (100, "Wind Turbine", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    WaterPump =         (104, "Water Pump", 1)
    MineralizerInternalName =         (999, "Mineralizer", 1)
    SandBankInternalName = (999, "Sand Bank", 1)
    
    Hydroponium =       (201, "Hydroponium", 2)
    LittariumInternalName = (999, "Littarium", 2)
    SalinatorInternalName = (999, "Salinator", 2)
    ShadeclothPillarInternalName = (999, "Shadecloth Pillar", 2)
    MonorailNodeInternalName = (999, "Monorail Node", 2)
    CoralLabInternalName = (999, "Coral Lab", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclerStationInternalName = (999, "Recycler Station", 3)
    RecyclingBeaconInternalName = (999, "Recycling Beacon", 3)
    RockHopperInternalName = (999, "Rock Hopper", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    CombustorInternalName = (999, "Combustor", 4)


class ScorchedCalderaBuildings(BuildingEnum):
    "The building IDs for all buildings in Scorched Caldera"
    GeothermalPlantInternalName = (999, "Geothermal Plant", 1)
    SeismicDetonatorInternalName = (999, "Seismic Detonator", 1)
    ConeFilterInternalName = (999, "Cone Filter", 1)
    Irrigator =         (102, "Irrigator", 1)
    Excavator =         (103, "Excavator", 1)
    
    ShadeclothPillarInternalName = (999, "Shadecloth Pillar", 2)
    MiniBambooNurseryInternalName = (999, "Mini Bamboo Nursery", 2)
    PercolotriumInternalName = (999, "Percolotrium", 2)
    RockHopperInternalName = (999, "Rock Hopper", 2)
    MonorailNodeInternalName = (999, "Monorail Node", 2)
    TranspiratorInternalName = (999, "Transpirator", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclerStationInternalName = (999, "Recycler Station", 3)
    RecyclingBeaconInternalName = (999, "Recycling Beacon", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CombustorInternalName = (999, "Combustor", 4)


class ArchipelagoBuildings(BuildingEnum):
    "The building IDs for all buildings in Archipelago (the map)"
    Turbine =           (100, "Wind Turbine", 1)
    UnderseaDredge =    (999, "Undersea Dredger", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    Excavator =         (103, "Excavator", 1)
    WaterPump =         (104, "Water Pump", 1)
    MineralizerInternalName =         (999, "Mineralizer", 1)
    
    Hydroponium =       (201, "Hydroponium", 2)
    LittariumInternalName = (999, "Littarium", 2)
    SalinatorInternalName = (999, "Salinator", 2)
    ShadeclothPillarInternalName = (999, "Shadecloth Pillar", 2)
    MonorailNodeInternalName = (999, "Monorail Node", 2)
    CoralLabInternalName = (999, "Coral Lab", 2)
    ResearchCenter =    (200, "Research Center", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    LoadingDock =       (301, "Loading Dock", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    CombustorInternalName = (999, "Combustor", 4)



## Region Polar

class VolcanicGlacierBuildings(BuildingEnum):
    "The building IDs for all buildings in Volcanic Glacier"
    SeismicDetonatorInternalName = (999, "Seismic Detonator", 1)
    GeothermalPlantInternalName = (999, "Geothermal Plant", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    SolarAmplifier =    (205, "Solar Amplifier", 1)
    Excavator =         (103, "Excavator", 1)
    
    MonorailNodeInternalName = (999, "Monorail Node", 2)
    Arboretum =         (203, "Arboretum", 2)
    Biodome =           (999, "Biodome", 2)
    RadialExcavator =   (999, "Radial Excavator", 2)
    IgneousHeatsink =   (999, "Igneous Heatsink", 2)
    AlgaeGreenhouse =   (999, "Algae Greenhouse", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclerStationInternalName = (999, "Recycler Station", 3)
    RecyclingBeaconInternalName = (999, "Recycling Beacon", 3)
    RockHopperInternalName = (999, "Rock Hopper", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    DehumidifierInternalName = (999, "Dehumidifier", 4)
    CombustorInternalName = (999, "Combustor", 4)
    FlashFreezer =      (999, "Flash Freezer", 4)


class SubpolarRiverBuildings(BuildingEnum):
    "The building IDs for all buildings in Subpolar River"
    Turbine =           (100, "Turbine", 1)
    WaterPump =         (104, "Water Pump", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    PipeHub =           (999, "Pipe Hub", 1)
    CarbonCompactor =   (999, "Carbon Compactor", 1)
    
    SolarAmplifier =    (205, "Solar Amplifier", 2)
    Arboretum =         (203, "Arboretum", 2)
    Biodome =           (999, "Biodome", 2)
    AlgaeGreenhouse =   (999, "Algae Greenhouse", 2)
    ChaparrallumInternalName = (999, "Chaparrallum", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    FlyingRecyclingDroneInternalName = (999, "Flying Recycling Drone", 3)
    StandaloneBeaconInternalName = (999, "Standalone Beacon", 3)
    RockHopperInternalName = (999, "Rock Hopper", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    DehumidifierInternalName = (999, "Dehumidifier", 4)
    CombustorInternalName = (999, "Combustor", 4)
    FlashFreezer =      (999, "Flash Freezer", 4)


class PollutedFjordBuildings(BuildingEnum):
    "The building IDs for all buildings in Polluted Fjord"
    Turbine =           (100, "Wind Turbine", 1)
    TidalTurbineInternalName = (999, "Tidal Turbine", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    SolarAmplifier =    (205, "Solar Amplifier", 1)
    WaterPump =         (104, "Water Pump", 1)
    Calcifier =         (105, "Calcifier", 1)
    
    MonorailNodeInternalName = (999, "Monorail Node", 2)
    Arboretum =         (203, "Arboretum", 2)
    Biodome =           (999, "Biodome", 2)
    AlgaeGreenhouse =   (999, "Algae Greenhouse", 2)
    RockHopperInternalName = (999, "Rock Hopper", 2)
    Excavator =         (103, "Excavator", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclerStationInternalName = (999, "Recycler Station", 3)
    RecyclingBeaconInternalName = (999, "Recycling Beacon", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    DehumidifierInternalName = (999, "Dehumidifier", 4)
    CombustorInternalName = (999, "Combustor", 4)
    FlashFreezer =      (999, "Flash Freezer", 4)



# Region Continental

class FloodedCityBuildings(BuildingEnum):
    "The building IDs for all buildings in Flooded City"
    UnderseaDredge =    (999, "Undersea Dredger", 1)
    TidalTurbineInternalName = (999, "Tidal Turbine", 1)
    LoadingDock =       (301, "Loading Dock", 1)
    MonorailNodeInternalName = (999, "Monorail Node", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    SeismicDetonatorInternalName = (999, "Seismic Detonator", 1)
    
    MineralizerInternalName =         (999, "Mineralizer", 2)
    ThalassicPurifier = (999, "Thalassic Purifier", 2)
    BambooNursery =(999, "Bamboo Nursery", 2)
    ConservatoryInternalName = (999, "Conservatory", 2)
    RadiationCleanser = (999, "Radiation Cleanser", 2)
    PylonInternalName = (999, "Pylon", 2)
    Heliocage = (999, "Heliocage", 2)
    
    FlyingRecyclingDroneInternalName = (999, "Flying Recycling Drone", 3)
    SatelliteUplink = (999, "Satellite Uplink", 3)
    RocketSilo = (999, "Rocket Silo", 3)
    RecyclingSilo =     (303, "Recycling Silo")
    StandaloneBeaconInternalName = (999, "Standalone Beacon", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    RocketThrusters = (999, "Rocket Thrusters", 3)
    CommsArrayA = (999, "Comms Array A", 3)
    CargoHold = (999, "Cargo Hold", 3)
    CommsArrayB = (999, "Comms Array B", 3)
    CryoPods = (999, "Cryo Pods", 3)
    CommsArrayC = (999, "Comms Array C", 3)
    LifeSupport = (999, "Life Support", 3)
    CommsArrayD = (999, "Comms Array D", 3)
    SeedVaultCockpit = (999, "Seed Vault Cockpit", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    DehumidifierInternalName = (999, "Dehumidifier", 4)
    CombustorInternalName = (999, "Combustor", 4)
    FlashFreezer =      (999, "Flash Freezer", 4)


class IrradiatedSprawlBuildings(BuildingEnum):
    "The building IDs for all buildings in Irradiated Sprawl"
    Turbine =           (100, "Turbine", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    PylonInternalName = (999, "Pylon", 1)
    RadiationCleanser = (999, "Radiation Cleanser", 1)
    MonorailNodeInternalName = (999, "Monorail Node", 1)
    
    MineralizerInternalName =         (999, "Mineralizer", 2)
    ThalassicPurifier = (999, "Thalassic Purifier", 2)
    BambooNursery =(999, "Bamboo Nursery", 2)
    ConservatoryInternalName = (999, "Conservatory", 2)
    Heliocage = (999, "Heliocage", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclerStationInternalName = (999, "Recycler Station", 3)
    # MonorailNodeInternalName = (999, "Monorail Node", 2) ##Duplicate
    RecyclingBeaconInternalName = (999, "Recycling Beacon", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    DehumidifierInternalName = (999, "Dehumidifier", 4)
    CombustorInternalName = (999, "Combustor", 4)
    FlashFreezer =      (999, "Flash Freezer", 4)


class ContinentalOutskirtsBuildings(BuildingEnum):
    "The building IDs for all buildings in Continental Outskirts"
    PylonInternalName = (999, "Pylon", 1)
    ConeFilterInternalName = (999, "Cone Filter", 1)
    PipeHub =           (999, "Pipe Hub", 1)
    WaterPump =         (104, "Water Pump", 1)
    Calcifier =         (105, "Calcifier")
    Excavator =         (103, "Excavator", 1)
    
    Beehive =           (202, "Beehive")
    ConservatoryInternalName = (999, "Conservatory", 2)
    BambooNursery =(999, "Bamboo Nursery", 2)
    RockHopperInternalName = (999, "Rock Hopper", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    FlyingRecyclingDroneInternalName = (999, "Flying Recycling Drone", 3)
    StandaloneBeaconInternalName = (999, "Standalone Beacon", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    DehumidifierInternalName = (999, "Dehumidifier", 4)
    CombustorInternalName = (999, "Combustor", 4)
    FlashFreezer =      (999, "Flash Freezer", 4)



# Region Arid

class ParchedDunesBuildings(BuildingEnum):
    "The building IDs for all buildings in Parched Dunes"
    Aqueduct = (999, "Aqueduct", 1)
    SolarArray = (999, "Solar Array", 1)
    SandHelix = (999, "Sand Helix", 1)
    ConeFilterInternalName = (999, "Cone Filter", 1)
    Irrigator =         (102, "Irrigator", 1)
        
    SolarAmplifier =    (205, "Solar Amplifier", 2)
    RecyclingSilo =     (303, "Recycling Silo", 2)
    Excavator =         (103, "Excavator", 2)
    Hydroponium =       (201, "Hydroponium", 2)
    Sedimenter =        (999, "Sedimenter", 2)
    SavannahSeeder =    (999, "Savannah Seeder", 2)
    Xerophytium =       (999, "Xerophytium", 2)
    WildlifeBridge =    (326, "Wildlife Bridge", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    # RecyclingSilo =     (303, "Recycling Silo", 2) ##Duplicate
    LoadingDock =       (301, "Loading Dock", 3)
    PoundLock =         (302, "Pound Lock", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    # WildlifeBridge =    (326, "Wildlife Bridge", 2) ##Duplicate
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    DehumidifierInternalName = (999, "Dehumidifier", 4)
    CombustorInternalName = (999, "Combustor", 4)
    FlashFreezer =      (999, "Flash Freezer", 4)
    Calcifier =         (105, "Calcifier", 4)


class CanyonPeaksBuildings(BuildingEnum):
    "The building IDs for all buildings in Canyon Peaks"
    SolarArray = (999, "Solar Array", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    WildlifeBridge =    (326, "Wildlife Bridge", 1)
    ResearchCenter =    (200, "Research Center", 1)
    
    Beehive =           (202, "Beehive", 2)
    ChaparrallumInternalName = (999, "Chaparrallum", 2)
    Xerophytium =       (999, "Xerophytium", 2)
    Heliocage = (999, "Heliocage", 2)
    Arboretum =         (203, "Arboretum", 2)
    RockHopperInternalName = (999, "Rock Hopper", 2)
    DehumidifierInternalName = (999, "Dehumidifier", 2)
    
    Airship =           (300, "Airship", 3)
    BridgeBuilder = (999, "Bridge Builder", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    # WildlifeBridge =    (326, "Wildlife Bridge", 1) ##Duplicate
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    # DehumidifierInternalName = (999, "Dehumidifier", 4) ##Duplicate
    CombustorInternalName = (999, "Combustor", 4)
    FlashFreezer =      (999, "Flash Freezer", 4)


class FrackedFloodplainBuildings(BuildingEnum):
    "The building IDs for all buildings in Fracked Floodplain"
    SolarArray = (999, "Solar Array", 1)
    ConeFilterInternalName = (999, "Cone Filter", 1)
    Irrigator =         (102, "Irrigator", 1)
    HyacinthGerminator = (999, "Hyacinth Germinator", 1)
    SeismicDetonatorInternalName = (999, "Seismic Detonator", 1)
    SandHelix = (999, "Sand Helix", 1)
    
    BiofuelExtractor = (999, "Biofuel Extractor", 2)
    # Calcifier =         (105, "Calcifier", 2)   ##Duplicate
    Hydroponium =       (201, "Hydroponium", 2)
    ChaparrallumInternalName = (999, "Chaparrallum", 2)
    BirdSanctuary = (999, "Bird Sanctuary", 2)
    SavannahSeeder =    (999, "Savannah Seeder", 2)
    # ##Dehumidifier
    SonicPulse =        (325, "Sonic Pulse", 2)
    
    RecyclingRover = (999, "Recycling Rover", 3)
    MonorailNodeInternalName = (999, "Monorail Node", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RocketThrusters = (999, "Rocket Thrusters", 3)
    AricCommsArray = (999, "Arid Comms Array", 3)
    Cockpit = (999, "Cockpit", 3)
    # ##Sonic Pulse
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory")
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    DehumidifierInternalName = (999, "Dehumidifier", 4)
    CombustorInternalName = (999, "Combustor", 4)
    FlashFreezer =      (999, "Flash Freezer", 4)
    Calcifier =         (105, "Calcifier", 4)
    

all_building_enums_list = [
    RiverValleyBuildings,
    HillAndDaleBuildings,
    PollutedBayBuildings,
    AbandonedQuarryBuildings,
    
    DesolateIslandBuildings,
    ScorchedCalderaBuildings,
    ArchipelagoBuildings,
    
    VolcanicGlacierBuildings,
    SubpolarRiverBuildings,
    PollutedFjordBuildings,
    
    FloodedCityBuildings,
    IrradiatedSprawlBuildings,
    ContinentalOutskirtsBuildings,
    
    ParchedDunesBuildings,
    CanyonPeaksBuildings,
    FrackedFloodplainBuildings
]

def test_building_enum(enum_to_test):
    print()
    for i in enum_to_test:
        display_name = i.get_displayname()
        try:
            building_id = i.get_internal_id()
        except NotImplementedError:
            print(f"Building {display_name:<30} has unknown ID (999).")
        
        try: 
            tier_number = i.get_tier()
        except KeyError:
            print(f"Building {display_name} has no assigned tier.")
        

def main():
    test_building_enum(RiverValleyBuildings)
    test_building_enum(HillAndDaleBuildings)
    test_building_enum(PollutedBayBuildings)
    test_building_enum(AbandonedQuarryBuildings)
    test_building_enum(DesolateIslandBuildings)
    test_building_enum(ScorchedCalderaBuildings)

if __name__ == "__main__":
    main()    
