from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification, Location
from . import items
if TYPE_CHECKING:
    from .world import TerraNilWorld

RIVER_VALLEY = (1<<31) | (10<<12)

LOCATION_NAME_TO_ID = {
    "First Energy (River Valley)": RIVER_VALLEY | 1,
    "First Pollution Removed (River Valley)": RIVER_VALLEY | 2,
    "First Greenery (River Valley)": RIVER_VALLEY | 3,
    "First Water (River Valley)": RIVER_VALLEY | 4,
    "Greenery 25% (River Valley)": RIVER_VALLEY | 5,
    "Greenery 50% (River Valley)": RIVER_VALLEY | 6,
    "Greenery 75% (River Valley)": RIVER_VALLEY | 7,
    "Greenery 100% (River Valley)": RIVER_VALLEY | 8,

    "First Fynbos (River Valley)": RIVER_VALLEY | 10,
    "First Wetlands (River Valley)": RIVER_VALLEY | 11,
    "First Forest (River Valley)": RIVER_VALLEY | 12,
    "First Fire (River Valley)": RIVER_VALLEY | 13,
    "Fynbos Completed (River Valley)": RIVER_VALLEY | 14,
    "Wetlands Completed (River Valley)": RIVER_VALLEY | 15,
    "Forest Completed (River Valley)": RIVER_VALLEY | 16,

    "First Recycling (River Valley)": RIVER_VALLEY | 18,
    "Recycling Completed (River Valley)": RIVER_VALLEY | 19,
    "3 Photo Stars (River Valley)": RIVER_VALLEY | 20,
    "10 Photo Stars (River Valley)": RIVER_VALLEY | 21,
    "Bronze Photo (River Valley)": RIVER_VALLEY | 22,
    "Silver Photo (River Valley)": RIVER_VALLEY | 23,
    "Gold Photo (River Valley)": RIVER_VALLEY | 24,

    "Waterlillies Blossom (River Valley)": RIVER_VALLEY | 26,
    "Migratory Birds Return (River Valley)": RIVER_VALLEY | 27,
    "Ferns On Riverbanks (River Valley)": RIVER_VALLEY | 28,
    "Fungi In Forests (River Valley)": RIVER_VALLEY | 29,
    "Rains Begin (River Valley)": RIVER_VALLEY | 30,
    "Wildflower Blooms (River Valley)": RIVER_VALLEY | 31,
    "Salmon Run (River Valley)": RIVER_VALLEY | 32,
}

class TerraNilLocation(Location):
    game = "TerraNil"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: TerraNilWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: TerraNilWorld) -> None:
    rivervalleyt1 = world.get_region("River Valley Tier 1")
    rivervalleyt2 = world.get_region("River Valley Tier 2")
    rivervalleyt3 = world.get_region("River Valley Tier 3")

    rivervalleyt1.add_locations(get_location_names_with_ids([
        "First Energy (River Valley)",
        "First Pollution Removed (River Valley)",
        "First Greenery (River Valley)",
        "First Water (River Valley)",
        "Greenery 25% (River Valley)",
        "Greenery 50% (River Valley)",
        "Greenery 75% (River Valley)",
        "Greenery 100% (River Valley)",
    ]), TerraNilLocation)

    rivervalleyt2.add_locations(get_location_names_with_ids([
        "First Fynbos (River Valley)",
        "First Wetlands (River Valley)",
        "First Forest (River Valley)",
        "First Fire (River Valley)",
        "Fynbos Completed (River Valley)",
        "Wetlands Completed (River Valley)",
        "Forest Completed (River Valley)",
    ]), TerraNilLocation)

    rivervalleyt3.add_locations(get_location_names_with_ids([
        "First Recycling (River Valley)",
        "Recycling Completed (River Valley)",
        "3 Photo Stars (River Valley)",
        "10 Photo Stars (River Valley)",
        "Bronze Photo (River Valley)",
        "Silver Photo (River Valley)",
        "Gold Photo (River Valley)",
    ]), TerraNilLocation)

    if world.options.climate_goals:
        rivervalleyclimate = world.get_region("River Valley Climate Goals")
        rivervalleyclimate.add_locations(get_location_names_with_ids([
            "Waterlillies Blossom (River Valley)",
            "Migratory Birds Return (River Valley)",
            "Ferns On Riverbanks (River Valley)",
            "Fungi In Forests (River Valley)",
            "Rains Begin (River Valley)",
            "Wildflower Blooms (River Valley)",
            "Salmon Run (River Valley)",
        ]), TerraNilLocation)

def create_events(world: TerraNilWorld) -> None:
    rivervalleyt1 = world.get_region("River Valley Tier 1")
    rivervalleyt2 = world.get_region("River Valley Tier 2")
    rivervalleyt3 = world.get_region("River Valley Tier 3")

    rivervalleyt1.add_event(
        "Tier 1 Completed (River Valley)",
        "Tier 1 Completed (River Valley)",
        location_type=TerraNilLocation,
        item_type=items.TerraNilItem
    )

    rivervalleyt2.add_event(
        "Tier 2 Completed (River Valley)",
        "Tier 2 Completed (River Valley)",
        location_type=TerraNilLocation,
        item_type=items.TerraNilItem
    )

    rivervalleyt3.add_event(
        "Liftoff (River Valley)",
        "Liftoff (River Valley)",
        location_type=TerraNilLocation,
        item_type=items.TerraNilItem
    )
