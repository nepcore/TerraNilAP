from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification, Location
from . import items
if TYPE_CHECKING:
    from .world import TerraNilWorld

RIVER_VALLEY = (1<<31) | (10<<12)
ABANDONED_QUARRY = (1<<31) | (11<<12)
POLLUTED_BAY = (1<<31) | (12<<12)
HILL_AND_DALE = (1<<31) | (13<<12)
DESOLATE_ISLAND = (1<<31) | (20<<12)
SCORCHED_CALDERA = (1<<31) | (22<<12)
VOLCANIC_GLACIER = (1<<31) | (30<<12)

locations = {
    "River Valley": [
        {
            "River Valley - First Energy": RIVER_VALLEY | 1,
            "River Valley - First Pollution Removed": RIVER_VALLEY | 2,
            "River Valley - First Greenery": RIVER_VALLEY | 3,
            "River Valley - First Water": RIVER_VALLEY | 4,
            "River Valley - Greenery 25%": RIVER_VALLEY | 5,
            "River Valley - Greenery 50%": RIVER_VALLEY | 6,
            "River Valley - Greenery 75%": RIVER_VALLEY | 7,
            "River Valley - Greenery 100%": RIVER_VALLEY | 8,
        },
        {
            "River Valley - First Fynbos": RIVER_VALLEY | 10,
            "River Valley - First Wetlands": RIVER_VALLEY | 11,
            "River Valley - First Forest": RIVER_VALLEY | 12,
            "River Valley - First Fire": RIVER_VALLEY | 13,
            "River Valley - Fynbos Completed": RIVER_VALLEY | 14,
            "River Valley - Wetlands Completed": RIVER_VALLEY | 15,
            "River Valley - Forest Completed": RIVER_VALLEY | 16,
        },
        {
            "River Valley - First Recycling": RIVER_VALLEY | 18,
            "River Valley - Recycling Completed": RIVER_VALLEY | 19,
            "River Valley - 3 Photo Stars": RIVER_VALLEY | 20,
            "River Valley - 10 Photo Stars": RIVER_VALLEY | 21,
            "River Valley - Bronze Photo": RIVER_VALLEY | 100,
            "River Valley - Silver Photo": RIVER_VALLEY | 101,
            "River Valley - Gold Photo": RIVER_VALLEY | 102,
        },
        {
            "River Valley - Waterlillies Blossom": RIVER_VALLEY | 26,
            "River Valley - Migratory Birds Return": RIVER_VALLEY | 27,
            "River Valley - Ferns On Riverbanks": RIVER_VALLEY | 28,
            "River Valley - Fungi In Forests": RIVER_VALLEY | 29,
            "River Valley - Rains Begin": RIVER_VALLEY | 30,
            "River Valley - Wildflower Blooms": RIVER_VALLEY | 31,
            "River Valley - Salmon Run": RIVER_VALLEY | 32,
        },
    ],
    "Abandoned Quarry": [
        {
            "Abandoned Quarry - First Energy": ABANDONED_QUARRY | 1,
            "Abandoned Quarry - First Lava": ABANDONED_QUARRY | 2,
            "Abandoned Quarry - First Water": ABANDONED_QUARRY | 3,
            "Abandoned Quarry - First Pollution Removed": ABANDONED_QUARRY | 4,
            "Abandoned Quarry - First Greenery": ABANDONED_QUARRY | 5,
            "Abandoned Quarry - Greenery 25%": ABANDONED_QUARRY | 6,
            "Abandoned Quarry - Greenery 50%": ABANDONED_QUARRY | 7,
            "Abandoned Quarry - Greenery 75%": ABANDONED_QUARRY | 8,
            "Abandoned Quarry - Greenery 100%": ABANDONED_QUARRY | 9,
        },
        {
            "Abandoned Quarry - First Fynbos": ABANDONED_QUARRY | 10,
            "Abandoned Quarry - First Wetlands": ABANDONED_QUARRY | 11,
            "Abandoned Quarry - First Forest": ABANDONED_QUARRY | 12,
            "Abandoned Quarry - First Fire": ABANDONED_QUARRY | 13,
            "Abandoned Quarry - Fynbos Completed": ABANDONED_QUARRY | 14,
            "Abandoned Quarry - Wetlands Completed": ABANDONED_QUARRY | 15,
            "Abandoned Quarry - Forest Completed": ABANDONED_QUARRY | 16,
        },
        {
            "Abandoned Quarry - First Recycling": ABANDONED_QUARRY | 20,
            "Abandoned Quarry - Recycling Completed": ABANDONED_QUARRY | 21,
            "Abandoned Quarry - 3 Photo Stars": ABANDONED_QUARRY | 22,
            "Abandoned Quarry - 10 Photo Stars": ABANDONED_QUARRY | 23,
            "Abandoned Quarry - Bronze Photo": ABANDONED_QUARRY | 100,
            "Abandoned Quarry - Silver Photo": ABANDONED_QUARRY | 101,
            "Abandoned Quarry - Gold Photo": ABANDONED_QUARRY | 102,
        },
        {
            "Abandoned Quarry - Wildflower Bloom": ABANDONED_QUARRY | 30,
            "Abandoned Quarry - Migratory Birds Return": ABANDONED_QUARRY | 31,
            "Abandoned Quarry - Fungi In Forests": ABANDONED_QUARRY | 32,
            "Abandoned Quarry - Ferns On Riverbanks": ABANDONED_QUARRY | 33,
            "Abandoned Quarry - Waterlilies Blossom": ABANDONED_QUARRY | 34,
            "Abandoned Quarry - Salmon Run": ABANDONED_QUARRY | 35,
            "Abandoned Quarry - Rains Begin": ABANDONED_QUARRY | 36,
        },
    ],
    "Polluted Bay": [
        {
            "Polluted Bay - First Energy": POLLUTED_BAY | 1,
            "Polluted Bay - First Pollution Removed": POLLUTED_BAY | 2,
            "Polluted Bay - First Greenery": POLLUTED_BAY | 3,
            "Polluted Bay - First Water": POLLUTED_BAY | 4,
            "Polluted Bay - Greenery 25%": POLLUTED_BAY | 5,
            "Polluted Bay - Greenery 50%": POLLUTED_BAY | 6,
            "Polluted Bay - Greenery 75%": POLLUTED_BAY | 7,
            "Polluted Bay - Greenery 100%": POLLUTED_BAY | 8,
        },
        {
            "Polluted Bay - First Fynbos": POLLUTED_BAY | 10,
            "Polluted Bay - First Wetlands": POLLUTED_BAY | 11,
            "Polluted Bay - First Forest": POLLUTED_BAY | 12,
            "Polluted Bay - First Fire": POLLUTED_BAY | 13,
            "Polluted Bay - Fynbos Completed": POLLUTED_BAY | 14,
            "Polluted Bay - Wetlands Completed": POLLUTED_BAY | 15,
            "Polluted Bay - Forest Completed": POLLUTED_BAY | 16,
            "Polluted Bay - First Deciduous Forest": POLLUTED_BAY | 17,
            "Polluted Bay - Deciduous Forest Completed": POLLUTED_BAY | 18,
        },
        {
            "Polluted Bay - First Recycling": POLLUTED_BAY | 20,
            "Polluted Bay - Recycling Completed": POLLUTED_BAY | 21,
            "Polluted Bay - 3 Photo Stars": POLLUTED_BAY | 22,
            "Polluted Bay - 10 Photo Stars": POLLUTED_BAY | 23,
            "Polluted Bay - Bronze Photo": POLLUTED_BAY | 100,
            "Polluted Bay - Silver Photo": POLLUTED_BAY | 101,
            "Polluted Bay - Gold Photo": POLLUTED_BAY | 102,
        },
        {
            "Polluted Bay - Wildflower Bloom": POLLUTED_BAY | 30,
            "Polluted Bay - Migratory Birds Return": POLLUTED_BAY | 31,
            "Polluted Bay - Fungi In Forests": POLLUTED_BAY | 32,
            "Polluted Bay - Ferns On Riverbanks": POLLUTED_BAY | 33,
            "Polluted Bay - Cliff Foliage": POLLUTED_BAY | 34,
            "Polluted Bay - Waterlilies Blossom": POLLUTED_BAY | 35,
            "Polluted Bay - Salmon Run": POLLUTED_BAY | 36,
            "Polluted Bay - Vegetation Boom": POLLUTED_BAY | 37,
            "Polluted Bay - Rains Begin": POLLUTED_BAY | 38,
        },
    ],
    "Hill and Dale": [
        {
            "Hill and Dale - First Energy": HILL_AND_DALE | 1,
            "Hill and Dale - First Pollution Removed": HILL_AND_DALE | 2,
            "Hill and Dale - First Greenery": HILL_AND_DALE | 3,
            "Hill and Dale - First Water": HILL_AND_DALE | 4,
            "Hill and Dale - Greenery 25%": HILL_AND_DALE | 5,
            "Hill and Dale - Greenery 50%": HILL_AND_DALE | 6,
            "Hill and Dale - Greenery 75%": HILL_AND_DALE | 7,
            "Hill and Dale - Greenery 100%": HILL_AND_DALE | 8,
        },
        {
            "Hill and Dale - First Fynbos": HILL_AND_DALE | 10,
            "Hill and Dale - First Wetlands": HILL_AND_DALE | 11,
            "Hill and Dale - First Forest": HILL_AND_DALE | 12,
            "Hill and Dale - First Fire": HILL_AND_DALE | 13,
            "Hill and Dale - Fynbos Completed": HILL_AND_DALE | 14,
            "Hill and Dale - Wetlands Completed": HILL_AND_DALE | 15,
            "Hill and Dale - Forest Completed": HILL_AND_DALE | 16,
            "Hill and Dale - First Rocky Scrublands": HILL_AND_DALE | 17,
            "Hill and Dale - Rocky Scrublands Completed": HILL_AND_DALE | 18,
        },
        {
            "Hill and Dale - First Recycling": HILL_AND_DALE | 20,
            "Hill and Dale - Recycling Completed": HILL_AND_DALE | 21,
            "Hill and Dale - 3 Photo Stars": HILL_AND_DALE | 22,
            "Hill and Dale - 10 Photo Stars": HILL_AND_DALE | 23,
            "Hill and Dale - Bronze Photo": HILL_AND_DALE | 100,
            "Hill and Dale - Silver Photo": HILL_AND_DALE | 101,
            "Hill and Dale - Gold Photo": HILL_AND_DALE | 102,
        },
        {
            "Hill and Dale - Wildflower Bloom": HILL_AND_DALE | 30,
            "Hill and Dale - Migratory Birds Return": HILL_AND_DALE | 31,
            "Hill and Dale - Fungi In Forests": HILL_AND_DALE | 32,
            "Hill and Dale - Ferns On Riverbanks": HILL_AND_DALE | 33,
            "Hill and Dale - Waterlilies Blossom": HILL_AND_DALE | 34,
            "Hill and Dale - Salmon Run": HILL_AND_DALE | 35,
            "Hill and Dale - Rains Begin": HILL_AND_DALE | 36,
        },
    ],
    "Desolate Island": [
        {
            "Desolate Island - First Energy": DESOLATE_ISLAND | 1,
            "Desolate Island - First Pollution Removed": DESOLATE_ISLAND | 2,
            "Desolate Island - First Greenery": DESOLATE_ISLAND | 3,
            "Desolate Island - First River": DESOLATE_ISLAND | 4,
            "Desolate Island - Greenery 25%": DESOLATE_ISLAND | 5,
            "Desolate Island - Greenery 50%": DESOLATE_ISLAND | 6,
            "Desolate Island - Greenery 75%": DESOLATE_ISLAND | 7,
            "Desolate Island - Greenery 100%": DESOLATE_ISLAND | 8,
        },
        {
            "Desolate Island - First Beach": DESOLATE_ISLAND | 10,
            "Desolate Island - First Mangrove": DESOLATE_ISLAND | 11,
            "Desolate Island - First Tropical Forest": DESOLATE_ISLAND | 12,
            "Desolate Island - First Coral Reef": DESOLATE_ISLAND | 13,
            "Desolate Island - Beach Completed": DESOLATE_ISLAND | 14,
            "Desolate Island - Mangrove Completed": DESOLATE_ISLAND | 15,
            "Desolate Island - Tropical Forest Completed": DESOLATE_ISLAND | 16,
            "Desolate Island - Coral Reef Completed": DESOLATE_ISLAND | 17,
        },
        {
            "Desolate Island - First Recycling": DESOLATE_ISLAND | 18,
            "Desolate Island - Recycling Completed": DESOLATE_ISLAND | 19,
            "Desolate Island - 3 Photo Stars": DESOLATE_ISLAND | 20,
            "Desolate Island - 10 Photo Stars": DESOLATE_ISLAND | 21,
            "Desolate Island - Bronze Photo": DESOLATE_ISLAND | 100,
            "Desolate Island - Silver Photo": DESOLATE_ISLAND | 101,
            "Desolate Island - Gold Photo": DESOLATE_ISLAND | 102,
        },
        {
            "Desolate Island - Moss On Rock Faces": DESOLATE_ISLAND | 26,
            "Desolate Island - Migratory Birds Return": DESOLATE_ISLAND | 27,
            "Desolate Island - Crabs Populate Beaches": DESOLATE_ISLAND | 28,
            "Desolate Island - Coconut Palms": DESOLATE_ISLAND | 29,
            "Desolate Island - Dragonflies": DESOLATE_ISLAND | 30,
            "Desolate Island - Jellyfish Return": DESOLATE_ISLAND | 31,
            "Desolate Island - Ferns On Riverbanks": DESOLATE_ISLAND | 32,
            "Desolate Island - Ivy Overgrowth": DESOLATE_ISLAND | 33,
            "Desolate Island - Vines Grow": DESOLATE_ISLAND | 34,
            "Desolate Island - Waterlilies Blossom": DESOLATE_ISLAND | 35,
            "Desolate Island - Thunderstorms Begin": DESOLATE_ISLAND | 36,
        },
    ],
    "Scorched Caldera": [
        {
            "Scorched Caldera - First Energy": SCORCHED_CALDERA | 1,
            "Scorched Caldera - First Pollution Removed": SCORCHED_CALDERA | 2,
            "Scorched Caldera - First Greenery": SCORCHED_CALDERA | 3,
            "Scorched Caldera - Greenery 25%": SCORCHED_CALDERA | 4,
            "Scorched Caldera - Greenery 50%": SCORCHED_CALDERA | 5,
            "Scorched Caldera - Greenery 75%": SCORCHED_CALDERA | 6,
            "Scorched Caldera - Greenery 100%": SCORCHED_CALDERA | 7,
        },
        {
            "Scorched Caldera - First Water": SCORCHED_CALDERA | 10,
            "Scorched Caldera - First Lake Vegetation": SCORCHED_CALDERA | 11,
            "Scorched Caldera - First Bamboo": SCORCHED_CALDERA | 12,
            "Scorched Caldera - First Tropical Forest": SCORCHED_CALDERA | 13,
            "Scorched Caldera - Lake Vegetation Completed": SCORCHED_CALDERA | 14,
            "Scorched Caldera - Bamboo Completed": SCORCHED_CALDERA | 15,
            "Scorched Caldera - Tropical Forest Completed": SCORCHED_CALDERA | 16,
        },
        {
            "Scorched Caldera - First Recycling": SCORCHED_CALDERA | 20,
            "Scorched Caldera - Recycling Completed": SCORCHED_CALDERA | 21,
            "Scorched Caldera - 3 Photo Stars": SCORCHED_CALDERA | 22,
            "Scorched Caldera - 10 Photo Stars": SCORCHED_CALDERA | 23,
            "Scorched Caldera - Bronze Photo": SCORCHED_CALDERA | 100,
            "Scorched Caldera - Silver Photo": SCORCHED_CALDERA | 101,
            "Scorched Caldera - Gold Photo": SCORCHED_CALDERA | 102,
        },
        {
            "Scorched Caldera - Ivy Overgrowth": SCORCHED_CALDERA | 30,
            "Scorched Caldera - Migratory Birds Return": SCORCHED_CALDERA | 31,
            "Scorched Caldera - Ferns On Riverbanks": SCORCHED_CALDERA | 32,
            "Scorched Caldera - Vines Grow": SCORCHED_CALDERA | 33,
            "Scorched Caldera - Waterlilies Blossom": SCORCHED_CALDERA | 34,
            "Scorched Caldera - Dragonflies": SCORCHED_CALDERA | 35,
            "Scorched Caldera - Cloud Forests": SCORCHED_CALDERA | 36,
            "Scorched Caldera - Moss On Rock Faces": SCORCHED_CALDERA | 37,
            "Scorched Caldera - Thunderstorms Begin": SCORCHED_CALDERA | 38,
        },
    ],
    "Volcanic Glacier": [
        {
            "Volcanic Glacier - First Energy": VOLCANIC_GLACIER | 1,
            "Volcanic Glacier - First Lava": VOLCANIC_GLACIER | 2,
            "Volcanic Glacier - First Greenery": VOLCANIC_GLACIER | 3,
            "Volcanic Glacier - Greenery 25%": VOLCANIC_GLACIER | 4,
            "Volcanic Glacier - Greenery 50%": VOLCANIC_GLACIER | 5,
            "Volcanic Glacier - Greenery 75%": VOLCANIC_GLACIER | 6,
            "Volcanic Glacier - Greenery 100%": VOLCANIC_GLACIER | 7,
        },
        {
            "Volcanic Glacier - First Fire": VOLCANIC_GLACIER | 10,
            "Volcanic Glacier - First Tundra": VOLCANIC_GLACIER | 11,
            "Volcanic Glacier - First Forest": VOLCANIC_GLACIER | 12,
            "Volcanic Glacier - First Lichen": VOLCANIC_GLACIER | 13,
            "Volcanic Glacier - First Kelp Forest": VOLCANIC_GLACIER | 14,
            "Volcanic Glacier - Tundra Completed": VOLCANIC_GLACIER | 15,
            "Volcanic Glacier - Forest Completed": VOLCANIC_GLACIER | 16,
            "Volcanic Glacier - Lichen Completed": VOLCANIC_GLACIER | 17,
            "Volcanic Glacier - Kelp Forest Completed": VOLCANIC_GLACIER | 18,
        },
        {
            "Volcanic Glacier - First Recycling": VOLCANIC_GLACIER | 20,
            "Volcanic Glacier - Recycling Completed": VOLCANIC_GLACIER | 21,
            "Volcanic Glacier - 3 Photo Stars": VOLCANIC_GLACIER | 22,
            "Volcanic Glacier - 10 Photo Stars": VOLCANIC_GLACIER | 23,
            "Volcanic Glacier - Bronze Photo": VOLCANIC_GLACIER | 100,
            "Volcanic Glacier - Silver Photo": VOLCANIC_GLACIER | 101,
            "Volcanic Glacier - Gold Photo": VOLCANIC_GLACIER | 102,
        },
        {
            "Volcanic Glacier - Snow Melts": VOLCANIC_GLACIER | 30,
            "Volcanic Glacier - Fungi In Forests": VOLCANIC_GLACIER | 31,
            "Volcanic Glacier - Icebergs Form": VOLCANIC_GLACIER | 32,
            "Volcanic Glacier - Moss On Boulders": VOLCANIC_GLACIER | 33,
            "Volcanic Glacier - Ivy Overgrowth": VOLCANIC_GLACIER | 34,
            "Volcanic Glacier - Butterflies": VOLCANIC_GLACIER | 35,
            "Volcanic Glacier - Migratory Birds Return": VOLCANIC_GLACIER | 36,
            "Volcanic Glacier - Moss On Rock Faces": VOLCANIC_GLACIER | 37,
            "Volcanic Glacier - Pelagic Fish": VOLCANIC_GLACIER | 38,
            "Volcanic Glacier - Snowfall Begins": VOLCANIC_GLACIER | 39,
            "Volcanic Glacier - Aurora": VOLCANIC_GLACIER | 40,
        },
    ]
}

