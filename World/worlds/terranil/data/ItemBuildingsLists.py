from enum import Enum

class BuildingEnum(Enum):
    def __int__(self):
        return self.value[0]

    def __str__(self):
        return self.value[1]


## Region Temperate

class RiverValleyBuildings(BuildingEnum):
    "The building IDs for all buildings in River Valley"
    Turbine =           (100, "Turbine")
    ToxinScrubber =     (101, "Toxin Scrubber")
    Irrigator =         (102, "Irrigator")
    Excavator =         (103, "Excavator")
    WaterPump =         (104, "Water Pump")
    Calcifier =         (105, "Calcifier")
    ResearchCenter =    (200, "Research Center")
    Hydroponium =       (201, "Hydroponium")
    Beehive =           (202, "Beehive")
    Arboretum =         (203, "Arboretum")
    SolarAmplifier =    (205, "Solar Amplifier")
    Airship =           (300, "Airship")
    LoadingDock =       (301, "Loading Dock")
    PoundLock =         (302, "Pound Lock")
    RecyclingSilo =     (303, "Recycling Silo")
    RecyclingDrone =    (304, "Recycling Drone")
    SonicPulse =        (325, "Sonic Pulse")
    WildlifeBridge =    (326, "Wildlife Bridge")
    CloudSeeder =       (404, "Cloud Seeder")
    AnimalObservatory = (500, "Animal Observatory")


class HillAndDaleBuildings(BuildingEnum):
    "The building IDs for all buildings in Hill and Dale"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


class PolutedBayBuildings(BuildingEnum):
    "The building IDs for all buildings in Polluted Bay"
    # Turbine =           (100, "Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


class AbandonedQuarryBuildings(BuildingEnum):
    "The building IDs for all buildings in Abandoned Quarry"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")



## Region Tropical

class DesolateIslandBuildings(BuildingEnum):
    "The building IDs for all buildings in Desolate Island"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


class ScorchedCalderaBuildings(BuildingEnum):
    "The building IDs for all buildings in Scorched Caldera"
    # Turbine =           (100, "Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


class ArchipelagoBuildings(BuildingEnum):
    "The building IDs for all buildings in Archipelago (the map)"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


## Region Polar

class VolcanicGlacierBuildings(BuildingEnum):
    "The building IDs for all buildings in Volcanic Glacier"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


class SubpolarRiverBuildings(BuildingEnum):
    "The building IDs for all buildings in Subpolar River"
    # Turbine =           (100, "Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


class PollutedFjordBuildings(BuildingEnum):
    "The building IDs for all buildings in Polluted Fjord"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")



# Region Continental

class FloodedCityBuildings(BuildingEnum):
    "The building IDs for all buildings in Flooded City"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


class IrradiatedSprawlBuildings(BuildingEnum):
    "The building IDs for all buildings in Irradiated Sprawl"
    # Turbine =           (100, "Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


class ContinentalOutskirtsBuildings(BuildingEnum):
    "The building IDs for all buildings in Continental Outskirts"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")
    
    
    
# Region Arid

class ParchedDunesBuildings(BuildingEnum):
    "The building IDs for all buildings in Parched Dunes"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


class CanyonPeaksBuildings(BuildingEnum):
    "The building IDs for all buildings in Canyon Peaks"
    # Turbine =           (100, "Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")


class FrackedFloodplainBuildings(BuildingEnum):
    "The building IDs for all buildings in Fracked Floodplain"
    # Turbine =           (100, "Wind Turbine")
    # ToxinScrubber =     (101, "Toxin Scrubber")
    # Irrigator =         (102, "Irrigator")
    # Excavator =         (103, "Excavator")
    # WaterPump =         (104, "Water Pump")
    # Calcifier =         (105, "Calcifier")
    # ResearchCenter =    (200, "Research Center")
    # Hydroponium =       (201, "Hydroponium")
    # Beehive =           (202, "Beehive")
    # Arboretum =         (203, "Arboretum")
    # SolarAmplifier =    (205, "Solar Amplifier")
    # Airship =           (300, "Airship")
    # LoadingDock =       (301, "Loading Dock")
    # PoundLock =         (302, "Pound Lock")
    # RecyclingSilo =     (303, "Recycling Silo")
    # RecyclingDrone =    (304, "Recycling Drone")
    # SonicPulse =        (325, "Sonic Pulse")
    # WildlifeBridge =    (326, "Wildlife Bridge")
    # CloudSeeder =       (404, "Cloud Seeder")
    # AnimalObservatory = (500, "Animal Observatory")