from __future__ import annotations
from typing import TYPE_CHECKING
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, HasFromListUnique, Rule
if TYPE_CHECKING:
    from .world import TerraNilWorld

levels = [
    "River Valley",
    "Abandoned Quarry",
    "Polluted Bay",
    "Hill and Dale",
    "Desolate Island",
    "Scorched Caldera",
    "Volcanic Glacier",
]

def set_all_rules(world: TerraNilWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: TerraNilWorld) -> None:
    for level in levels:
        world.set_rule(world.get_entrance(f"World Map to {level} Tier 1"), Has(f"{level} Unlock"))
        world.set_rule(world.get_entrance(f"{level} Tier 1 to {level} Tier 2"), Has(f"Tier 1 Completed ({level})"))
        world.set_rule(world.get_entrance(f"{level} Tier 2 to {level} Tier 3"), Has(f"Tier 2 Completed ({level})"))
        world.set_rule(world.get_entrance(f"{level} Tier 3 to World Map"), Has(f"Liftoff ({level})"))

    if world.options.climate_goals:
        rivervalley_climate = world.get_entrance("River Valley Tier 2 to River Valley Climate Goals")
        world.set_rule(rivervalley_climate, Has("Research Center (River Valley)"))

def set_all_location_rules(world: TerraNilWorld) -> None:
    set_all_location_rules_river_valley(world)
    set_all_location_rules_abandoned_quarry(world)
    set_all_location_rules_polluted_bay(world)
    set_all_location_rules_hill_and_dale(world)
    set_all_location_rules_desolate_island(world)
    set_all_location_rules_scorched_caldera(world)
    set_all_location_rules_volcanic_glacier(world)

def set_all_location_rules_river_valley(world: TerraNilWorld) -> None:
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

    recyclingbase = tier2 & (
        HasAll(
            "Airship (River Valley)",
            "Recycling Drone (River Valley)",
            "Loading Dock (River Valley)",
        ) | Has("Recycling Silo")
    )
    recyclingfull = recyclingbase & HasAll(
        "Airship (River Valley)",
        "Recycling Drone (River Valley)",
        "Loading Dock (River Valley)",
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
            "Wildflower Blooms (River Valley)",
            "Migratory Birds Return (River Valley)",
            "Fungi In Forests (River Valley)",
        ]:
            world.set_rule(world.get_location(goal), climategoals)

        for goal in [
            "Ferns On Riverbanks (River Valley)",
            "Rains Begin (River Valley)",
            "Waterlillies Blossom (River Valley)",
            "Salmon Run (River Valley)",
        ]:
            world.set_rule(world.get_location(goal), climategoals & tier2 & Has("Recycling Silo (River Valley)"))

