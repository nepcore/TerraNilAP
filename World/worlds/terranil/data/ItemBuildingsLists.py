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
    ConeFilter =        (120, "Cone Filter", 1)
    Irrigator =         (102, "Irrigator", 1)
    Excavator =         (103, "Excavator", 1)
    WaterPump =         (104, "Water Pump", 1)
    Calcifier =         (105, "Calcifier", 1)
    
    ResearchCenter =    (200, "Research Center", 2)
    Hydroponium =       (201, "Hydroponium", 2)
    Beehive =           (202, "Beehive", 2)
    Arboretum =         (203, "Arboretum", 2)
    SolarAmplifier =    (205, "Solar Amplifier", 2)
    Chaparrallum =      (230, "Chaparrallum", 2)
    
    Airship =           (300, "Airship", 3)
    LoadingDock =       (301, "Loading Dock", 3)
    PoundLock =         (302, "Pound Lock", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    Combustor =         (402, "Combustor", 4)


class PollutedBayBuildings(BuildingEnum):
    "The building IDs for all buildings in Polluted Bay"
    TidalTurbine =      (112, "Tidal Turbine", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    Pylon =             (228, "Pylon", 1)
    Excavator =         (103, "Excavator", 1)
    WaterPump =         (104, "Water Pump", 1)
    Calcifier =         (105, "Calcifier", 1)
    
    ResearchCenter =    (200, "Research Center", 2)
    Hydroponium =       (201, "Hydroponium", 2)
    Beehive =           (202, "Beehive", 2)
    Arboretum =         (203, "Arboretum", 2)
    SolarAmplifier =    (205, "Solar Amplifier", 2)
    Conservatory =      (227, "Conservatory", 2)
    
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
    SeismicDetonator =  (218, "Seismic Detonator", 1)
    
    ResearchCenter =    (200, "Research Center", 2)
    Hydroponium =       (201, "Hydroponium", 2)
    Beehive =           (202, "Beehive", 2)
    Arboretum =         (203, "Arboretum", 2)
    SolarAmplifier =    (205, "Solar Amplifier", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    FlyingRecyclingDrone = (307, "Flying Recycling Drone", 3)
    StandaloneBeacon =  (327, "Standalone Beacon", 3)
    RockHopper =        (324, "Rock Hopper", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    Dehumidifier =      (405, "Dehumidifier", 4)



## Region Tropical

class DesolateIslandBuildings(BuildingEnum):
    "The building IDs for all buildings in Desolate Island"
    Turbine =           (100, "Wind Turbine", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    WaterPump =         (104, "Water Pump", 1)
    Mineralizer =       (108, "Mineralizer", 1)
    SandBank =          (107, "Sand Bank", 1)
    
    Hydroponium =       (201, "Hydroponium", 2)
    Littarium =         (209, "Littarium", 2)
    Salinator =         (208, "Salinator", 2)
    ShadeclothPillar =  (210, "Shadecloth Pillar", 2)
    MonorailNode =      (212, "Monorail Node", 2)
    CoralLab =          (211, "Coral Lab", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclerStation =   (305, "Recycler Station", 3)
    RecyclingBeacon =   (306, "Recycling Beacon", 3)
    RockHopper =        (324, "Rock Hopper", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    Combustor = (402, "Combustor", 4)


class ScorchedCalderaBuildings(BuildingEnum):
    "The building IDs for all buildings in Scorched Caldera"
    GeothermalPlant =   (110, "Geothermal Plant", 1)
    SeismicDetonator =  (218, "Seismic Detonator", 1)
    ConeFilter =        (120, "Cone Filter", 1)
    Irrigator =         (102, "Irrigator", 1)
    Excavator =         (103, "Excavator", 1)
    
    ShadeclothPillar =  (210, "Shadecloth Pillar", 2)
    MiniBambooNurseryInternalName = (223, "Mini Bamboo Nursery", 2)
    PercolotriumInternalName = (999, "Percolotrium", 2)
    RockHopperInternalName = (324, "Rock Hopper", 2)
    MonorailNodeInternalName = (212, "Monorail Node", 2)
    TranspiratorInternalName = (999, "Transpirator", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclerStation =   (305, "Recycler Station", 3)
    RecyclingBeacon =   (306, "Recycling Beacon", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    Combustor =         (402, "Combustor", 4)


class ArchipelagoBuildings(BuildingEnum):
    "The building IDs for all buildings in Archipelago (the map)"
    Turbine =           (100, "Wind Turbine", 1)
    UnderseaDredge =    (999, "Undersea Dredger", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    Excavator =         (103, "Excavator", 1)
    WaterPump =         (104, "Water Pump", 1)
    Mineralizer =       (108, "Mineralizer", 1)
    
    Hydroponium =       (201, "Hydroponium", 2)
    Littarium =         (209, "Littarium", 2)
    Salinator =         (208, "Salinator", 2)
    ShadeclothPillar =  (210, "Shadecloth Pillar", 2)
    MonorailNode =      (212, "Monorail Node", 2)
    CoralLab =          (211, "Coral Lab", 2)
    ResearchCenter =    (200, "Research Center", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    LoadingDock =       (301, "Loading Dock", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    Combustor =         (402, "Combustor", 4)



## Region Polar

class VolcanicGlacierBuildings(BuildingEnum):
    "The building IDs for all buildings in Volcanic Glacier"
    SeismicDetonator =  (218, "Seismic Detonator", 1)
    GeothermalPlant =   (110, "Geothermal Plant", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    SolarAmplifier =    (205, "Solar Amplifier", 1)
    Excavator =         (103, "Excavator", 1)
    
    MonorailNode =      (212, "Monorail Node", 2)
    Arboretum =         (203, "Arboretum", 2)
    Biodome =           (999, "Biodome", 2)
    RadialExcavator =   (999, "Radial Excavator", 2)
    IgneousHeatsink =   (999, "Igneous Heatsink", 2)
    AlgaeGreenhouse =   (999, "Algae Greenhouse", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclerStation = (305, "Recycler Station", 3)
    RecyclingBeacon = (306, "Recycling Beacon", 3)
    RockHopper = (324, "Rock Hopper", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    Dehumidifier =      (405, "Dehumidifier", 4)
    Combustor =         (402, "Combustor", 4)
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
    Chaparrallum = (230, "Chaparrallum", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    FlyingRecyclingDrone = (307, "Flying Recycling Drone", 3)
    StandaloneBeaconInternalName = (327, "Standalone Beacon", 3)
    RockHopper = (324, "Rock Hopper", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    Dehumidifier = (405, "Dehumidifier", 4)
    Combustor = (402, "Combustor", 4)
    FlashFreezer =      (999, "Flash Freezer", 4)


class PollutedFjordBuildings(BuildingEnum):
    "The building IDs for all buildings in Polluted Fjord"
    Turbine =           (100, "Wind Turbine", 1)
    TidalTurbine = (112, "Tidal Turbine", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    SolarAmplifier =    (205, "Solar Amplifier", 1)
    WaterPump =         (104, "Water Pump", 1)
    Calcifier =         (105, "Calcifier", 1)
    
    MonorailNodeInternalName = (212, "Monorail Node", 2)
    Arboretum =         (203, "Arboretum", 2)
    Biodome =           (999, "Biodome", 2)
    AlgaeGreenhouse =   (999, "Algae Greenhouse", 2)
    RockHopper =        (324, "Rock Hopper", 2)
    Excavator =         (103, "Excavator", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclerStation = (305, "Recycler Station", 3)
    RecyclingBeacon = (306, "Recycling Beacon", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    Dehumidifier = (405, "Dehumidifier", 4)
    Combustor = (402, "Combustor", 4)
    FlashFreezer =      (999, "Flash Freezer", 4)



# Region Continental

class FloodedCityBuildings(BuildingEnum):
    "The building IDs for all buildings in Flooded City"
    UnderseaDredge =    (999, "Undersea Dredger", 1)
    TidalTurbine = (112, "Tidal Turbine", 1)
    LoadingDock =       (301, "Loading Dock", 1)
    MonorailNodeInternalName = (212, "Monorail Node", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    SeismicDetonator = (218, "Seismic Detonator", 1)
    
    MineralizerInternalName =         (999, "Mineralizer", 2)
    ThalassicPurifier = (999, "Thalassic Purifier", 2)
    BambooNursery =(999, "Bamboo Nursery", 2)
    Conservatory = (227, "Conservatory", 2)
    RadiationCleanser = (999, "Radiation Cleanser", 2)
    PylonInternalName = (999, "Pylon", 2)
    Heliocage = (999, "Heliocage", 2)
    
    FlyingRecyclingDrone = (307, "Flying Recycling Drone", 3)
    SatelliteUplink = (999, "Satellite Uplink", 3)
    RocketSilo = (999, "Rocket Silo", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    StandaloneBeaconInternalName = (327, "Standalone Beacon", 3)
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
    Dehumidifier = (405, "Dehumidifier", 4)
    Combustor = (402, "Combustor", 4)
    FlashFreezer =      (999, "Flash Freezer", 4)


class IrradiatedSprawlBuildings(BuildingEnum):
    "The building IDs for all buildings in Irradiated Sprawl"
    Turbine =           (100, "Turbine", 1)
    ToxinScrubber =     (101, "Toxin Scrubber", 1)
    Irrigator =         (102, "Irrigator", 1)
    Pylon = (228, "Pylon", 1)
    RadiationCleanser = (999, "Radiation Cleanser", 1)
    MonorailNodeInternalName = (212, "Monorail Node", 1)
    
    MineralizerInternalName =         (999, "Mineralizer", 2)
    ThalassicPurifier = (999, "Thalassic Purifier", 2)
    BambooNursery =(999, "Bamboo Nursery", 2)
    Conservatory = (227, "Conservatory", 2)
    Heliocage = (999, "Heliocage", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclerStation = (305, "Recycler Station", 3)
    # MonorailNodeInternalName = (212, "Monorail Node", 3) ##Duplicate
    RecyclingBeacon = (306, "Recycling Beacon", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    Dehumidifier = (405, "Dehumidifier", 4)
    Combustor = (402, "Combustor", 4)
    FlashFreezer =      (999, "Flash Freezer", 4)


class ContinentalOutskirtsBuildings(BuildingEnum):
    "The building IDs for all buildings in Continental Outskirts"
    Pylon = (228, "Pylon", 1)
    ConeFilter = (120, "Cone Filter", 1)
    PipeHub =           (999, "Pipe Hub", 1)
    WaterPump =         (104, "Water Pump", 1)
    Calcifier =         (105, "Calcifier", 1)
    Excavator =         (103, "Excavator", 1)
    
    Beehive =           (202, "Beehive", 2)
    Conservatory = (227, "Conservatory", 2)
    BambooNursery =(999, "Bamboo Nursery", 2)
    RockHopperInternalName = (324, "Rock Hopper", 2)
    
    Airship =           (300, "Airship", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RecyclingDrone =    (304, "Recycling Drone", 3)
    FlyingRecyclingDrone = (307, "Flying Recycling Drone", 3)
    StandaloneBeaconInternalName = (327, "Standalone Beacon", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    Dehumidifier = (405, "Dehumidifier", 4)
    Combustor = (402, "Combustor", 4)
    FlashFreezer =      (999, "Flash Freezer", 4)



# Region Arid

class ParchedDunesBuildings(BuildingEnum):
    "The building IDs for all buildings in Parched Dunes"
    Aqueduct = (999, "Aqueduct", 1)
    SolarArray = (999, "Solar Array", 1)
    SandHelix = (999, "Sand Helix", 1)
    ConeFilter = (120, "Cone Filter", 1)
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
    Dehumidifier = (405, "Dehumidifier", 4)
    Combustor = (402, "Combustor", 4)
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
    Chaparrallum = (230, "Chaparrallum", 2)
    Xerophytium =       (999, "Xerophytium", 2)
    Heliocage = (999, "Heliocage", 2)
    Arboretum =         (203, "Arboretum", 2)
    RockHopperInternalName = (324, "Rock Hopper", 2)
    DehumidifierInternalName = (999, "Dehumidifier", 2)
    
    Airship =           (300, "Airship", 3)
    BridgeBuilder = (999, "Bridge Builder", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    SonicPulse =        (325, "Sonic Pulse", 3)
    # WildlifeBridge =    (326, "Wildlife Bridge", 1) ##Duplicate
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    # DehumidifierInternalName = (999, "Dehumidifier", 4) ##Duplicate
    Combustor = (402, "Combustor", 4)
    FlashFreezer =      (999, "Flash Freezer", 4)


class FrackedFloodplainBuildings(BuildingEnum):
    "The building IDs for all buildings in Fracked Floodplain"
    SolarArray = (999, "Solar Array", 1)
    ConeFilter = (120, "Cone Filter", 1)
    Irrigator =         (102, "Irrigator", 1)
    HyacinthGerminator = (999, "Hyacinth Germinator", 1)
    SeismicDetonator = (218, "Seismic Detonator", 1)
    SandHelix = (999, "Sand Helix", 1)
    
    BiofuelExtractor = (999, "Biofuel Extractor", 2)
    # Calcifier =         (105, "Calcifier", 2)   ##Duplicate
    Hydroponium =       (201, "Hydroponium", 2)
    Chaparrallum = (230, "Chaparrallum", 2)
    BirdSanctuary = (999, "Bird Sanctuary", 2)
    SavannahSeeder =    (999, "Savannah Seeder", 2)
    # ##Dehumidifier
    SonicPulse =        (325, "Sonic Pulse", 2)
    
    RecyclingRover = (999, "Recycling Rover", 3)
    MonorailNodeInternalName = (212, "Monorail Node", 3)
    RecyclingSilo =     (303, "Recycling Silo", 3)
    RocketThrusters = (999, "Rocket Thrusters", 3)
    AricCommsArray = (999, "Arid Comms Array", 3)
    Cockpit = (999, "Cockpit", 3)
    # ##Sonic Pulse
    WildlifeBridge =    (326, "Wildlife Bridge", 3)
    AnimalObservatory = (500, "Animal Observatory", 3)
    
    CloudSeeder =       (404, "Cloud Seeder", 4)
    Dehumidifier = (405, "Dehumidifier", 4)
    Combustor = (402, "Combustor", 4)
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

def test_building_enum(enum_to_test: BuildingEnum, test_id: bool = True, test_tier: bool = True) -> bool:
    has_erred = False
    print(f"\nMap: {enum_to_test.__name__}")
    for i in enum_to_test: # type: ignore
        display_name = i.get_displayName()
        if test_id:
            try:
                building_id = i.get_internalID()
            except NotImplementedError:
                print(f"Building {display_name:<30} has unknown ID (999).")
                has_erred = True
            
        if test_tier:
            try: 
                tier_number = i.get_tier()
            except IndexError:
                print(f"Building {display_name} has no assigned tier.")
                has_erred = True
                
    return has_erred
        

def main():
    for i in all_building_enums_list:
        test_building_enum(i, True, True)

if __name__ == "__main__":
    main()    
