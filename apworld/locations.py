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
            "First Energy (River Valley)": RIVER_VALLEY | 1,
            "First Pollution Removed (River Valley)": RIVER_VALLEY | 2,
            "First Greenery (River Valley)": RIVER_VALLEY | 3,
            "First Water (River Valley)": RIVER_VALLEY | 4,
            "Greenery 25% (River Valley)": RIVER_VALLEY | 5,
            "Greenery 50% (River Valley)": RIVER_VALLEY | 6,
            "Greenery 75% (River Valley)": RIVER_VALLEY | 7,
            "Greenery 100% (River Valley)": RIVER_VALLEY | 8,
        },
        {
            "First Fynbos (River Valley)": RIVER_VALLEY | 10,
            "First Wetlands (River Valley)": RIVER_VALLEY | 11,
            "First Forest (River Valley)": RIVER_VALLEY | 12,
            "First Fire (River Valley)": RIVER_VALLEY | 13,
            "Fynbos Completed (River Valley)": RIVER_VALLEY | 14,
            "Wetlands Completed (River Valley)": RIVER_VALLEY | 15,
            "Forest Completed (River Valley)": RIVER_VALLEY | 16,
        },
        {
            "First Recycling (River Valley)": RIVER_VALLEY | 18,
            "Recycling Completed (River Valley)": RIVER_VALLEY | 19,
            "3 Photo Stars (River Valley)": RIVER_VALLEY | 20,
            "10 Photo Stars (River Valley)": RIVER_VALLEY | 21,
            "Bronze Photo (River Valley)": RIVER_VALLEY | 100,
            "Silver Photo (River Valley)": RIVER_VALLEY | 101,
            "Gold Photo (River Valley)": RIVER_VALLEY | 102,
        },
        {
            "Waterlillies Blossom (River Valley)": RIVER_VALLEY | 26,
            "Migratory Birds Return (River Valley)": RIVER_VALLEY | 27,
            "Ferns On Riverbanks (River Valley)": RIVER_VALLEY | 28,
            "Fungi In Forests (River Valley)": RIVER_VALLEY | 29,
            "Rains Begin (River Valley)": RIVER_VALLEY | 30,
            "Wildflower Blooms (River Valley)": RIVER_VALLEY | 31,
            "Salmon Run (River Valley)": RIVER_VALLEY | 32,
        },
    ],
    "Abandoned Quarry": [
        {
            "First Energy (Abandoned Quarry)": ABANDONED_QUARRY | 1,
            "First Lava (Abandoned Quarry)": ABANDONED_QUARRY | 2,
            "First Water (Abandoned Quarry)": ABANDONED_QUARRY | 3,
            "First Pollution Removed (Abandoned Quarry)": ABANDONED_QUARRY | 4,
            "First Greenery (Abandoned Quarry)": ABANDONED_QUARRY | 5,
            "Greenery 25% (Abandoned Quarry)": ABANDONED_QUARRY | 6,
            "Greenery 50% (Abandoned Quarry)": ABANDONED_QUARRY | 7,
            "Greenery 75% (Abandoned Quarry)": ABANDONED_QUARRY | 8,
            "Greenery 100% (Abandoned Quarry)": ABANDONED_QUARRY | 9,
        },
        {
            "First Fynbos (Abandoned Quarry)": ABANDONED_QUARRY | 10,
            "First Wetlands (Abandoned Quarry)": ABANDONED_QUARRY | 11,
            "First Forest (Abandoned Quarry)": ABANDONED_QUARRY | 12,
            "First Fire (Abandoned Quarry)": ABANDONED_QUARRY | 13,
            "Fynbos Completed (Abandoned Quarry)": ABANDONED_QUARRY | 14,
            "Wetlands Completed (Abandoned Quarry)": ABANDONED_QUARRY | 15,
            "Forest Completed (Abandoned Quarry)": ABANDONED_QUARRY | 16,
        },
        {
            "First Recycling (Abandoned Quarry)": ABANDONED_QUARRY | 20,
            "Recycling Completed (Abandoned Quarry)": ABANDONED_QUARRY | 21,
            "3 Photo Stars (Abandoned Quarry)": ABANDONED_QUARRY | 22,
            "10 Photo Stars (Abandoned Quarry)": ABANDONED_QUARRY | 23,
            "Bronze Photo (Abandoned Quarry)": ABANDONED_QUARRY | 100,
            "Silver Photo (Abandoned Quarry)": ABANDONED_QUARRY | 101,
            "Gold Photo (Abandoned Quarry)": ABANDONED_QUARRY | 102,
        },
        {
            "Wildflower Bloom (Abandoned Quarry)": ABANDONED_QUARRY | 30,
            "Migratory Birds Return (Abandoned Quarry)": ABANDONED_QUARRY | 31,
            "Fungi In Forests (Abandoned Quarry)": ABANDONED_QUARRY | 32,
            "Ferns On Riverbanks (Abandoned Quarry)": ABANDONED_QUARRY | 33,
            "Waterlilies Blossom (Abandoned Quarry)": ABANDONED_QUARRY | 34,
            "Salmon Run (Abandoned Quarry)": ABANDONED_QUARRY | 35,
            "Rains Begin (Abandoned Quarry)": ABANDONED_QUARRY | 36,
        },
    ],
    "Polluted Bay": [
        {
            "First Energy (Polluted Bay)": POLLUTED_BAY | 1,
            "First Pollution Removed (Polluted Bay)": POLLUTED_BAY | 2,
            "First Greenery (Polluted Bay)": POLLUTED_BAY | 3,
            "First Water (Polluted Bay)": POLLUTED_BAY | 4,
            "Greenery 25% (Polluted Bay)": POLLUTED_BAY | 5,
            "Greenery 50% (Polluted Bay)": POLLUTED_BAY | 6,
            "Greenery 75% (Polluted Bay)": POLLUTED_BAY | 7,
            "Greenery 100% (Polluted Bay)": POLLUTED_BAY | 8,
        },
        {
            "First Fynbos (Polluted Bay)": POLLUTED_BAY | 10,
            "First Wetlands (Polluted Bay)": POLLUTED_BAY | 11,
            "First Forest (Polluted Bay)": POLLUTED_BAY | 12,
            "First Fire (Polluted Bay)": POLLUTED_BAY | 13,
            "Fynbos Completed (Polluted Bay)": POLLUTED_BAY | 14,
            "Wetlands Completed (Polluted Bay)": POLLUTED_BAY | 15,
            "Forest Completed (Polluted Bay)": POLLUTED_BAY | 16,
            "First Deciduous Forest (Polluted Bay)": POLLUTED_BAY | 17,
            "Deciduous Forest Completed (Polluted Bay)": POLLUTED_BAY | 18,
        },
        {
            "First Recycling (Polluted Bay)": POLLUTED_BAY | 20,
            "Recycling Completed (Polluted Bay)": POLLUTED_BAY | 21,
            "3 Photo Stars (Polluted Bay)": POLLUTED_BAY | 22,
            "10 Photo Stars (Polluted Bay)": POLLUTED_BAY | 23,
            "Bronze Photo (Polluted Bay)": POLLUTED_BAY | 100,
            "Silver Photo (Polluted Bay)": POLLUTED_BAY | 101,
            "Gold Photo (Polluted Bay)": POLLUTED_BAY | 102,
        },
        {
            "Wildflower Bloom (Polluted Bay)": POLLUTED_BAY | 30,
            "Migratory Birds Return (Polluted Bay)": POLLUTED_BAY | 31,
            "Fungi In Forests (Polluted Bay)": POLLUTED_BAY | 32,
            "Ferns On Riverbanks (Polluted Bay)": POLLUTED_BAY | 33,
            "Cliff Foliage (Polluted Bay)": POLLUTED_BAY | 34,
            "Waterlilies Blossom (Polluted Bay)": POLLUTED_BAY | 35,
            "Salmon Run (Polluted Bay)": POLLUTED_BAY | 36,
            "Vegetation Boom (Polluted Bay)": POLLUTED_BAY | 37,
            "Rains Begin (Polluted Bay)": POLLUTED_BAY | 38,
        },
    ],
    "Hill and Dale": [
        {
            "First Energy (Hill and Dale)": HILL_AND_DALE | 1,
            "First Pollution Removed (Hill and Dale)": HILL_AND_DALE | 2,
            "First Greenery (Hill and Dale)": HILL_AND_DALE | 3,
            "First Water (Hill and Dale)": HILL_AND_DALE | 4,
            "Greenery 25% (Hill and Dale)": HILL_AND_DALE | 5,
            "Greenery 50% (Hill and Dale)": HILL_AND_DALE | 6,
            "Greenery 75% (Hill and Dale)": HILL_AND_DALE | 7,
            "Greenery 100% (Hill and Dale)": HILL_AND_DALE | 8,
        },
        {
            "First Fynbos (Hill and Dale)": HILL_AND_DALE | 10,
            "First Wetlands (Hill and Dale)": HILL_AND_DALE | 11,
            "First Forest (Hill and Dale)": HILL_AND_DALE | 12,
            "First Fire (Hill and Dale)": HILL_AND_DALE | 13,
            "Fynbos Completed (Hill and Dale)": HILL_AND_DALE | 14,
            "Wetlands Completed (Hill and Dale)": HILL_AND_DALE | 15,
            "Forest Completed (Hill and Dale)": HILL_AND_DALE | 16,
            "First Rocky Scrublands (Hill and Dale)": HILL_AND_DALE | 17,
            "Rocky Scrublands Completed (Hill and Dale)": HILL_AND_DALE | 18,
        },
        {
            "First Recycling (Hill and Dale)": HILL_AND_DALE | 20,
            "Recycling Completed (Hill and Dale)": HILL_AND_DALE | 21,
            "3 Photo Stars (Hill and Dale)": HILL_AND_DALE | 22,
            "10 Photo Stars (Hill and Dale)": HILL_AND_DALE | 23,
            "Bronze Photo (Hill and Dale)": HILL_AND_DALE | 100,
            "Silver Photo (Hill and Dale)": HILL_AND_DALE | 101,
            "Gold Photo (Hill and Dale)": HILL_AND_DALE | 102,
        },
        {
            "Wildflower Bloom (Hill and Dale)": HILL_AND_DALE | 30,
            "Migratory Birds Return (Hill and Dale)": HILL_AND_DALE | 31,
            "Fungi In Forests (Hill and Dale)": HILL_AND_DALE | 32,
            "Ferns On Riverbanks (Hill and Dale)": HILL_AND_DALE | 33,
            "Waterlilies Blossom (Hill and Dale)": HILL_AND_DALE | 34,
            "Salmon Run (Hill and Dale)": HILL_AND_DALE | 35,
            "Rains Begin (Hill and Dale)": HILL_AND_DALE | 36,
        },
    ],
    "Desolate Island": [
        {
            "First Energy (Desolate Island)": DESOLATE_ISLAND | 1,
            "First Pollution Removed (Desolate Island)": DESOLATE_ISLAND | 2,
            "First Greenery (Desolate Island)": DESOLATE_ISLAND | 3,
            "First River (Desolate Island)": DESOLATE_ISLAND | 4,
            "Greenery 25% (Desolate Island)": DESOLATE_ISLAND | 5,
            "Greenery 50% (Desolate Island)": DESOLATE_ISLAND | 6,
            "Greenery 75% (Desolate Island)": DESOLATE_ISLAND | 7,
            "Greenery 100% (Desolate Island)": DESOLATE_ISLAND | 8,
        },
        {
            "First Beach (Desolate Island)": DESOLATE_ISLAND | 10,
            "First Mangrove (Desolate Island)": DESOLATE_ISLAND | 11,
            "First Tropical Forest (Desolate Island)": DESOLATE_ISLAND | 12,
            "First Coral Reef (Desolate Island)": DESOLATE_ISLAND | 13,
            "Beach Completed (Desolate Island)": DESOLATE_ISLAND | 14,
            "Mangrove Completed (Desolate Island)": DESOLATE_ISLAND | 15,
            "Tropical Forest Completed (Desolate Island)": DESOLATE_ISLAND | 16,
            "Coral Reef Completed (Desolate Island)": DESOLATE_ISLAND | 17,
        },
        {
            "First Recycling (Desolate Island)": DESOLATE_ISLAND | 18,
            "Recycling Completed (Desolate Island)": DESOLATE_ISLAND | 19,
            "3 Photo Stars (Desolate Island)": DESOLATE_ISLAND | 20,
            "10 Photo Stars (Desolate Island)": DESOLATE_ISLAND | 21,
            "Bronze Photo (Desolate Island)": DESOLATE_ISLAND | 100,
            "Silver Photo (Desolate Island)": DESOLATE_ISLAND | 101,
            "Gold Photo (Desolate Island)": DESOLATE_ISLAND | 102,
        },
        {
            "Moss On Rock Faces (Desolate Island)": DESOLATE_ISLAND | 26,
            "Migratory Birds Return (Desolate Island)": DESOLATE_ISLAND | 27,
            "Crabs Populate Beaches (Desolate Island)": DESOLATE_ISLAND | 28,
            "Coconut Palms (Desolate Island)": DESOLATE_ISLAND | 29,
            "Dragonflies (Desolate Island)": DESOLATE_ISLAND | 30,
            "Jellyfish Return (Desolate Island)": DESOLATE_ISLAND | 31,
            "Ferns On Riverbanks (Desolate Island)": DESOLATE_ISLAND | 32,
            "Ivy Overgrowth (Desolate Island)": DESOLATE_ISLAND | 33,
            "Vines Grow (Desolate Island)": DESOLATE_ISLAND | 34,
            "Waterlilies Blossom (Desolate Island)": DESOLATE_ISLAND | 35,
            "Thunderstorms Begin (Desolate Island)": DESOLATE_ISLAND | 36,
        },
    ],
    "Scorched Caldera": [
        {
            "First Energy (Scorched Caldera)": SCORCHED_CALDERA | 1,
            "First Pollution Removed (Scorched Caldera)": SCORCHED_CALDERA | 2,
            "First Greenery (Scorched Caldera)": SCORCHED_CALDERA | 3,
            "Greenery 25% (Scorched Caldera)": SCORCHED_CALDERA | 4,
            "Greenery 50% (Scorched Caldera)": SCORCHED_CALDERA | 5,
            "Greenery 75% (Scorched Caldera)": SCORCHED_CALDERA | 6,
            "Greenery 100% (Scorched Caldera)": SCORCHED_CALDERA | 7,
        },
        {
            "First Water (Scorched Caldera)": SCORCHED_CALDERA | 10,
            "First Lake Vegetation (Scorched Caldera)": SCORCHED_CALDERA | 11,
            "First Bamboo (Scorched Caldera)": SCORCHED_CALDERA | 12,
            "First Tropical Forest (Scorched Caldera)": SCORCHED_CALDERA | 13,
            "Lake Vegetation Completed (Scorched Caldera)": SCORCHED_CALDERA | 14,
            "Bamboo Completed (Scorched Caldera)": SCORCHED_CALDERA | 15,
            "Tropical Forest Completed (Scorched Caldera)": SCORCHED_CALDERA | 16,
        },
        {
            "First Recycling (Scorched Caldera)": SCORCHED_CALDERA | 20,
            "Recycling Completed (Scorched Caldera)": SCORCHED_CALDERA | 21,
            "3 Photo Stars (Scorched Caldera)": SCORCHED_CALDERA | 22,
            "10 Photo Stars (Scorched Caldera)": SCORCHED_CALDERA | 23,
            "Bronze Photo (Scorched Caldera)": SCORCHED_CALDERA | 100,
            "Silver Photo (Scorched Caldera)": SCORCHED_CALDERA | 101,
            "Gold Photo (Scorched Caldera)": SCORCHED_CALDERA | 102,
        },
        {
            "Ivy Overgrowth (Scorched Caldera)": SCORCHED_CALDERA | 30,
            "Migratory Birds Return (Scorched Caldera)": SCORCHED_CALDERA | 31,
            "Ferns On Riverbanks (Scorched Caldera)": SCORCHED_CALDERA | 32,
            "Vines Grow (Scorched Caldera)": SCORCHED_CALDERA | 33,
            "Waterlilies Blossom (Scorched Caldera)": SCORCHED_CALDERA | 34,
            "Dragonflies (Scorched Caldera)": SCORCHED_CALDERA | 35,
            "Cloud Forests (Scorched Caldera)": SCORCHED_CALDERA | 36,
            "Moss On Rock Faces (Scorched Caldera)": SCORCHED_CALDERA | 37,
            "Thunderstorms Begin (Scorched Caldera)": SCORCHED_CALDERA | 38,
        },
    ],
    "Volcanic Glacier": [
        {
            "First Energy (Volcanic Glacier)": VOLCANIC_GLACIER | 1,
            "First Lava (Volcanic Glacier)": VOLCANIC_GLACIER | 2,
            "First Greenery (Volcanic Glacier)": VOLCANIC_GLACIER | 3,
            "Greenery 25% (Volcanic Glacier)": VOLCANIC_GLACIER | 4,
            "Greenery 50% (Volcanic Glacier)": VOLCANIC_GLACIER | 5,
            "Greenery 75% (Volcanic Glacier)": VOLCANIC_GLACIER | 6,
            "Greenery 100% (Volcanic Glacier)": VOLCANIC_GLACIER | 7,
        },
        {
            "First Fire (Volcanic Glacier)": VOLCANIC_GLACIER | 10,
            "First Tundra (Volcanic Glacier)": VOLCANIC_GLACIER | 11,
            "First Forest (Volcanic Glacier)": VOLCANIC_GLACIER | 12,
            "First Lichen (Volcanic Glacier)": VOLCANIC_GLACIER | 13,
            "First Kelp Forest (Volcanic Glacier)": VOLCANIC_GLACIER | 14,
            "Tundra Completed (Volcanic Glacier)": VOLCANIC_GLACIER | 15,
            "Forest Completed (Volcanic Glacier)": VOLCANIC_GLACIER | 16,
            "Lichen Completed (Volcanic Glacier)": VOLCANIC_GLACIER | 17,
            "Kelp Forest Completed (Volcanic Glacier)": VOLCANIC_GLACIER | 18,
        },
        {
            "First Recycling (Volcanic Glacier)": VOLCANIC_GLACIER | 20,
            "Recycling Completed (Volcanic Glacier)": VOLCANIC_GLACIER | 21,
            "3 Photo Stars (Volcanic Glacier)": VOLCANIC_GLACIER | 22,
            "10 Photo Stars (Volcanic Glacier)": VOLCANIC_GLACIER | 23,
            "Bronze Photo (Volcanic Glacier)": VOLCANIC_GLACIER | 100,
            "Silver Photo (Volcanic Glacier)": VOLCANIC_GLACIER | 101,
            "Gold Photo (Volcanic Glacier)": VOLCANIC_GLACIER | 102,
        },
        {
            "Snow Melts (Volcanic Glacier)": VOLCANIC_GLACIER | 30,
            "Fungi In Forests (Volcanic Glacier)": VOLCANIC_GLACIER | 31,
            "Icebergs Form (Volcanic Glacier)": VOLCANIC_GLACIER | 32,
            "Moss On Boulders (Volcanic Glacier)": VOLCANIC_GLACIER | 33,
            "Ivy Overgrowth (Volcanic Glacier)": VOLCANIC_GLACIER | 34,
            "Butterflies (Volcanic Glacier)": VOLCANIC_GLACIER | 35,
            "Migratory Birds Return (Volcanic Glacier)": VOLCANIC_GLACIER | 36,
            "Moss On Rock Faces (Volcanic Glacier)": VOLCANIC_GLACIER | 37,
            "Pelagic Fish (Volcanic Glacier)": VOLCANIC_GLACIER | 38,
            "Snowfall Begins (Volcanic Glacier)": VOLCANIC_GLACIER | 39,
            "Aurora (Volcanic Glacier)": VOLCANIC_GLACIER | 40,
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
            f"Tier 1 Completed ({level})",
            f"Tier 1 Completed ({level})",
            location_type=TerraNilLocation,
            item_type=items.TerraNilItem
        )
        t2.add_event(
            f"Tier 2 Completed ({level})",
            f"Tier 2 Completed ({level})",
            location_type=TerraNilLocation,
            item_type=items.TerraNilItem
        )
        t3.add_event(
            f"Liftoff ({level})",
            f"Liftoff ({level})",
            location_type=TerraNilLocation,
            item_type=items.TerraNilItem
        )
