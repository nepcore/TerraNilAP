## Contains a list of all items in the game, as well as functions for turning them into IDs.

from enum import Enum
from typing import Any, Literal
from dataclasses import dataclass
from BaseClasses import ItemClassification  #type: ignore
from .ItemDataBuildings import *

@dataclass
class TerraNilMapData:
    """
    A dataclass containing the internal name, internal id, displayname as well as the region of a certain map.

    Methods:
    __str__: returns the display name.
    __int__: returns the internal id.
    read_data: returns all the data as a string in a human-readable format.
    as_dict: returns the data as a dictionary
    """
    displayname:  str
    InternalID:   int
    region:       str

    def __str__(self) -> str:
        return self.displayname
    
    def __int__(self) -> int:
        return self.InternalID
    
    def read_data(self) -> str:
        "Provides a human-readable oversight of the stored data."
        return f"Map {self.displayname} of region {self.region} with internal ID {self.InternalID}"
    

RiverValleyData =            TerraNilMapData(displayname = "River Valley",          region = "Temperate", InternalID = 10)
AbandonedQuarryData =        TerraNilMapData(displayname = "Abandoned Quarry",      region = "Temperate", InternalID = 11)
PollutedBayData =            TerraNilMapData(displayname = "Polluted Bay",          region = "Temperate", InternalID = 12)
HillandDaleData =            TerraNilMapData(displayname = "Hill and Dale",         region = "Temperate", InternalID = 13)

DesolateIslandData =         TerraNilMapData(displayname = "Desolate Island",       region = "Tropical", InternalID = 20)
ArchipelagoData =            TerraNilMapData(displayname = "Archipelago",           region = "Tropical", InternalID = 21)
ScorchedCalderaData =        TerraNilMapData(displayname = "Scorched Caldera",      region = "Tropical", InternalID = 22)

VolcanicGlacierData =        TerraNilMapData(displayname = "Volcanic Glacier",      region = "Polar", InternalID = 30)
PollutedFjordData =          TerraNilMapData(displayname = "Polluted Fjord",        region = "Polar", InternalID = 31)
SubpolarRiverData =          TerraNilMapData(displayname = "Subpolar River",        region = "Polar", InternalID = 32)

FloodedCityData =            TerraNilMapData(displayname = "Flooded City",          region = "Continental", InternalID = 50)
IrradiatedSprawlData =       TerraNilMapData(displayname = "Irradiated Sprawl",     region = "Continental", InternalID = 51)
ContinentalOutskirtsData =   TerraNilMapData(displayname = "Continental Outskirts", region = "Continental", InternalID = 52)

ParchedDunesData =           TerraNilMapData(displayname = "Parched Dunes",         region = "Arid", InternalID = 41)
CanyonPeaksData =            TerraNilMapData(displayname = "Canyon Peaks",          region = "Arid", InternalID = 42)
FrackedFloodplainData =      TerraNilMapData(displayname = "Fracked Floodplain",    region = "Arid", InternalID = 43)


map_displayname_to_data: dict[str, TerraNilMapData] = {
    "River Valley":          RiverValleyData,
    # "Abandoned Quarry":      AbandonedQuarryData,
    # "Polluted Bay":          PollutedBayData,
    # "Hill and Dale":         HillandDaleData,

    "Desolate Island":       DesolateIslandData,
    # "Archipelago":           ArchipelagoData,
    # "Scorched Caldera":      ScorchedCalderaData,

    # "Volcanic Glacier":      VolcanicGlacierData,
    # "Polluted Fjord":        PollutedFjordData,
    # "Subpolar River":        SubpolarRiverData,

    # "Flooded City":          FloodedCityData,
    # "Irradiated Sprawl":     IrradiatedSprawlData,
    # "Continental Outskirts": ContinentalOutskirtsData,

    # "Parched Dunes":         ParchedDunesData,
    # "Canyon Peaks":          CanyonPeaksData,
    # "Fracked Floodplain":    FrackedFloodplainData,
}

def get_map_id(map_name: str) -> int:
    "Returns the ID for a given display name for a map."
    return map_displayname_to_data[map_name].InternalID



# This world considers all of its own item IDs to be 32 bit
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


