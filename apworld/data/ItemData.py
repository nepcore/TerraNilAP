## Contains a list of all items in the game, as well as functions for turning them into IDs.

from enum import Enum
# from BaseClasses import ItemClassification

# missions = {
#     "River Valley":          (ItemClassification.progression),
#     ## Currently only River Valley is implemented. Below are the other, yet-to-be-implemented regions

#     # "Hill and Dale":         (ItemClassification.progression),
#     # "Polluted Bay":          (ItemClassification.progression),
#     # "Abandoned Quarry":      (ItemClassification.progression),

#     # "Desolate Island":       (ItemClassification.progression),
#     # "Scorched Caldera":      (ItemClassification.progression),
#     # "Archipelago":           (ItemClassification.progression),

#     # "Volcanic Glacier":      (ItemClassification.progression),
#     # "Subpolar River":        (ItemClassification.progression),
#     # "Polluted Fjord":        (ItemClassification.progression),

#     # "Flooded City":          (ItemClassification.progression),
#     # "Continental Outskirts": (ItemClassification.progression),
#     # "Irradiated Sprawl":     (ItemClassification.progression),

#     # "Parched Dunes":         (ItemClassification.progression),
#     # "Canyon Peaks":          (ItemClassification.progression),
#     # "Fracked Floodplain":    (ItemClassification.progression),
# }

region_ids = {
    "River Valley": 0b000000001010,
    # "Hill and Dale": 0o01,
    # "Polluted Bay": 0o02,
    # "Abandoned Quarry": 0o03,

    # "Desolate Island": 0o10,
    # "Scorched Caldera": 0o11,
    # "Archipelago": 0o12,

    # "Volcanic Glacier": 0o20,
    # "Subpolar River": 0o21,
    # "Polluted Fjord": 0o22,

    # "Flooded City": 0o30,
    # "Continental Outskirts": 0o31,
    # "Irradiated Sprawl": 0o32,

    # "Parched Dunes": 0o40,
    # "Canyon Peaks": 0o41,
    # "Fracked Floodplain": 0o42,
}

class BuildingEnum(Enum):
    def __int__(self):
        return self.value[0]

    def __str__(self):
        return self.value[1]


class RiverValleyBuildings(BuildingEnum):
    "The building IDs for all buildings in River Valley"
    Turbine =           (100, "Wind Turbine")
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



# THis world considers all of its own item IDs to be 32 bit
# Any ID with the highest order bit set is treated in a special way by the client mod
# All other IDs are just normal numbers that cover any items that do not fit the following schema
#
# For IDs with the highest order bit set there are an additional 7 bits that act as flags
# The first bit should be set if the item is a building or mission unlock
# the other flag bits are reserved to eventually be used for things like animal or climate parameter unlocks
# After those first 8 bits there are 12 bits denoting the mission id and 12 bits denoting the item
# if the mission bits are all 0 the item is considered to apply to all missions
# if the building unlock bit is set, the mission bits are not all 0, and the item bits are all 0 it is considered to be unlocking that mission
#
# As an example this is the ID for the river valley wind turbine
# Signifies this ID is using the above schema
# | This is a building unlock
# | |
# 1 1 000000 000000001010 000001100100
#           |  MissionID | BuildingID |


# For Building IDs, we follow the following convention:
def generate_building_id(region_id: int, slot_number: int) -> int:
    """
    Constructs an ID for a given building based on it's region id, tier, and the slot number.

    The ID is a 32-bit integer. 
    The first bit is always 1.
    The second bit denotes that this item is a building unlock, and will be set to 1.
    The next bits denote other use cases, which are thus unset.

    The next 12 bits denote the region id.
    The next 12 bits denote the slot id.
    These are determined by the game itself and immutable.
    """
    first_bit = 1 << 31
    classification_bits = 1 << 30 #This is a building
    region_bits = region_id << 12
    slot_bits = slot_number
    return first_bit | classification_bits | region_bits | slot_bits




buildings_rivervalley_to_id = {
    str(x): generate_building_id(region_ids["River Valley"], int(x)) for x in RiverValleyBuildings
}

for key, value in buildings_rivervalley_to_id.items():
    print(f"{key:<20}: {value:b}")
