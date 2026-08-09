from __future__ import annotations
from typing import List, Literal, Any, Dict, Set, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum
from BaseClasses import Item, ItemClassification    #type: ignore
from Options import OptionError
from .Data.ItemData import RiverValleyData, DesolateIslandData, map_displayname_to_data, ITEM_NAME_TO_ID, ITEM_NAME_TO_CLASSIFICATION, items_by_level
if TYPE_CHECKING:
    from .world import TerraNilWorld # type: ignore

class TerraNilItem(Item):
    game = "TerraNil"

filler_names_ids_classification: List[tuple[str, int, Any]] = [
    ("Wet Rock", 1, ItemClassification.filler),
    ("10 Money", 2, ItemClassification.filler),
    ("25 Money", 3, ItemClassification.filler),
    ("50 Money", 4, ItemClassification.filler),
    ("75 Money", 5, ItemClassification.filler),
]

filler_toid = {key: value for key, value, _ in filler_names_ids_classification}
filler_toclassification = {key: value for key, _, value in filler_names_ids_classification}

ITEM_NAME_TO_ID |=              filler_toid
ITEM_NAME_TO_CLASSIFICATION |=  filler_toclassification

precollected_names = {
    "River Valley": [
        "Wind Turbine",
        "Toxin Scrubber",
    ],
    "Hill and Dale": [
        "Wind Turbine",
        "Cone Filter",
    ],
    "Polluted Bay": [
        "Tidal Turbine",
        "Toxin Scrubber",
    ],
    "Abandoned Quarry": [
        "Wind Turbine",
        "Toxin Scrubber",
        "Seismic Detonator",
    ],
    "Desolate Island": [
        "Wind Turbine",
        "Toxin Scrubber",
    ],
    "Scorched Caldera": [
        "Geothermal Plant",
        "Seismic Detonator",
        "Cone Filter",
    ],
    "Volcanic Glacier": [
        "Geothermal Plant",
        "Seismic Detonator",
        "Toxin Scrubber"
    ]
}

early_names = {
    "River Valley": [
        "Irrigator",
    ],
    "Hill and Dale": [
        "Irrigator",
    ],
    "Polluted Bay": [
        "Pylon",
        "Irrigator",
    ],
    "Abandoned Quarry": [
        "Irrigator",
        "Water Pump",
    ],
    "Desolate Island": [
        "Irrigator",
        "Mineralizer",
    ],
    "Scorched Caldera": [
        "Irrigator",
    ],
    "Volcanic Glacier": [
        "Irrigator",
    ]
}


def get_filler_item_name(world: TerraNilWorld) -> str:
    n = world.random.randint(0, len(filler_names_ids_classification) - 1)
    return filler_names_ids_classification[n][0]


def create_item(world: TerraNilWorld, name: str) -> TerraNilItem:
    item_id = ITEM_NAME_TO_ID[name]
    item_classification = ITEM_NAME_TO_CLASSIFICATION[name]
    return TerraNilItem(name, item_classification, item_id, world.player)


def create_all_items(world: TerraNilWorld) -> None:
    precollected = [f"{world.starting_level} - {item}" for item in precollected_names[world.starting_level]]
    precollected += [f"{world.starting_level} Unlock"]

    for item in early_names[world.starting_level]:
        world.multiworld.early_items[world.player][item] = 1

    items = []
    for level in world.levels_enabled:
        items += items_by_level[level]
    pool: List[Item] = [world.create_item(item) for item in items if item not in precollected]

    locations = len(world.multiworld.get_unfilled_locations(world.player))
    n_fillers = locations - len(pool)
    pool += [world.create_filler() for _ in range(n_fillers)]

    world.multiworld.itempool += pool

    for precollected_item_name in precollected:
        world.push_precollected(world.create_item(precollected_item_name))
