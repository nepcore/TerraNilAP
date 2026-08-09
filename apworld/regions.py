from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Entrance, Region
if TYPE_CHECKING:
    from.world import TerraNilWorld

def create_and_connect_regions(world: TerraNilWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: TerraNilWorld) -> None:
    menu = Region("Menu", world.player, world.multiworld)
    worldmap = Region("World Map", world.player, world.multiworld)
    world.multiworld.regions += [menu, worldmap]

    for level in world.levels_enabled:
        create_regions_for_level(world, level)

def create_regions_for_level(world: TerraNilWorld, level: str) -> None:
    t1 = Region(f"{level} Tier 1", world.player, world.multiworld)
    t2 = Region(f"{level} Tier 2", world.player, world.multiworld)
    t3 = Region(f"{level} Tier 3", world.player, world.multiworld)
    world.multiworld.regions += [t1, t2, t3]

    if world.options.climate_goals:
        climate = Region(f"{level} Climate Goals", world.player, world.multiworld)
        world.multiworld.regions += [climate]

def connect_regions(world: TerraNilWorld) -> None:
    menu = world.get_region("Menu")
    worldmap = world.get_region("World Map")
    t1 = world.get_region(f"{world.starting_level} Tier 1")
    #t2 = world.get_region(f"{world.starting_level} Tier 2")
    menu.connect(t1, f"Menu to {world.starting_level} Tier 1")
    t1.connect(worldmap, f"{world.starting_level} Tier 1 to World Map")
    #menu.connect(world.get_region("River Valley Tier 1"), "Menu to River Valley Tier 1")

    for level in world.levels_enabled:
        connect_regions_for_level(world, level)

def connect_regions_for_level(world: TerraNilWorld, level: str) -> None:
    worldmap = world.get_region("World Map")
    t1 = world.get_region(f"{level} Tier 1")
    t2 = world.get_region(f"{level} Tier 2")
    t3 = world.get_region(f"{level} Tier 3")

    worldmap.connect(t1, f"World Map to {level} Tier 1")
    t1.connect(t2, f"{level} Tier 1 to {level} Tier 2")
    t2.connect(t3, f"{level} Tier 2 to {level} Tier 3")
    #t3.connect(worldmap, f"{level} Tier 3 to World Map")

    if world.options.climate_goals:
        climate = world.get_region(f"{level} Climate Goals")
        t2.connect(climate, f"{level} Tier 2 to {level} Climate Goals")
