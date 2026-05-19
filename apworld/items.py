from __future__ import annotations
from typing import List, Literal, Any, Dict, Set, TYPE_CHECKING
from dataclasses import dataclass
from enum import Enum
from BaseClasses import Item, ItemClassification    #type: ignore
from Options import OptionError
from .Data.ItemData import RiverValleyData, DesolateIslandData, map_displayname_to_data, ITEM_NAME_TO_ID, ITEM_NAME_TO_CLASSIFICATION
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

precollected_names: List[str] = {
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

    pool: List[Item] = [world.create_item(item) for item in ITEM_NAME_TO_ID.keys() if item not in precollected]

    locations = len(world.multiworld.get_unfilled_locations(world.player))
    n_fillers = locations - len(pool)
    pool += [world.create_filler() for _ in range(n_fillers)]

    world.multiworld.itempool += pool

    for precollected_item_name in precollected:
        world.push_precollected(world.create_item(precollected_item_name))
