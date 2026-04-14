from __future__ import annotations
from typing import List, Dict, Set, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum
from BaseClasses import Item, ItemClassification
# from .missions import Mission
if TYPE_CHECKING:
    from .world import TerraNilWorld

import os

print(os.getcwd())

ITEM_NAME_TO_ID = {}

class TerraNilItem(Item):
    game = "Terra Nil"

class Building(Enum):
    Turbine = 100, "Wind Turbine"
    ToxinScrubber = 101, "Toxin Scrubber"
    Irrigator = 102, "Irrigator"
    Excavator = 103, "Excavator"
    WaterPump = 104, "Water Pump"
    Calcifier = 105, "Calcifier"
    ResearchCenter = 200, "Research Center"
    Hydroponium = 201, "Hydroponium"
    Beehive = 202, "Beehive"
    Arboretum = 203, "Arboretum"
    SolarAmplifier = 205, "Solar Amplifier"
    Airship = 300, "Airship"
    LoadingDock = 301, "Loading Dock"
    PoundLock = 302, "Pound Lock"
    RecyclingSilo = 303, "Recycling Silo"
    RecyclingDrone = 304, "Recycling Drone"
    SonicPulse = 325, "Sonic Pulse"
    WildlifeBridge = 326, "Wildlife Bridge"
    CloudSeeder = 404, "Cloud Seeder"
    AnimalObservatory = 500, "Animal Observatory"

    def __int__(self):
        return self.value[0]

    def __str__(self):
        return self.value[1]

from enum import Enum

class Mission(Enum):
    All = 0, "All"
    RiverValley = 10, "River Valley"

    def __int__(self):
        return self.value[0]

    def __str__(self):
        return self.value[1]


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
class TNItem:
    name: str
    id: int
    classification: ItemClassification

    def __init__(self, name: str, id: int, classification: ItemClassification):
        self.name = name
        self.id = id
        self.classification = classification

    @classmethod
    def building(cls, mission: Mission, building: Building, classification = ItemClassification.progression):
        if (mission == Mission.All):
            return cls(f"{str(building)}", (1<<31) | (1<<30) | int(building), classification)
        else:
            return cls(f"{str(building)} ({str(mission)})", (1<<31) | (1<<30) | (int(mission)<<12) | int(building), classification)

    @classmethod
    def mission_unlock(cls, mission: Mission):
        return cls(f"{str(mission)} Unlock", (1<<31) | (1<<30) | (int(mission)<<12), ItemClassification.progression)

    def to_item(self, world: TerraNilWorld):
        return TerraNilItem(self.name, self.classification, self.id, world.player)

fillers: List[TNItem] = [
    TNItem("Wet Rock", 1, ItemClassification.filler),
]

precollected: List[TNItem] = [
    # Level Unlocks
    TNItem.mission_unlock(Mission.RiverValley),

    # River Valley Tier 1
    TNItem.building(Mission.RiverValley, Building.Turbine),
    TNItem.building(Mission.RiverValley, Building.ToxinScrubber),
]

items: List[TNItem] = [
    # River Valley Tier 1
    TNItem.building(Mission.RiverValley, Building.Irrigator),
    TNItem.building(Mission.RiverValley, Building.WaterPump),
    TNItem.building(Mission.RiverValley, Building.Calcifier, ItemClassification.useful),
    TNItem.building(Mission.RiverValley, Building.Excavator),

    # River Valley Tier 2
    TNItem.building(Mission.RiverValley, Building.Hydroponium),
    TNItem.building(Mission.RiverValley, Building.Beehive),
    TNItem.building(Mission.RiverValley, Building.SolarAmplifier),
    TNItem.building(Mission.RiverValley, Building.Arboretum),
    TNItem.building(Mission.RiverValley, Building.ResearchCenter),
    TNItem.building(Mission.RiverValley, Building.CloudSeeder),

    # River Valley Tier 3
    TNItem.building(Mission.RiverValley, Building.Airship),
    TNItem.building(Mission.RiverValley, Building.LoadingDock),
    TNItem.building(Mission.RiverValley, Building.PoundLock),
    TNItem.building(Mission.RiverValley, Building.RecyclingSilo),
    TNItem.building(Mission.RiverValley, Building.RecyclingDrone),
    TNItem.building(Mission.RiverValley, Building.SonicPulse),
    TNItem.building(Mission.RiverValley, Building.WildlifeBridge),
    TNItem.building(Mission.RiverValley, Building.AnimalObservatory),
]

for item in items + precollected + fillers:
    ITEM_NAME_TO_ID[item.name] = item.id

def get_filler_item_name(world: TerraNilWorld) -> str:
    n = world.random.randint(0, len(fillers) - 1)
    print(f"{len(fillers)} fillers exist, selected {n}")
    return fillers[n].name

def create_item(world: TerraNilWorld, name: str) -> TerraNilItem:
    print(f"looking up '{name}'")
    res = [item for item in items + precollected + fillers if item.name == name]
    print(f"{len(res)}: {res}")
    return [item for item in items + precollected + fillers if item.name == name][0].to_item(world)

def create_all_items(world: TerraNilWorld) -> None:
    pool: List[Item] = [world.create_item(item.name) for item in items]

    locations = len(world.multiworld.get_unfilled_locations(world.player))
    n_fillers = locations - len(pool)
    pool += [world.create_filler() for _ in range(n_fillers)]

    world.multiworld.itempool += pool

    for item in precollected:
        world.push_precollected(world.create_item(item.name))