def set_all_location_rules_abandoned_quarry(world: TerraNilWorld) -> None:
    tier1 = Has("Tier 1 Completed (Abandoned Quarry)")
    tier2 = Has("Tier 2 Completed (Abandoned Quarry)")

    energy = Has("Wind Turbine (Abandoned Quarry)")
    lava = Has("Seismic Detonator (Abandoned Quarry)")
    water = energy & Has("Water Pump (Abandoned Quarry)")
    pollution = energy & Has("Toxin Scrubber (Abandoned Quarry)")
    greenery = pollution & Has("Irrigator (Abandoned Quarry)")

    world.set_rule(world.get_location("First Energy (Abandoned Quarry)"), energy)
    world.set_rule(world.get_location("First Pollution Removed (Abandoned Quarry)"), pollution)
    world.set_rule(world.get_location("First Greenery (Abandoned Quarry)"), water | greenery)
    world.set_rule(world.get_location("First Water (Abandoned Quarry)"), water)
    world.set_rule(world.get_location("First Lava (Abandoned Quarry)"), lava)

    world.set_rule(world.get_location("Greenery 25% (Abandoned Quarry)"), greenery)
    world.set_rule(world.get_location("Greenery 50% (Abandoned Quarry)"), greenery)
    world.set_rule(world.get_location("Greenery 75% (Abandoned Quarry)"), greenery)
    world.set_rule(world.get_location("Greenery 100% (Abandoned Quarry)"), greenery)
    world.set_rule(world.get_location("Tier 1 Completed (Abandoned Quarry)"), greenery)

    fire = tier1 & energy & HasAll("Solar Amplifier (Abandoned Quarry)", "Dehumidifier (Abandoned Quarry)")
    forest = fire & Has("Arboretum (Abandoned Quarry)")
    fynbos = forest & Has("Beehive (Abandoned Quarry)")
    wetlands = tier1 & water & Has("Hydroponium (Abandoned Quarry)")

    world.set_rule(world.get_location("First Fire (Abandoned Quarry)"), fire)
    world.set_rule(world.get_location("First Forest (Abandoned Quarry)"), forest)
    world.set_rule(world.get_location("Forest Completed (Abandoned Quarry)"), forest)
    world.set_rule(world.get_location("First Fynbos (Abandoned Quarry)"), fynbos)
    world.set_rule(world.get_location("Fynbos Completed (Abandoned Quarry)"), fynbos)
    world.set_rule(world.get_location("First Wetlands (Abandoned Quarry)"), wetlands)
    world.set_rule(world.get_location("Wetlands Completed (Abandoned Quarry)"), wetlands)
    world.set_rule(world.get_location("Tier 2 Completed (Abandoned Quarry)"), fynbos & forest & wetlands)

    photos = tier2 & Has("Animal Observatory (Abandoned Quarry)")

    world.set_rule(world.get_location("3 Photo Stars (Abandoned Quarry)"), photos)
    world.set_rule(world.get_location("10 Photo Stars (Abandoned Quarry)"), photos)
    world.set_rule(world.get_location("Bronze Photo (Abandoned Quarry)"), photos)
    world.set_rule(world.get_location("Silver Photo (Abandoned Quarry)"), photos)
    world.set_rule(world.get_location("Gold Photo (Abandoned Quarry)"), photos)

    recyclingbase = tier2 & (
        HasAll(
            "Airship (Abandoned Quarry)",
            "Recycling Drone (Abandoned Quarry)",
            "Flying Recycling Drone (Abandoned Quarry)",
            "Standalone Beacon (Abandoned Quarry)",
        ) |
        Has("Recycling Silo (Abandoned Quarry)")
    )
    recyclingfull = recyclingbase & HasAll(
        "Airship (Abandoned Quarry)",
        "Recycling Drone (Abandoned Quarry)",
        "Flying Recycling Drone (Abandoned Quarry)",
        "Standalone Beacon (Abandoned Quarry)",
        "Recycling Silo (Abandoned Quarry)",
        "Rock Hopper (Abandoned Quarry)",
    )

    world.set_rule(world.get_location("First Recycling (Abandoned Quarry)"), recyclingbase)
    world.set_rule(world.get_location("Recycling Completed (Abandoned Quarry)"), recyclingfull)

    world.set_rule(world.get_location("Liftoff (Abandoned Quarry)"), photos & recyclingfull)

    if world.options.climate_goals:
        climate = energy & water & Has("Cloud Seeder (Abandoned Quarry)")

        for goal in [
            "Wildflower Bloom (Abandoned Quarry)",
            "Migratory Birds Return (Abandoned Quarry)",
            "Fungi In Forests (Abandoned Quarry)",
        ]:
            world.set_rule(world.get_location(goal), climate)

        for goal in [
            "Ferns On Riverbanks (Abandoned Quarry)",
            "Waterlilies Blossom (Abandoned Quarry)",
            "Salmon Run (Abandoned Quarry)",
            "Rains Begin (Abandoned Quarry)",
        ]:
            world.set_rule(world.get_location(goal), climate & tier2 & Has("Recycling Silo (Abandoned Quarry)"))

