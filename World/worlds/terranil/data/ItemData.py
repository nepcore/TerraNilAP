## Contains a list of all items in the game, as well as functions for turning them into IDs.

from enum import Enum
from dataclasses import dataclass
from BaseClasses import ItemClassification
from worlds.terranil.data.ItemBuildingsLists import RiverValleyBuildings


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
    InternalName: str
    region:       str

    def __str__(self) -> str:
        return self.displayname
    
    def __int__(self) -> int:
        return self.InternalID
    
    def read_data(self) -> str:
        return f"Map {self.displayname} of region {self.region} with internal ID {self.InternalID} and name {self.InternalName}"


all_map_datas = {
    "River Valley":          TerraNilMapData(displayname = "River Valley",          region = "Temperate", InternalID= 10, InternalName= "TemperateRiver"),
    "Abandoned Quarry":      TerraNilMapData(displayname = "Abandoned Quarry",      region = "Temperate", InternalID= 11, InternalName= "TemperateQuarry"),
    "Polluted Bay":          TerraNilMapData(displayname = "Polluted Bay",          region = "Temperate", InternalID= 11, InternalName= "TemperateBay"),
    "Hill and Dale":         TerraNilMapData(displayname = "Hill and Dale",         region = "Temperate", InternalID= 13, InternalName= "TemperateHillAndDale"),

    "Desolate Island":       TerraNilMapData(displayname = "Desolate Island",       region = "Tropical", InternalID= 20, InternalName= "TropicalIsland"),
    "Archipelago":           TerraNilMapData(displayname = "Archipelago",           region = "Tropical", InternalID= 21, InternalName= "TropicalArchipelago"),
    "Scorched Caldera":      TerraNilMapData(displayname = "Scorched Caldera",      region = "Tropical", InternalID= 22, InternalName= "TropicalCaldera"),

    "Volcanic Glacier":      TerraNilMapData(displayname = "Volcanic Glacier",      region = "Polar", InternalID= 30, InternalName= "PolarVolcano"),
    "Polluted Fjord":        TerraNilMapData(displayname = "Polluted Fjord",        region = "Polar", InternalID= 31, InternalName= "PolarFjord"),
    "Subpolar River":        TerraNilMapData(displayname = "Subpolar River",        region = "Polar", InternalID= 32, InternalName= "SubpolarRiver"),

    "Flooded City":          TerraNilMapData(displayname = "Flooded City",          region = "Continental", InternalID= 50, InternalName= "CoastalCity"),
    "Irradiated Sprawl":     TerraNilMapData(displayname = "Irradiated Sprawl",     region = "Continental", InternalID= 51, InternalName= "IslandCity"),
    "Continental Outskirts": TerraNilMapData(displayname = "Continental Outskirts", region = "Continental", InternalID= 52, InternalName= "ContinentalOutskirt"),

    "Parched Dunes":         TerraNilMapData(displayname = "Parched Dunes",         region = "Arid", InternalID= 41, InternalName= "AridDelta"),
    "Canyon Peaks":          TerraNilMapData(displayname = "Canyon Peaks",          region = "Arid", InternalID= 42, InternalName= "AridCanyon"),
    "Fracked Floodplain":    TerraNilMapData(displayname = "Fracked Floodplain",    region = "Arid", InternalID= 43, InternalName= "AridSwamp"),
}

def get_map_id(map_name: str) -> int:
    "Returns the ID for a given display name for a map."
    return all_map_datas[map_name].InternalID

def get_map_internal_name(map_name: str) -> str:
    "Returns the internal name for a given display name for a map."
    return all_map_datas[map_name].InternalName



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


maps_as_items: dict[str, ItemClassification] = dict()
for displayname, data in all_map_datas.items():
    maps_as_items[f"{displayname} Map"] = (ItemClassification.progression)
    
maps_to_id = {
    f"{displayname} Map": generate_mapunlock_id(map_id=data.InternalID) for displayname, data in all_map_datas.items()
}
    
buildings_rivervalley_as_items = dict()
for displayname in RiverValleyBuildings:
    buildings_rivervalley_as_items[f"River Valley {displayname}"] = (ItemClassification.progression)

buildings_rivervalley_to_id = {
    f"River Valley {str(x)}" : generate_building_id(get_map_id("River Valley"), int(x)) for x in RiverValleyBuildings
}

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
        
if __name__ == "__main__":
    main()