# For Map IDs, we follow the following convention:
def generate_mapunlock_id(map_id: int) -> int:
    """
    Constructs an ID for a given building based on it's region id, tier, and the slot number.

    The ID is a 32-bit integer. 
    The first bit is always 1.
    The next bit denotes that this item is a building or map unlock, and will be set to 1.
    The next 7 bits denote other use cases, which are thus unset.

    The next 12 bits denote the region id.
    The next 12 bits are 0.
    These are determined by the game itself and immutable.
    """
    first_bit = 1 << 31
    classification_bits = 1 << 30 #This is a a map
    map_bits = map_id << 12
    return first_bit | classification_bits | map_bits

# For Building IDs, we follow the following convention:
def generate_building_id(map_id: int, slot_number: int) -> int:
    """
    Constructs an ID for a given building based on it's region id, tier, and the slot number.

    The ID is a 32-bit integer. 
    The first bit is always 1.
    The second bit denotes that this item is a building or map unlock, and will be set to 1.
    The next 6 bits denote other use cases, which are thus unset.

    The next 12 bits denote the region id.
    The next 12 bits denote the slot id.
    These are determined by the game itself and immutable.
    """
    first_bit = 1 << 31
    classification_bits = 1 << 30 #This is a building
    map_bits = map_id << 12
    slot_bits = slot_number
    return first_bit | classification_bits | map_bits | slot_bits

def generate_building_toclassification_and_toid_dict(source, map: TerraNilMapData) -> tuple[dict[str, Literal[ItemClassification.progression]], dict[str, int]]: # type: ignore
    "Generates a dictionary of building items and ids for a given BuildingEnum and map"
    buildings_items_dict: dict[str, Literal[ItemClassification.progression]] = dict() # type: ignore
    buildings_toid_dict: dict[str, int] = dict()
    for buildingdata in source:
        buildings_items_dict[f"{map.displayname} {buildingdata}"] = (ItemClassification.progression) #TODO: Label correct classification
        buildings_toid_dict[f"{map.displayname} {buildingdata}"]  = generate_building_id(map.InternalID, buildingdata.get_internalID(ignore_missing_ids = True))
    return buildings_items_dict, buildings_toid_dict


maps_classification: dict[str, ItemClassification] = dict()
for displayname in map_displayname_to_data.keys():
    maps_classification[f"{displayname} Map"] = (ItemClassification.progression)
    
maps_to_id = {
    f"{displayname} Map": generate_mapunlock_id(map_id=data.InternalID) for displayname, data in map_displayname_to_data.items()
}
    
buildings_rivervalley_classification, buildings_rivervalley_to_id = generate_building_toclassification_and_toid_dict(RiverValleyBuildings, map_displayname_to_data["River Valley"])
buildings_desolateisland_classification, buildings_desolateisland_to_id = generate_building_toclassification_and_toid_dict(DesolateIslandBuildings, map_displayname_to_data["Desolate Island"])

buildings_rivervalley_to_id = {
    f"River Valley {str(x)}" : generate_building_id(get_map_id("River Valley"), int(x)) for x in RiverValleyBuildings
}

ITEM_NAME_TO_ID: dict[str, int] = \
    maps_to_id | \
    buildings_desolateisland_to_id | \
    buildings_rivervalley_to_id
    
ITEM_NAME_TO_CLASSIFICATION: dict[str, Any] = \
    maps_classification | \
    buildings_rivervalley_classification | \
    buildings_desolateisland_classification

def main():
    # print("Map items:")
    # for key, value in maps_as_items.items():
    #     print(f"{key:<32}")
        
    print("\nMap IDs:")
    for key, value in maps_to_id.items():
        print(f"{key:<32}: 0b {value:b}, 0x{value:x}")
        
    # print("\nRiver Valley Buildings items:")
    # for key, value in buildings_rivervalley_as_items.items():
    #     print(f"{key:<32}")
        
    print("\nRiver Valley Buildings IDs:")
    for key, value in buildings_rivervalley_to_id.items():
        print(f"{key:<32}: 0b {value:b}, 0x{value:x}")
        
    print("\nRiver Valley Buildings IDs:")
    for key, value in buildings_desolateisland_to_id.items():
        print(f"{key:<32}: 0b {value:b}, 0x{value:x}")
        
if __name__ == "__main__":
    main()