def set_all_location_rules_polluted_bay(world: TerraNilWorld) -> None:
    tier1 = Has("Tier 1 Completed (Polluted Bay)")
    tier2 = Has("Tier 2 Completed (Polluted Bay)")

    energy = Has("Tidal Turbine (Polluted Bay)")
    water = energy & Has("Water Pump (Polluted Bay)")
    pollution = energy & Has("Toxin Scrubber (Polluted Bay)")
    first_greenery = pollution & Has("Irrigator (Polluted Bay)")
    greenery = first_greenery & Has("Pylon (Polluted Bay)")

    world.set_rule(world.get_location("First Energy (Polluted Bay)"), energy)
    world.set_rule(world.get_location("First Pollution Removed (Polluted Bay)"), pollution)
    world.set_rule(world.get_location("First Greenery (Polluted Bay)"), water | first_greenery)
    world.set_rule(world.get_location("First Water (Polluted Bay)"), water)

    world.set_rule(world.get_location("Greenery 25% (Polluted Bay)"), greenery)
    world.set_rule(world.get_location("Greenery 50% (Polluted Bay)"), greenery)
    world.set_rule(world.get_location("Greenery 75% (Polluted Bay)"), greenery)
    world.set_rule(world.get_location("Greenery 100% (Polluted Bay)"), greenery)
    world.set_rule(world.get_location("Tier 1 Completed (Polluted Bay)"), greenery)

    fynbos = tier1 & Has("Beehive (Polluted Bay)")
    fire = fynbos & energy & Has("Solar Amplifier (Polluted Bay)")
    forest = fire & Has("Arboretum (Polluted Bay)")
    wetlands = tier1 & water & Has("Hydroponium (Polluted Bay)")
    deciduousforest = tier1 & water & HasAll("Conservatory (Polluted Bay)", "Cloud Seeder (Polluted Bay)")

    world.set_rule(world.get_location("First Fire (Polluted Bay)"), fire)
    world.set_rule(world.get_location("First Forest (Polluted Bay)"), forest)
    world.set_rule(world.get_location("Forest Completed (Polluted Bay)"), forest)
    world.set_rule(world.get_location("First Fynbos (Polluted Bay)"), fynbos)
    world.set_rule(world.get_location("Fynbos Completed (Polluted Bay)"), fynbos)
    world.set_rule(world.get_location("First Wetlands (Polluted Bay)"), wetlands)
    world.set_rule(world.get_location("Wetlands Completed (Polluted Bay)"), wetlands)
    world.set_rule(world.get_location("First Deciduous Forest (Polluted Bay)"), deciduousforest)
    world.set_rule(world.get_location("Deciduous Forest Completed (Polluted Bay)"), deciduousforest)
    world.set_rule(world.get_location("Tier 2 Completed (Polluted Bay)"), fynbos & forest & wetlands & deciduousforest)

    photos = tier2 & Has("Animal Observatory (Polluted Bay)")

    world.set_rule(world.get_location("3 Photo Stars (Polluted Bay)"), photos)
    world.set_rule(world.get_location("10 Photo Stars (Polluted Bay)"), photos)
    world.set_rule(world.get_location("Bronze Photo (Polluted Bay)"), photos)
    world.set_rule(world.get_location("Silver Photo (Polluted Bay)"), photos)
    world.set_rule(world.get_location("Gold Photo (Polluted Bay)"), photos)

    recyclingbase = tier2 & (
        HasAll(
            "Airship (Polluted Bay)",
            "Recycling Drone (Polluted Bay)",
            "Loading Dock (Polluted Bay)",
        ) | Has("Recycling Silo")
    )
    recyclingfull = tier2 & HasAll(
        "Airship (Polluted Bay)",
        "Recycling Drone (Polluted Bay)",
        "Loading Dock (Polluted Bay)",
        "Recycling Silo (Polluted Bay)",
        "Water Pump (Polluted Bay)",
        "Excavator (Polluted Bay)",
    )

    world.set_rule(world.get_location("First Recycling (Polluted Bay)"), recyclingbase)
    world.set_rule(world.get_location("Recycling Completed (Polluted Bay)"), recyclingfull)

    world.set_rule(world.get_location("Liftoff (Polluted Bay)"), photos & recyclingfull)

    if world.options.climate_goals:
        climate = energy & water & Has("Cloud Seeder (Polluted Bay)")

        for goal in [
            "Wildflower Bloom (Polluted Bay)",
            "Migratory Birds Return (Polluted Bay)",
            "Fungi In Forests (Polluted Bay)",
        ]:
            world.set_rule(world.get_location(goal), climate)

        for goal in [
            "Ferns On Riverbanks (Polluted Bay)",
            "Cliff Foliage (Polluted Bay)",
            "Waterlilies Blossom (Polluted Bay)",
            "Salmon Run (Polluted Bay)",
            "Vegetation Boom (Polluted Bay)",
            "Rains Begin (Polluted Bay)",
        ]:
            world.set_rule(world.get_location(goal), climate & tier2 & Has("Recycling Silo (Polluted Bay)"))