LOCATION_NAME_TO_ID = {}
for level in locations:
    for tier in locations[level]:
        for name in tier:
            LOCATION_NAME_TO_ID[name] = tier[name]

class TerraNilLocation(Location):
    game = "TerraNil"

def create_all_locations(world: TerraNilWorld) -> None:
    for level in locations:
        world.get_region(f"{level} Tier 1").add_locations(locations[level][0], TerraNilLocation)
        world.get_region(f"{level} Tier 2").add_locations(locations[level][1], TerraNilLocation)
        world.get_region(f"{level} Tier 3").add_locations(locations[level][2], TerraNilLocation)

        if world.options.climate_goals:
            world.get_region(f"{level} Climate Goals").add_locations(locations[level][3], TerraNilLocation)

    create_events(world)

def create_events(world: TerraNilWorld) -> None:
    for level in locations:
        t1 = world.get_region(f"{level} Tier 1")
        t2 = world.get_region(f"{level} Tier 2")
        t3 = world.get_region(f"{level} Tier 3")
        t1.add_event(
            f"{level} - Tier 1 Completed",
            f"{level} - Tier 1 Completed",
            location_type=TerraNilLocation,
            item_type=items.TerraNilItem
        )
        t2.add_event(
            f"{level} - Tier 2 Completed",
            f"{level} - Tier 2 Completed",
            location_type=TerraNilLocation,
            item_type=items.TerraNilItem
        )
        t3.add_event(
            f"{level} - Liftoff",
            f"{level} - Liftoff",
            location_type=TerraNilLocation,
            item_type=items.TerraNilItem
        )
