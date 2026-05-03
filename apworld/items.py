from __future__ import annotations
from typing import List, Literal, Any, Dict, Set, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum
from BaseClasses import Item, ItemClassification    #type: ignore
# from .missions import Mission     ##Deprecated; New one is Data/ItemData.py
from .Data.ItemData import RiverValleyData, DesolateIslandData, map_displayname_to_data, ITEM_NAME_TO_ID, ITEM_NAME_TO_CLASSIFICATION
if TYPE_CHECKING:
    from .world import TerraNilWorld # type: ignore

class TerraNilItem(Item):
    game = "TerraNil"
    
filler_names_ids_classification: List[tuple[str, int, Any]] = [
    ("Wet Rock", 1, ItemClassification.filler),
    ("10 Resources", 2, ItemClassification.filler),
    ("25 Resources", 3, ItemClassification.filler),
    ("50 Resources", 4, ItemClassification.filler),
    ("75 Resources", 5, ItemClassification.filler),
]

filler_toid = {key: value for key, value, _ in filler_names_ids_classification}
filler_toclassification = {key: value for key, _, value in filler_names_ids_classification}

ITEM_NAME_TO_ID |=              filler_toid
ITEM_NAME_TO_CLASSIFICATION |=  filler_toclassification

precollected_names: List[str] = [
    "River Valley Map",
    "River Valley Turbine",
    "River Valley Toxin Scrubber"
]


def get_filler_item_name(world: TerraNilWorld) -> str:
    n = world.random.randint(0, len(filler_names_ids_classification) - 1)
    print(f"{len(filler_names_ids_classification)} fillers exist, selected {n}")
    return filler_names_ids_classification[n][0]


def create_item(world: TerraNilWorld, name: str) -> TerraNilItem:
    item_id = ITEM_NAME_TO_ID[name]
    item_classification = ITEM_NAME_TO_CLASSIFICATION[name]
    return TerraNilItem(name, item_classification, item_id, world.player)


def create_all_items(world: TerraNilWorld) -> None:
    pool: List[Item] = [world.create_item(item) for item in ITEM_NAME_TO_ID.keys()]

    locations = len(world.multiworld.get_unfilled_locations(world.player))
    n_fillers = locations - len(pool)
    pool += [world.create_filler() for _ in range(n_fillers)]

    world.multiworld.itempool += pool

    for precollected_item_name in precollected_names:
        world.push_precollected(world.create_item(precollected_item_name))
        
        

## Deprecated: Use Data/ItemData.py
## I commented this away for now in case something goes wrong with the new ItemData method
# class Building(Enum):
#     Turbine = 100, "Wind Turbine"
#     ToxinScrubber = 101, "Toxin Scrubber"
#     Irrigator = 102, "Irrigator"
#     Excavator = 103, "Excavator"
#     WaterPump = 104, "Water Pump"
#     Calcifier = 105, "Calcifier"
#     SandBank = 107, "Sand Bank"
#     Mineralizer = 108, "Mineralizer"
#     ResearchCenter = 200, "Research Center"
#     Hydroponium = 201, "Hydroponium"
#     Beehive = 202, "Beehive"
#     Arboretum = 203, "Arboretum"
#     SolarAmplifier = 205, "Solar Amplifier"
#     Salinator = 208, "Salinator"
#     Littarium = 209, "Littarium"
#     ShadeclothPillar = 210, "Shadecloth Pillar"
#     CoralLab = 211, "Coral Lab"
#     MonorailNode = 212, "Monorail Node"
#     Airship = 300, "Airship"
#     LoadingDock = 301, "Loading Dock"
#     PoundLock = 302, "Pound Lock"
#     RecyclingSilo = 303, "Recycling Silo"
#     RecyclingDrone = 304, "Recycling Drone"
#     RecyclerStation = 305, "Recycler Station"
#     RecyclingBeacon = 306, "Recycling Beacon"
#     RockHopper = 324, "Rock Hopper"
#     SonicPulse = 325, "Sonic Pulse"
#     WildlifeBridge = 326, "Wildlife Bridge"
#     Combustor = 402, "Combustor"
#     CloudSeeder = 404, "Cloud Seeder"
#     AnimalObservatory = 500, "Animal Observatory"

#     def __int__(self):
#         return self.value[0]

#     def __str__(self):
#         return self.value[1]

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
# class TNItem:
#     name: str
#     id: int
#     classification: ItemClassification

#     def __init__(self, name: str, id: int, classification: ItemClassification):
#         self.name = name
#         self.id = id
#         self.classification = classification