def set_all_location_rules_hill_and_dale(world: TerraNilWorld) -> None:
    tier1 = Has("Tier 1 Completed (Hill and Dale)")
    tier2 = Has("Tier 2 Completed (Hill and Dale)")

    energy = Has("Wind Turbine (Hill and Dale)")
    water = energy & Has("Water Pump (Hill and Dale)")
    pollution = energy & Has("Cone Filter (Hill and Dale)")
    greenery = pollution & Has("Irrigator (Hill and Dale)")

    world.set_rule(world.get_location("First Energy (Hill and Dale)"), energy)
    world.set_rule(world.get_location("First Pollution Removed (Hill and Dale)"), pollution)
    world.set_rule(world.get_location("First Greenery (Hill and Dale)"), water | greenery)
    world.set_rule(world.get_location("First Water (Hill and Dale)"), water)

    world.set_rule(world.get_location("Greenery 25% (Hill and Dale)"), greenery)
    world.set_rule(world.get_location("Greenery 50% (Hill and Dale)"), greenery)
    world.set_rule(world.get_location("Greenery 75% (Hill and Dale)"), greenery)
    world.set_rule(world.get_location("Greenery 100% (Hill and Dale)"), greenery)
    world.set_rule(world.get_location("Tier 1 Completed (Hill and Dale)"), greenery)

    fynbos = tier1 & Has("Beehive (Hill and Dale)")
    fire = fynbos & energy & Has("Solar Amplifier (Hill and Dale)")
    forest = fire & Has("Arboretum (Hill and Dale)")
    wetlands = tier1 & water & Has("Hydroponium (Hill and Dale)")
    rockyscrubland = tier1 & Has("Chaparrallum (Hill and Dale)")

    world.set_rule(world.get_location("First Fire (Hill and Dale)"), fire)
    world.set_rule(world.get_location("First Forest (Hill and Dale)"), forest)
    world.set_rule(world.get_location("Forest Completed (Hill and Dale)"), forest)
    world.set_rule(world.get_location("First Fynbos (Hill and Dale)"), fynbos)
    world.set_rule(world.get_location("Fynbos Completed (Hill and Dale)"), fynbos)
    world.set_rule(world.get_location("First Wetlands (Hill and Dale)"), wetlands)
    world.set_rule(world.get_location("Wetlands Completed (Hill and Dale)"), wetlands)
    world.set_rule(world.get_location("First Rocky Scrublands (Hill and Dale)"), rockyscrubland)
    world.set_rule(world.get_location("Rocky Scrublands Completed (Hill and Dale)"), rockyscrubland)
    world.set_rule(world.get_location("Tier 2 Completed (Hill and Dale)"), fynbos & forest & wetlands & rockyscrubland)

    photos = tier2 & Has("Animal Observatory (Hill and Dale)")

    world.set_rule(world.get_location("3 Photo Stars (Hill and Dale)"), photos)
    world.set_rule(world.get_location("10 Photo Stars (Hill and Dale)"), photos)
    world.set_rule(world.get_location("Bronze Photo (Hill and Dale)"), photos)
    world.set_rule(world.get_location("Silver Photo (Hill and Dale)"), photos)
    world.set_rule(world.get_location("Gold Photo (Hill and Dale)"), photos)

    recyclingbase = tier2 & (
        HasAll(
            "Airship (Hill and Dale)",
            "Recycling Drone (Hill and Dale)",
            "Loading Dock (Hill and Dale)",
        ) | Has("Recycling Silo")
    )
    recyclingfull = recyclingbase & HasAll(
        "Airship (Hill and Dale)",
        "Recycling Drone (Hill and Dale)",
        "Loading Dock (Hill and Dale)",
        "Recycling Silo (Hill and Dale)",
        "Pound Lock (Hill and Dale)",
        "Water Pump (Hill and Dale)",
        "Excavator (Hill and Dale)",
    )

    world.set_rule(world.get_location("First Recycling (Hill and Dale)"), recyclingbase)
    world.set_rule(world.get_location("Recycling Completed (Hill and Dale)"), recyclingfull)

    world.set_rule(world.get_location("Liftoff (Hill and Dale)"), photos & recyclingfull)

    if world.options.climate_goals:
        humidity = energy & water & Has("Cloud Seeder (Hill and Dale)")
        temperature = energy & greenery & Has("Combustor (Hill and Dale)")

        for goal in [
            "Migratory Birds Return (Hill and Dale)",
            "Fungi In Forests (Hill and Dale)",
        ]:
            world.set_rule(world.get_location(goal), humidity)

        for goal in [
            "Salmon Run (Hill and Dale)",
        ]:
            world.set_rule(world.get_location(goal), temperature)

        for goal in [
            "Wildflower Bloom (Hill and Dale)",
            "Ferns On Riverbanks (Hill and Dale)",
            "Waterlilies Blossom (Hill and Dale)",
            "Rains Begin (Hill and Dale)",
        ]:
            world.set_rule(world.get_location(goal), humidity & temperature)

