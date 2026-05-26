## Contains a list of all items in the game, as well as functions for turning them into IDs.

from enum import Enum
from typing import Any, Literal
from dataclasses import dataclass
from BaseClasses import ItemClassification  #type: ignore
from .ItemDataBuildings import *
from .MapData import *

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
        buildings_items_dict[f"{map.displayname} - {buildingdata}"] = (ItemClassification.progression) #TODO: Label correct classification
        buildings_toid_dict[f"{map.displayname} - {buildingdata}"]  = generate_building_id(map.InternalID, buildingdata.get_internalID(ignore_missing_ids = True))
    return buildings_items_dict, buildings_toid_dict


maps_classification: dict[str, ItemClassification] = dict()
for displayname in map_displayname_to_data.keys():
    maps_classification[f"{displayname} Unlock"] = (ItemClassification.progression)

maps_to_id = {
    f"{displayname} Unlock": generate_mapunlock_id(map_id=data.InternalID) for displayname, data in map_displayname_to_data.items()
}

buildings_rivervalley_classification, buildings_rivervalley_to_id = \
    generate_building_toclassification_and_toid_dict(RiverValleyBuildings, map_displayname_to_data["River Valley"])
buildings_abandonedquarry_classification, buildings_abandonedquarry_to_id = \
    generate_building_toclassification_and_toid_dict(AbandonedQuarryBuildings, map_displayname_to_data["Abandoned Quarry"])
buildings_pollutedbay_classification, buildings_pollutedbay_to_id = \
    generate_building_toclassification_and_toid_dict(PollutedBayBuildings, map_displayname_to_data["Polluted Bay"])
buildings_hillanddale_classification, buildings_hillanddale_to_id = \
    generate_building_toclassification_and_toid_dict(HillAndDaleBuildings, map_displayname_to_data["Hill and Dale"])
buildings_desolateisland_classification, buildings_desolateisland_to_id = \
    generate_building_toclassification_and_toid_dict(DesolateIslandBuildings, map_displayname_to_data["Desolate Island"])
buildings_scorchedcaldera_classification, buildings_scorchedcaldera_to_id = \
    generate_building_toclassification_and_toid_dict(ScorchedCalderaBuildings, map_displayname_to_data["Scorched Caldera"])
buildings_volcanicglacier_classification, buildings_volcanicglacier_to_id = \
    generate_building_toclassification_and_toid_dict(VolcanicGlacierBuildings, map_displayname_to_data["Volcanic Glacier"])

ITEM_NAME_TO_ID: dict[str, int] = \
    maps_to_id | \
    buildings_rivervalley_to_id | \
    buildings_abandonedquarry_to_id | \
    buildings_pollutedbay_to_id | \
    buildings_hillanddale_to_id | \
    buildings_desolateisland_to_id | \
    buildings_scorchedcaldera_to_id | \
    buildings_volcanicglacier_to_id

ITEM_NAME_TO_CLASSIFICATION: dict[str, Any] = \
    maps_classification | \
    buildings_rivervalley_classification | \
    buildings_abandonedquarry_classification | \
    buildings_pollutedbay_classification | \
    buildings_hillanddale_classification | \
    buildings_desolateisland_classification | \
    buildings_scorchedcaldera_classification | \
    buildings_volcanicglacier_classification

def main():
    print("\nMap IDs:")
    for key, value in maps_to_id.items():
        print(f"{key:<32}: 0b {value:b}, 0x{value:x}")

    print("\nRiver Valley Buildings IDs:")
    for key, value in buildings_rivervalley_to_id.items():
        print(f"{key:<32}: 0b {value:b}, 0x{value:x}")

    print("\nAbandoned Quarry Buildings IDs:")
    for key, value in buildings_abandonedquarry_to_id.items():
        print(f"{key:<32}: 0b {value:b}, 0x{value:x}")

    print("\nPolluted Bay Buildings IDs:")
    for key, value in buildings_pollutedbay_to_id.items():
        print(f"{key:<32}: 0b {value:b}, 0x{value:x}")

    print("\nHill and Dale Buildings IDs:")
    for key, value in buildings_hillanddale_to_id.items():
        print(f"{key:<32}: 0b {value:b}, 0x{value:x}")

    print("\nDesolate Island Buildings IDs:")
    for key, value in buildings_desolateisland_to_id.items():
        print(f"{key:<32}: 0b {value:b}, 0x{value:x}")

    print("\nScorched Caldera Buildings IDs:")
    for key, value in buildings_scorchedcaldera_to_id.items():
        print(f"{key:<32}: 0b {value:b}, 0x{value:x}")

    print("\nVolcanic Glacier Buildings IDs:")
    for key, value in buildings_volcanicglacier_to_id.items():
        print(f"{key:<32}: 0b {value:b}, 0x{value:x}")

if __name__ == "__main__":
    main()
