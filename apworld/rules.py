from __future__ import annotations
from typing import TYPE_CHECKING
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule
if TYPE_CHECKING:
    from .world import TerraNilWorld

def set_all_rules(world: TerraNilWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: TerraNilWorld) -> None:
    rivervalley_t1_to_t2 = world.get_entrance("River Valley Tier 1 to River Valley Tier 2")
    world.set_rule(rivervalley_t1_to_t2, Has("Tier 1 Completed (River Valley)"))

    rivervalley_t2_to_t3 = world.get_entrance("River Valley Tier 2 to River Valley Tier 3")
    world.set_rule(rivervalley_t2_to_t3, Has("Tier 2 Completed (River Valley)"))

    rivervalley_complete = world.get_entrance("River Valley Tier 3 to World Map")
    world.set_rule(rivervalley_complete, Has("Liftoff (River Valley)"))

    if world.options.climate_goals:
        rivervalley_climate = world.get_entrance("River Valley Tier 2 to River Valley Climate Goals")
        world.set_rule(rivervalley_climate, Has("Research Center (River Valley)"))

def set_all_location_rules(world: TerraNilWorld) -> None:
    tier1 = Has("Tier 1 Completed (River Valley)")
    tier2 = Has("Tier 2 Completed (River Valley)")

    energy = Has("Wind Turbine (River Valley)")
    world.set_rule(world.get_location("First Energy (River Valley)"), energy)

    world.set_rule(
        world.get_location("First Pollution Removed (River Valley)"),
        energy & Has("Toxin Scrubber (River Valley)")
    )

    world.set_rule(
        world.get_location("First Greenery (River Valley)"),
        energy & (
            HasAll("Toxin Scrubber (River Valley)", "Irrigator (River Valley)") |
            Has("Water Pump (River Valley)")
        )
    )

    water = energy & Has("Water Pump (River Valley)")
    if world.options.rain_logic:
        water = energy & (
            Has("Water Pump (River Valley)") |
            (tier1 & HasAll("Research Center (River Valley)", "Toxin Scrubber (River Valley)", "Irrigator (River Valley)"))
        )

    world.set_rule(world.get_location("First Water (River Valley)"), water)

    greenery = energy & HasAll("Toxin Scrubber (River Valley)", "Irrigator (River Valley)")
    world.set_rule(world.get_location("Greenery 25% (River Valley)"), greenery)
    world.set_rule(world.get_location("Greenery 50% (River Valley)"), greenery)
    world.set_rule(world.get_location("Greenery 75% (River Valley)"), greenery)
    world.set_rule(world.get_location("Greenery 100% (River Valley)"), greenery)
    world.set_rule(world.get_location("Tier 1 Completed (River Valley)"), greenery)

    fynbos = tier1 & Has("Beehive (River Valley)")
    world.set_rule(world.get_location("First Fynbos (River Valley)"), fynbos)
    world.set_rule(world.get_location("Fynbos Completed (River Valley)"), fynbos)

    wetlands = tier1 & water & Has("Hydroponium (River Valley)")
    world.set_rule(world.get_location("First Wetlands (River Valley)"), wetlands)
    world.set_rule(world.get_location("Wetlands Completed (River Valley)"), wetlands)

    fire = tier1 & HasAll("Beehive (River Valley)", "Solar Amplifier (River Valley)")
    world.set_rule(world.get_location("First Fire (River Valley)"), fire)

    forest = fire & Has("Arboretum (River Valley)")
    world.set_rule(world.get_location("First Forest (River Valley)"), forest)
    world.set_rule(world.get_location("Forest Completed (River Valley)"), forest)

    world.set_rule(world.get_location("Tier 2 Completed (River Valley)"), fynbos & wetlands & forest)

    photos = tier2 & HasAll("Animal Observatory (River Valley)", "Wildlife Bridge (River Valley)", "Sonic Pulse (River Valley)")
    world.set_rule(world.get_location("3 Photo Stars (River Valley)"), photos)
    world.set_rule(world.get_location("10 Photo Stars (River Valley)"), photos)
    world.set_rule(world.get_location("Bronze Photo (River Valley)"), photos)
    world.set_rule(world.get_location("Silver Photo (River Valley)"), photos)
    world.set_rule(world.get_location("Gold Photo (River Valley)"), photos)

    recyclingbase = tier2 & HasAll("Airship (River Valley)", "Recycling Drone (River Valley)", "Loading Dock (River Valley)")
    recyclingfull = recyclingbase & HasAll(
        "Recycling Silo (River Valley)",
        "Pound Lock (River Valley)",
        "Water Pump (River Valley)",
        "Excavator (River Valley)",
    )

    world.set_rule(world.get_location("First Recycling (River Valley)"), recyclingbase)
    world.set_rule(world.get_location("Recycling Completed (River Valley)"), recyclingfull)

    world.set_rule(world.get_location("Liftoff (River Valley)"), photos & recyclingfull)

    if world.options.climate_goals:
        climategoals = tier1 & Has("Research Center (River Valley)")

        if not world.options.rain_logic:
            climategoals = climategoals & water & Has("Cloud Seeder (River Valley)")

        for goal in [
            "Waterlillies Blossom (River Valley)",
            "Migratory Birds Return (River Valley)",
            "Fungi In Forests (River Valley)",
        ]:
            world.set_rule(world.get_location(goal), climategoals)

        for goal in [
            "Ferns On Riverbanks (River Valley)",
            "Rains Begin (River Valley)",
            "Wildflower Blooms (River Valley)",
            "Salmon Run (River Valley)",
        ]:
            world.set_rule(world.get_location(goal), climategoals & tier2 & Has("Recycling Silo (River Valley)"))

def set_completion_condition(world: TerraNilWorld) -> None:
    world.set_completion_rule(Has("Liftoff (River Valley)"))