def set_all_location_rules_desolate_island(world: TerraNilWorld) -> None:
    tier1 = Has("Tier 1 Completed (Desolate Island)")
    tier2 = Has("Tier 2 Completed (Desolate Island)")

    energy = Has("Wind Turbine (Desolate Island)")
    world.set_rule(world.get_location("First Energy (Desolate Island)"), energy)

    world.set_rule(
        world.get_location("First Pollution Removed (Desolate Island)"),
        energy & Has("Toxin Scrubber (Desolate Island)")
    )

    world.set_rule(
        world.get_location("First Greenery (Desolate Island)"),
        energy & (
            HasAll("Toxin Scrubber (Desolate Island)", "Irrigator (Desolate Island)") |
            Has("Water Pump (Desolate Island)")
        )
    )

    water = energy & Has("Water Pump (Desolate Island)")
    world.set_rule(world.get_location("First River (Desolate Island)"), water)

    partial_greenery = energy & HasAll("Toxin Scrubber (Desolate Island)", "Irrigator (Desolate Island)")
    full_greenery = partial_greenery & Has("Mineralizer (Desolate Island)")
    world.set_rule(world.get_location("Greenery 25% (Desolate Island)"), partial_greenery)
    world.set_rule(world.get_location("Greenery 50% (Desolate Island)"), partial_greenery)
    world.set_rule(world.get_location("Greenery 75% (Desolate Island)"), full_greenery)
    world.set_rule(world.get_location("Greenery 100% (Desolate Island)"), full_greenery)
    world.set_rule(world.get_location("Tier 1 Completed (Desolate Island)"), full_greenery)

    beach = tier1 & HasAll("Littarium (Desolate Island)", "Combustor (Desolate Island)")
    world.set_rule(world.get_location("First Beach (Desolate Island)"), beach)
    world.set_rule(world.get_location("Beach Completed (Desolate Island)"), beach)

    partial_mangrove = tier1 & Has("Hydroponium (Desolate Island)")
    full_mangrove = partial_mangrove & Has("Salinator (Desolate Island)")
    world.set_rule(world.get_location("First Mangrove (Desolate Island)"), partial_mangrove)
    world.set_rule(world.get_location("Mangrove Completed (Desolate Island)"), full_mangrove)

    rainforest = tier1 & HasAll("Shadecloth Pillar (Desolate Island)", "Combustor (Desolate Island)")
    world.set_rule(world.get_location("First Tropical Forest (Desolate Island)"), rainforest)
    world.set_rule(world.get_location("Tropical Forest Completed (Desolate Island)"), rainforest)

    coralreef = tier1 & HasAll(
        "Coral Lab (Desolate Island)",
        "Combustor (Desolate Island)",
        "Sand Bank (Desolate Island)",
        "Monorail Node (Desolate Island)"
    )
    world.set_rule(world.get_location("First Coral Reef (Desolate Island)"), coralreef)
    world.set_rule(world.get_location("Coral Reef Completed (Desolate Island)"), coralreef)

    world.set_rule(world.get_location("Tier 2 Completed (Desolate Island)"), beach & full_mangrove & rainforest & coralreef)

    photos = tier2 & HasAll("Animal Observatory (Desolate Island)", "Sonic Pulse (Desolate Island)")
    world.set_rule(world.get_location("3 Photo Stars (Desolate Island)"), photos)
    world.set_rule(world.get_location("10 Photo Stars (Desolate Island)"), photos)
    world.set_rule(world.get_location("Bronze Photo (Desolate Island)"), photos)
    world.set_rule(world.get_location("Silver Photo (Desolate Island)"), photos)
    world.set_rule(world.get_location("Gold Photo (Desolate Island)"), photos)

    recyclingbase = tier2 & (
        HasAll(
            "Airship (Desolate Island)",
            "Recycler Station (Desolate Island)",
            "Recycling Beacon (Desolate Island)",
        ) |
        Has("Recycling Silo (Desolate Island)")
    )
    recyclingfull = recyclingbase & HasAll(
        "Airship (Desolate Island)",
        "Recycler Station (Desolate Island)",
        "Recycling Beacon (Desolate Island)",
        "Recycling Silo (Desolate Island)",
        "Rock Hopper (Desolate Island)",
    )

    world.set_rule(world.get_location("First Recycling (Desolate Island)"), recyclingbase)
    world.set_rule(world.get_location("Recycling Completed (Desolate Island)"), recyclingfull)

    world.set_rule(world.get_location("Liftoff (Desolate Island)"), photos & recyclingfull)

    if world.options.climate_goals:
        humidity = water & Has("Cloud Seeder (Desolate Island)")
        temperature = partial_greenery & Has("Combustor (Desolate Island)")

        for goal in [
            "Migratory Birds Return (Desolate Island)",
            "Crabs Populate Beaches (Desolate Island)",
            "Coconut Palms (Desolate Island)",
            "Dragonflies (Desolate Island)",
        ]:
            world.set_rule(world.get_location(goal), temperature)

        for goal in [
            "Moss On Rock Faces (Desolate Island)",
            "Ferns On Riverbanks (Desolate Island)",
            "Waterlilies Blossom (Desolate Island)",
        ]:
            world.set_rule(world.get_location(goal), humidity)

        for goal in [
            "Ivy Overgrowth (Desolate Island)",
            "Jellyfish Return (Desolate Island)",
            "Vines Grow (Desolate Island)",
            "Thunderstorms Begin (Desolate Island)",
        ]:
            world.set_rule(world.get_location(goal), humidity & temperature)

