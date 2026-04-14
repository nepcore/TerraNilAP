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
    rivervalleyt1 = Region("River Valley Tier 1", world.player, world.multiworld)
    rivervalleyt2 = Region("River Valley Tier 2", world.player, world.multiworld)
    rivervalleyt3 = Region("River Valley Tier 3", world.player, world.multiworld)

    regions = [menu, worldmap, rivervalleyt1, rivervalleyt2, rivervalleyt3]

    if world.options.climate_goals:
        rivervalleyclimate = Region("River Valley Climate Goals", world.player, world.multiworld)
        regions.append(rivervalleyclimate)

    world.multiworld.regions += regions

def connect_regions(world: TerraNilWorld) -> None:
    menu = world.get_region("Menu")
    worldmap = world.get_region("World Map")
    rivervalleyt1 = world.get_region("River Valley Tier 1")
    rivervalleyt2 = world.get_region("River Valley Tier 2")
    rivervalleyt3 = world.get_region("River Valley Tier 3")

    menu.connect(rivervalleyt1, "Menu to River Valley Tier 1")
    rivervalleyt1.connect(rivervalleyt2, "River Valley Tier 1 to River Valley Tier 2")
    rivervalleyt2.connect(rivervalleyt3, "River Valley Tier 2 to River Valley Tier 3")
    rivervalleyt3.connect(worldmap, "River Valley Tier 3 to World Map")
    worldmap.connect(rivervalleyt1, "World Map to River Valley Tier 1")

    if world.options.climate_goals:
        rivervalleyclimate = world.get_region("River Valley Climate Goals")
        rivervalleyt2.connect(rivervalleyclimate, "River Valley Tier 2 to River Valley Climate Goals")