#     @classmethod
#     def building(cls, mission: Mission, building: Building, classification = ItemClassification.progression):
#         if (mission == Mission.All):
#             return cls(f"{str(building)}", (1<<31) | (1<<30) | int(building), classification)
#         else:
#             return cls(f"{str(building)} ({str(mission)})", (1<<31) | (1<<30) | (int(mission)<<12) | int(building), classification)

#     @classmethod
#     def mission_unlock(cls, mission: Mission):
#         return cls(f"{str(mission)} Unlock", (1<<31) | (1<<30) | (int(mission)<<12), ItemClassification.progression)

#     def to_item(self, world: TerraNilWorld):
#         return TerraNilItem(self.name, self.classification, self.id, world.player)

# fillers: List[TNItem] = [
#     TNItem("Wet Rock", 1, ItemClassification.filler),
#     TNItem("10 Money", 2, ItemClassification.filler),
#     TNItem("25 Money", 3, ItemClassification.filler),
#     TNItem("50 Money", 4, ItemClassification.filler),
#     TNItem("75 Money", 5, ItemClassification.filler),
# ]

# precollected: List[TNItem] = [
#     # Level Unlocks
#     TNItem.mission_unlock(Mission.RiverValley),

#     # River Valley Tier 1
#     TNItem.building(Mission.RiverValley, Building.Turbine),
#     TNItem.building(Mission.RiverValley, Building.ToxinScrubber),
# ]

# items: List[TNItem] = [
#     # River Valley Tier 1
#     TNItem.building(Mission.RiverValley, Building.Irrigator),
#     TNItem.building(Mission.RiverValley, Building.WaterPump),
#     TNItem.building(Mission.RiverValley, Building.Calcifier, ItemClassification.useful),
#     TNItem.building(Mission.RiverValley, Building.Excavator),

#     # River Valley Tier 2
#     TNItem.building(Mission.RiverValley, Building.Hydroponium),
#     TNItem.building(Mission.RiverValley, Building.Beehive),
#     TNItem.building(Mission.RiverValley, Building.SolarAmplifier),
#     TNItem.building(Mission.RiverValley, Building.Arboretum),
#     TNItem.building(Mission.RiverValley, Building.ResearchCenter),
#     TNItem.building(Mission.RiverValley, Building.CloudSeeder),

#     # River Valley Tier 3
#     TNItem.building(Mission.RiverValley, Building.Airship),
#     TNItem.building(Mission.RiverValley, Building.LoadingDock),
#     TNItem.building(Mission.RiverValley, Building.PoundLock),
#     TNItem.building(Mission.RiverValley, Building.RecyclingSilo),
#     TNItem.building(Mission.RiverValley, Building.RecyclingDrone),
#     TNItem.building(Mission.RiverValley, Building.SonicPulse),
#     TNItem.building(Mission.RiverValley, Building.WildlifeBridge),
#     TNItem.building(Mission.RiverValley, Building.AnimalObservatory),

#     # Level Unlocks
#     TNItem.mission_unlock(Mission.DesolateIsland),

#     # Desolate Island Tier 1
#     TNItem.building(Mission.DesolateIsland, Building.Turbine),
#     TNItem.building(Mission.DesolateIsland, Building.ToxinScrubber),
#     TNItem.building(Mission.DesolateIsland, Building.Irrigator),
#     TNItem.building(Mission.DesolateIsland, Building.WaterPump),
#     TNItem.building(Mission.DesolateIsland, Building.Mineralizer),
#     TNItem.building(Mission.DesolateIsland, Building.SandBank),

#     # Desolate Island Tier 2
#     TNItem.building(Mission.DesolateIsland, Building.Hydroponium),
#     TNItem.building(Mission.DesolateIsland, Building.Littarium),
#     TNItem.building(Mission.DesolateIsland, Building.Salinator),
#     TNItem.building(Mission.DesolateIsland, Building.ShadeclothPillar),
#     TNItem.building(Mission.DesolateIsland, Building.MonorailNode),
#     TNItem.building(Mission.DesolateIsland, Building.CoralLab),

#     # Desolate Island Tier 3
#     TNItem.building(Mission.DesolateIsland, Building.Airship),
#     TNItem.building(Mission.DesolateIsland, Building.RecyclingSilo),
#     TNItem.building(Mission.DesolateIsland, Building.RecyclerStation),
#     TNItem.building(Mission.DesolateIsland, Building.RecyclingBeacon),
#     TNItem.building(Mission.DesolateIsland, Building.RockHopper),
#     TNItem.building(Mission.DesolateIsland, Building.SonicPulse),
#     TNItem.building(Mission.DesolateIsland, Building.AnimalObservatory),

#     # Desolate Island Weather
#     TNItem.building(Mission.DesolateIsland, Building.CloudSeeder),
#     TNItem.building(Mission.DesolateIsland, Building.Combustor),
# ]