def set_all_location_rules_scorched_caldera(world: TerraNilWorld) -> None:
    tier1 = Has("Tier 1 Completed (Scorched Caldera)")
    tier2 = Has("Tier 2 Completed (Scorched Caldera)")

    energy = Has("Geothermal Plant (Scorched Caldera)")
    pollution = energy & Has("Cone Filter (Scorched Caldera)")
    first_greenery = pollution & Has("Irrigator (Scorched Caldera)")
    greenery = first_greenery & Has("Seismic Detonator (Scorched Caldera)")

    world.set_rule(world.get_location("First Energy (Scorched Caldera)"), energy)
    world.set_rule(world.get_location("First Pollution Removed (Scorched Caldera)"), pollution)
    world.set_rule(world.get_location("First Greenery (Scorched Caldera)"), first_greenery)

    world.set_rule(world.get_location("Greenery 25% (Scorched Caldera)"), first_greenery)
    world.set_rule(world.get_location("Greenery 50% (Scorched Caldera)"), greenery)
    world.set_rule(world.get_location("Greenery 75% (Scorched Caldera)"), greenery)
    world.set_rule(world.get_location("Greenery 100% (Scorched Caldera)"), greenery)
    world.set_rule(world.get_location("Tier 1 Completed (Scorched Caldera)"), greenery)

    water = tier1 & HasAll(
        "Transpirator (Scorched Caldera)",
        "Combustor (Scorched Caldera)",
        "Rock Hopper (Scorched Caldera)",
        "Monorail Node (Scorched Caldera)",
        "Seismic Detonator (Scorched Caldera)"
    )
    bamboo = tier1 & energy & Has("Mini Bamboo Nursery (Scorched Caldera)")
    tropicalforest = tier1 & Has("Shadecloth Pillar (Scorched Caldera)")
    lakevegetation = tropicalforest & water & Has("Percolotrium (Scorched Caldera)")

    world.set_rule(world.get_location("First Water (Scorched Caldera)"), water)
    world.set_rule(world.get_location("First Tropical Forest (Scorched Caldera)"), tropicalforest)
    world.set_rule(world.get_location("Tropical Forest Completed (Scorched Caldera)"), tropicalforest)
    world.set_rule(world.get_location("First Bamboo (Scorched Caldera)"), bamboo)
    world.set_rule(world.get_location("Bamboo Completed (Scorched Caldera)"), bamboo)
    world.set_rule(world.get_location("First Lake Vegetation (Scorched Caldera)"), lakevegetation)
    world.set_rule(world.get_location("Lake Vegetation Completed (Scorched Caldera)"), lakevegetation)
    world.set_rule(world.get_location("Tier 2 Completed (Scorched Caldera)"), bamboo & tropicalforest & lakevegetation)

    photos = tier2 & HasAll("Animal Observatory (Scorched Caldera)", "Sonic Pulse (Scorched Caldera)")
    world.set_rule(world.get_location("3 Photo Stars (Scorched Caldera)"), photos)
    world.set_rule(world.get_location("10 Photo Stars (Scorched Caldera)"), photos)
    world.set_rule(world.get_location("Bronze Photo (Scorched Caldera)"), photos)
    world.set_rule(world.get_location("Silver Photo (Scorched Caldera)"), photos)
    world.set_rule(world.get_location("Gold Photo (Scorched Caldera)"), photos)

    recyclingbase = tier2 & (
        HasAll(
            "Airship (Scorched Caldera)",
            "Recycler Station (Scorched Caldera)",
            "Recycling Beacon (Scorched Caldera)",
        ) |
        Has("Recycling Silo (Scorched Caldera)")
    )
    recyclingfull = recyclingbase & HasAll(
        "Airship (Scorched Caldera)",
        "Recycler Station (Scorched Caldera)",
        "Recycling Beacon (Scorched Caldera)",
        "Recycling Silo (Scorched Caldera)",
    )

    world.set_rule(world.get_location("First Recycling (Scorched Caldera)"), recyclingbase)
    world.set_rule(world.get_location("Recycling Completed (Scorched Caldera)"), recyclingfull)

    world.set_rule(world.get_location("Liftoff (Scorched Caldera)"), photos & recyclingfull)

    if world.options.climate_goals:
        for goal in [
            "Ivy Overgrowth (Scorched Caldera)",
            "Migratory Birds Return (Scorched Caldera)",
            "Ferns On Riverbanks (Scorched Caldera)",
            "Vines Grow (Scorched Caldera)",
            "Waterlilies Blossom (Scorched Caldera)",
            "Dragonflies (Scorched Caldera)",
            "Cloud Forests (Scorched Caldera)",
            "Moss On Rock Faces (Scorched Caldera)",
            "Thunderstorms Begin (Scorched Caldera)",
        ]:
            world.set_rule(world.get_location(goal), water)

def set_all_location_rules_volcanic_glacier(world: TerraNilWorld) -> None:
    tier1 = Has("Tier 1 Completed (Volcanic Glacier)")
    tier2 = Has("Tier 2 Completed (Volcanic Glacier)")

    lava = Has("Seismic Detonator (Volcanic Glacier)")
    energy = lava & Has("Geothermal Plant (Volcanic Glacier)")
    first_greenery = Has("Irrigator (Volcanic Glacier)")
    greenery = energy &first_greenery & Has("Toxin Scrubber (Volcanic Glacier)")

    world.set_rule(world.get_location("First Lava (Volcanic Glacier)"), lava)
    world.set_rule(world.get_location("First Energy (Volcanic Glacier)"), energy)
    world.set_rule(world.get_location("First Greenery (Volcanic Glacier)"), first_greenery)

    world.set_rule(world.get_location("Greenery 25% (Volcanic Glacier)"), greenery)
    world.set_rule(world.get_location("Greenery 50% (Volcanic Glacier)"), greenery)
    world.set_rule(world.get_location("Greenery 75% (Volcanic Glacier)"), greenery)
    world.set_rule(world.get_location("Greenery 100% (Volcanic Glacier)"), greenery)
    world.set_rule(world.get_location("Tier 1 Completed (Volcanic Glacier)"), greenery)

    tundra = tier1 & Has("Biodome (Volcanic Glacier)")
    fire = tundra & energy & Has("Solar Amplifier (Volcanic Glacier)")
    forest = fire & Has("Arboretum (Volcanic Glacier)")
    first_lichen = tier1 & Has("Algae Greenhouse (Volcanic Glacier)")
    lichen = first_lichen & Has("Radial Excavator (Volcanic Glacier)")
    kelpforest = first_lichen & Has("Monorail Node (Volcanic Glacier)")

    world.set_rule(world.get_location("First Fire (Volcanic Glacier)"), fire)
    world.set_rule(world.get_location("First Forest (Volcanic Glacier)"), forest)
    world.set_rule(world.get_location("Forest Completed (Volcanic Glacier)"), forest)
    world.set_rule(world.get_location("First Tundra (Volcanic Glacier)"), tundra)
    world.set_rule(world.get_location("Tundra Completed (Volcanic Glacier)"), tundra)
    world.set_rule(world.get_location("First Lichen (Volcanic Glacier)"), first_lichen)
    world.set_rule(world.get_location("Lichen Completed (Volcanic Glacier)"), lichen)
    world.set_rule(world.get_location("First Kelp Forest (Volcanic Glacier)"), kelpforest)
    world.set_rule(world.get_location("Kelp Forest Completed (Volcanic Glacier)"), kelpforest)
    world.set_rule(world.get_location("Tier 2 Completed (Volcanic Glacier)"), tundra & forest & lichen & kelpforest)

    photos = tier2 & Has("Animal Observatory (Volcanic Glacier)")

    world.set_rule(world.get_location("3 Photo Stars (Volcanic Glacier)"), photos)
    world.set_rule(world.get_location("10 Photo Stars (Volcanic Glacier)"), photos)
    world.set_rule(world.get_location("Bronze Photo (Volcanic Glacier)"), photos)
    world.set_rule(world.get_location("Silver Photo (Volcanic Glacier)"), photos)
    world.set_rule(world.get_location("Gold Photo (Volcanic Glacier)"), photos)

    recyclingbase = tier2 & (
        HasAll(
            "Airship (Volcanic Glacier)",
            "Recycler Station (Volcanic Glacier)",
            "Recycling Beacon (Volcanic Glacier)",
        ) |
        Has("Recycling Silo (Volcanic Glacier)")
    )
    recyclingfull = recyclingbase & HasAll(
        "Airship (Volcanic Glacier)",
        "Recycler Station (Volcanic Glacier)",
        "Recycling Beacon (Volcanic Glacier)",
        "Recycling Silo (Volcanic Glacier)",
        "Rock Hopper (Volcanic Glacier)",
    )

    world.set_rule(world.get_location("First Recycling (Volcanic Glacier)"), recyclingbase)
    world.set_rule(world.get_location("Recycling Completed (Volcanic Glacier)"), recyclingfull)

    world.set_rule(world.get_location("Liftoff (Volcanic Glacier)"), photos & recyclingfull)

    if world.options.climate_goals:
        humidity = energy & HasAll("Cloud Seeder (Volcanic Glacier)", "Dehumidifier (Volcanic Glacier)")
        temperature = energy & greenery & HasAll("Combustor (Volcanic Glacier)", "Flash Freezer (Volcanic Glacier)")
        radiation = greenery

        world.set_rule(world.get_location("Snow Melts (Volcanic Glacier)"), temperature)
        world.set_rule(world.get_location("Fungi In Forests (Volcanic Glacier)"), humidity)
        world.set_rule(world.get_location("Pelagic Fish (Volcanic Glacier)"), radiation)
        world.set_rule(world.get_location("Aurora (Volcanic Glacier)"), radiation)
        world.set_rule(world.get_location("Migratory Birds Return (Volcanic Glacier)"), temperature & radiation)
        world.set_rule(world.get_location("Icebergs Form (Volcanic Glacier)"), temperature & radiation)
        world.set_rule(world.get_location("Butterflies (Volcanic Glacier)"), temperature & radiation)
        world.set_rule(world.get_location("Moss On Boulders (Volcanic Glacier)"), humidity & temperature)
        world.set_rule(world.get_location("Ivy Overgrowth (Volcanic Glacier)"), humidity & temperature)
        world.set_rule(world.get_location("Moss On Rock Faces (Volcanic Glacier)"), humidity & temperature)
        world.set_rule(world.get_location("Snowfall Begins (Volcanic Glacier)"), humidity & temperature & radiation)

def set_completion_condition(world: TerraNilWorld) -> None:
    world.set_completion_rule(HasFromListUnique(
        *[f"Liftoff ({level})" for level in levels],
        count = world.options.levels_cleared_to_goal.value
        #"Liftoff (River Valley)",
        #"Liftoff (Abandoned Quarry)",
        #"Liftoff (Polluted Bay)",
        #"Liftoff (Hill and Dale)",
        #"Liftoff (Desolate Island)",
        #"Liftoff (Scorched Caldera)",
        #"Liftoff (Volcanic Glacier)",
    ))
