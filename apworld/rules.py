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
        world.set_rule(world.get_entrance(f"{level} Tier 1 to {level} Tier 2"), Has(f"{level} - Tier 1 Completed"))
        world.set_rule(world.get_entrance(f"{level} Tier 2 to {level} Tier 3"), Has(f"{level} - Tier 2 Completed"))
        world.set_rule(world.get_entrance(f"{level} Tier 3 to World Map"), Has(f"{level} - Liftoff"))

    if world.options.climate_goals:
        rivervalley_climate = world.get_entrance("River Valley Tier 2 to River Valley Climate Goals")
        world.set_rule(rivervalley_climate, Has("River Valley - Research Center"))

def set_all_location_rules(world: TerraNilWorld) -> None:
    set_all_location_rules_river_valley(world)
    set_all_location_rules_abandoned_quarry(world)
    set_all_location_rules_polluted_bay(world)
    set_all_location_rules_hill_and_dale(world)
    set_all_location_rules_desolate_island(world)
    set_all_location_rules_scorched_caldera(world)
    set_all_location_rules_volcanic_glacier(world)

def set_all_location_rules_river_valley(world: TerraNilWorld) -> None:
    tier1 = Has("River Valley - Tier 1 Completed")
    tier2 = Has("River Valley - Tier 2 Completed")

    energy = Has("River Valley - Wind Turbine")
    world.set_rule(world.get_location("River Valley - First Energy"), energy)

    world.set_rule(
        world.get_location("River Valley - First Pollution Removed"),
        energy & Has("River Valley - Toxin Scrubber")
    )

    world.set_rule(
        world.get_location("River Valley - First Greenery"),
        energy & (
            HasAll("River Valley - Toxin Scrubber", "River Valley - Irrigator") |
            Has("River Valley - Water Pump")
        )
    )

    water = energy & Has("River Valley - Water Pump")
    if world.options.rain_logic:
        water = energy & (
            Has("River Valley - Water Pump") |
            (tier1 & HasAll("River Valley - Research Center", "River Valley - Toxin Scrubber", "River Valley - Irrigator"))
        )

    world.set_rule(world.get_location("River Valley - First Water"), water)

    greenery = energy & HasAll("River Valley - Toxin Scrubber", "River Valley - Irrigator")
    world.set_rule(world.get_location("River Valley - Greenery 25%"), greenery)
    world.set_rule(world.get_location("River Valley - Greenery 50%"), greenery)
    world.set_rule(world.get_location("River Valley - Greenery 75%"), greenery)
    world.set_rule(world.get_location("River Valley - Greenery 100%"), greenery)
    world.set_rule(world.get_location("River Valley - Tier 1 Completed"), greenery)

    fynbos = tier1 & Has("River Valley - Beehive")
    world.set_rule(world.get_location("River Valley - First Fynbos"), fynbos)
    world.set_rule(world.get_location("River Valley - Fynbos Completed"), fynbos)

    wetlands = tier1 & water & Has("River Valley - Hydroponium")
    world.set_rule(world.get_location("River Valley - First Wetlands"), wetlands)
    world.set_rule(world.get_location("River Valley - Wetlands Completed"), wetlands)

    fire = tier1 & HasAll("River Valley - Beehive", "River Valley - Solar Amplifier")
    world.set_rule(world.get_location("River Valley - First Fire"), fire)

    forest = fire & Has("River Valley - Arboretum")
    world.set_rule(world.get_location("River Valley - First Forest"), forest)
    world.set_rule(world.get_location("River Valley - Forest Completed"), forest)

    world.set_rule(world.get_location("River Valley - Tier 2 Completed"), fynbos & wetlands & forest)

    photos = tier2 & HasAll("River Valley - Animal Observatory", "River Valley - Wildlife Bridge", "River Valley - Sonic Pulse")
    world.set_rule(world.get_location("River Valley - 3 Photo Stars"), photos)
    world.set_rule(world.get_location("River Valley - 10 Photo Stars"), photos)
    world.set_rule(world.get_location("River Valley - Bronze Photo"), photos)
    world.set_rule(world.get_location("River Valley - Silver Photo"), photos)
    world.set_rule(world.get_location("River Valley - Gold Photo"), photos)

    recyclingbase = tier2 & (
        HasAll(
            "River Valley - Airship",
            "River Valley - Recycling Drone",
            "River Valley - Loading Dock",
        ) | Has("Recycling Silo")
    )
    recyclingfull = recyclingbase & HasAll(
        "River Valley - Airship",
        "River Valley - Recycling Drone",
        "River Valley - Loading Dock",
        "River Valley - Recycling Silo",
        "River Valley - Pound Lock",
        "River Valley - Water Pump",
        "River Valley - Excavator",
    )

    world.set_rule(world.get_location("River Valley - First Recycling"), recyclingbase)
    world.set_rule(world.get_location("River Valley - Recycling Completed"), recyclingfull)

    world.set_rule(world.get_location("River Valley - Liftoff"), photos & recyclingfull)

    if world.options.climate_goals:
        climategoals = tier1 & Has("River Valley - Research Center")

        if not world.options.rain_logic:
            climategoals = climategoals & water & Has("River Valley - Cloud Seeder")

        for goal in [
            "River Valley - Wildflower Blooms",
            "River Valley - Migratory Birds Return",
            "River Valley - Fungi In Forests",
        ]:
            world.set_rule(world.get_location(goal), climategoals)

        for goal in [
            "River Valley - Ferns On Riverbanks",
            "River Valley - Rains Begin",
            "River Valley - Waterlillies Blossom",
            "River Valley - Salmon Run",
        ]:
            world.set_rule(world.get_location(goal), climategoals & tier2 & Has("River Valley - Recycling Silo"))

def set_all_location_rules_abandoned_quarry(world: TerraNilWorld) -> None:
    tier1 = Has("Abandoned Quarry - Tier 1 Completed")
    tier2 = Has("Abandoned Quarry - Tier 2 Completed")

    energy = Has("Abandoned Quarry - Wind Turbine")
    lava = Has("Abandoned Quarry - Seismic Detonator")
    water = energy & Has("Abandoned Quarry - Water Pump")
    pollution = energy & Has("Abandoned Quarry - Toxin Scrubber")
    greenery = pollution & Has("Abandoned Quarry - Irrigator")

    world.set_rule(world.get_location("Abandoned Quarry - First Energy"), energy)
    world.set_rule(world.get_location("Abandoned Quarry - First Pollution Removed"), pollution)
    world.set_rule(world.get_location("Abandoned Quarry - First Greenery"), water | greenery)
    world.set_rule(world.get_location("Abandoned Quarry - First Water"), water)
    world.set_rule(world.get_location("Abandoned Quarry - First Lava"), lava)

    world.set_rule(world.get_location("Abandoned Quarry - Greenery 25%"), greenery)
    world.set_rule(world.get_location("Abandoned Quarry - Greenery 50%"), greenery)
    world.set_rule(world.get_location("Abandoned Quarry - Greenery 75%"), greenery)
    world.set_rule(world.get_location("Abandoned Quarry - Greenery 100%"), greenery)
    world.set_rule(world.get_location("Abandoned Quarry - Tier 1 Completed"), greenery)

    fire = tier1 & energy & HasAll("Abandoned Quarry - Solar Amplifier", "Abandoned Quarry - Dehumidifier")
    forest = fire & Has("Abandoned Quarry - Arboretum")
    fynbos = forest & Has("Abandoned Quarry - Beehive")
    wetlands = tier1 & water & Has("Abandoned Quarry - Hydroponium")

    world.set_rule(world.get_location("Abandoned Quarry - First Fire"), fire)
    world.set_rule(world.get_location("Abandoned Quarry - First Forest"), forest)
    world.set_rule(world.get_location("Abandoned Quarry - Forest Completed"), forest)
    world.set_rule(world.get_location("Abandoned Quarry - First Fynbos"), fynbos)
    world.set_rule(world.get_location("Abandoned Quarry - Fynbos Completed"), fynbos)
    world.set_rule(world.get_location("Abandoned Quarry - First Wetlands"), wetlands)
    world.set_rule(world.get_location("Abandoned Quarry - Wetlands Completed"), wetlands)
    world.set_rule(world.get_location("Abandoned Quarry - Tier 2 Completed"), fynbos & forest & wetlands)

    photos = tier2 & Has("Abandoned Quarry - Animal Observatory")

    world.set_rule(world.get_location("Abandoned Quarry - 3 Photo Stars"), photos)
    world.set_rule(world.get_location("Abandoned Quarry - 10 Photo Stars"), photos)
    world.set_rule(world.get_location("Abandoned Quarry - Bronze Photo"), photos)
    world.set_rule(world.get_location("Abandoned Quarry - Silver Photo"), photos)
    world.set_rule(world.get_location("Abandoned Quarry - Gold Photo"), photos)

    recyclingbase = tier2 & (
        HasAll(
            "Abandoned Quarry - Airship",
            "Abandoned Quarry - Recycling Drone",
            "Abandoned Quarry - Flying Recycling Drone",
            "Abandoned Quarry - Standalone Beacon",
        ) |
        Has("Abandoned Quarry - Recycling Silo")
    )
    recyclingfull = recyclingbase & HasAll(
        "Abandoned Quarry - Airship",
        "Abandoned Quarry - Recycling Drone",
        "Abandoned Quarry - Flying Recycling Drone",
        "Abandoned Quarry - Standalone Beacon",
        "Abandoned Quarry - Recycling Silo",
        "Abandoned Quarry - Rock Hopper",
    )

    world.set_rule(world.get_location("Abandoned Quarry - First Recycling"), recyclingbase)
    world.set_rule(world.get_location("Abandoned Quarry - Recycling Completed"), recyclingfull)

    world.set_rule(world.get_location("Abandoned Quarry - Liftoff"), photos & recyclingfull)

    if world.options.climate_goals:
        climate = energy & water & Has("Abandoned Quarry - Cloud Seeder")

        for goal in [
            "Abandoned Quarry - Wildflower Bloom",
            "Abandoned Quarry - Migratory Birds Return",
            "Abandoned Quarry - Fungi In Forests",
        ]:
            world.set_rule(world.get_location(goal), climate)

        for goal in [
            "Abandoned Quarry - Ferns On Riverbanks",
            "Abandoned Quarry - Waterlilies Blossom",
            "Abandoned Quarry - Salmon Run",
            "Abandoned Quarry - Rains Begin",
        ]:
            world.set_rule(world.get_location(goal), climate & tier2 & Has("Abandoned Quarry - Recycling Silo"))

def set_all_location_rules_polluted_bay(world: TerraNilWorld) -> None:
    tier1 = Has("Polluted Bay - Tier 1 Completed")
    tier2 = Has("Polluted Bay - Tier 2 Completed")

    energy = Has("Polluted Bay - Tidal Turbine")
    water = energy & Has("Polluted Bay - Water Pump")
    pollution = energy & Has("Polluted Bay - Toxin Scrubber")
    first_greenery = pollution & Has("Polluted Bay - Irrigator")
    greenery = first_greenery & Has("Polluted Bay - Pylon")

    world.set_rule(world.get_location("Polluted Bay - First Energy"), energy)
    world.set_rule(world.get_location("Polluted Bay - First Pollution Removed"), pollution)
    world.set_rule(world.get_location("Polluted Bay - First Greenery"), water | first_greenery)
    world.set_rule(world.get_location("Polluted Bay - First Water"), water)

    world.set_rule(world.get_location("Polluted Bay - Greenery 25%"), greenery)
    world.set_rule(world.get_location("Polluted Bay - Greenery 50%"), greenery)
    world.set_rule(world.get_location("Polluted Bay - Greenery 75%"), greenery)
    world.set_rule(world.get_location("Polluted Bay - Greenery 100%"), greenery)
    world.set_rule(world.get_location("Polluted Bay - Tier 1 Completed"), greenery)

    fynbos = tier1 & Has("Polluted Bay - Beehive")
    fire = fynbos & energy & Has("Polluted Bay - Solar Amplifier")
    forest = fire & Has("Polluted Bay - Arboretum")
    wetlands = tier1 & water & Has("Polluted Bay - Hydroponium")
    deciduousforest = tier1 & water & HasAll("Polluted Bay - Conservatory", "Polluted Bay - Cloud Seeder")

    world.set_rule(world.get_location("Polluted Bay - First Fire"), fire)
    world.set_rule(world.get_location("Polluted Bay - First Forest"), forest)
    world.set_rule(world.get_location("Polluted Bay - Forest Completed"), forest)
    world.set_rule(world.get_location("Polluted Bay - First Fynbos"), fynbos)
    world.set_rule(world.get_location("Polluted Bay - Fynbos Completed"), fynbos)
    world.set_rule(world.get_location("Polluted Bay - First Wetlands"), wetlands)
    world.set_rule(world.get_location("Polluted Bay - Wetlands Completed"), wetlands)
    world.set_rule(world.get_location("Polluted Bay - First Deciduous Forest"), deciduousforest)
    world.set_rule(world.get_location("Polluted Bay - Deciduous Forest Completed"), deciduousforest)
    world.set_rule(world.get_location("Polluted Bay - Tier 2 Completed"), fynbos & forest & wetlands & deciduousforest)

    photos = tier2 & Has("Polluted Bay - Animal Observatory")

    world.set_rule(world.get_location("Polluted Bay - 3 Photo Stars"), photos)
    world.set_rule(world.get_location("Polluted Bay - 10 Photo Stars"), photos)
    world.set_rule(world.get_location("Polluted Bay - Bronze Photo"), photos)
    world.set_rule(world.get_location("Polluted Bay - Silver Photo"), photos)
    world.set_rule(world.get_location("Polluted Bay - Gold Photo"), photos)

    recyclingbase = tier2 & (
        HasAll(
            "Polluted Bay - Airship",
            "Polluted Bay - Recycling Drone",
            "Polluted Bay - Loading Dock",
        ) | Has("Recycling Silo")
    )
    recyclingfull = tier2 & HasAll(
        "Polluted Bay - Airship",
        "Polluted Bay - Recycling Drone",
        "Polluted Bay - Loading Dock",
        "Polluted Bay - Recycling Silo",
        "Polluted Bay - Water Pump",
        "Polluted Bay - Excavator",
    )

    world.set_rule(world.get_location("Polluted Bay - First Recycling"), recyclingbase)
    world.set_rule(world.get_location("Polluted Bay - Recycling Completed"), recyclingfull)

    world.set_rule(world.get_location("Polluted Bay - Liftoff"), photos & recyclingfull)

    if world.options.climate_goals:
        climate = energy & water & Has("Polluted Bay - Cloud Seeder")

        for goal in [
            "Polluted Bay - Wildflower Bloom",
            "Polluted Bay - Migratory Birds Return",
            "Polluted Bay - Fungi In Forests",
        ]:
            world.set_rule(world.get_location(goal), climate)

        for goal in [
            "Polluted Bay - Ferns On Riverbanks",
            "Polluted Bay - Cliff Foliage",
            "Polluted Bay - Waterlilies Blossom",
            "Polluted Bay - Salmon Run",
            "Polluted Bay - Vegetation Boom",
            "Polluted Bay - Rains Begin",
        ]:
            world.set_rule(world.get_location(goal), climate & tier2 & Has("Polluted Bay - Recycling Silo"))

def set_all_location_rules_hill_and_dale(world: TerraNilWorld) -> None:
    tier1 = Has("Hill and Dale - Tier 1 Completed")
    tier2 = Has("Hill and Dale - Tier 2 Completed")

    energy = Has("Hill and Dale - Wind Turbine")
    water = energy & Has("Hill and Dale - Water Pump")
    pollution = energy & Has("Hill and Dale - Cone Filter")
    greenery = pollution & Has("Hill and Dale - Irrigator")

    world.set_rule(world.get_location("Hill and Dale - First Energy"), energy)
    world.set_rule(world.get_location("Hill and Dale - First Pollution Removed"), pollution)
    world.set_rule(world.get_location("Hill and Dale - First Greenery"), water | greenery)
    world.set_rule(world.get_location("Hill and Dale - First Water"), water)

    world.set_rule(world.get_location("Hill and Dale - Greenery 25%"), greenery)
    world.set_rule(world.get_location("Hill and Dale - Greenery 50%"), greenery)
    world.set_rule(world.get_location("Hill and Dale - Greenery 75%"), greenery)
    world.set_rule(world.get_location("Hill and Dale - Greenery 100%"), greenery)
    world.set_rule(world.get_location("Hill and Dale - Tier 1 Completed"), greenery)

    fynbos = tier1 & Has("Hill and Dale - Beehive")
    fire = fynbos & energy & Has("Hill and Dale - Solar Amplifier")
    forest = fire & Has("Hill and Dale - Arboretum")
    wetlands = tier1 & water & Has("Hill and Dale - Hydroponium")
    rockyscrubland = tier1 & Has("Hill and Dale - Chaparrallum")

    world.set_rule(world.get_location("Hill and Dale - First Fire"), fire)
    world.set_rule(world.get_location("Hill and Dale - First Forest"), forest)
    world.set_rule(world.get_location("Hill and Dale - Forest Completed"), forest)
    world.set_rule(world.get_location("Hill and Dale - First Fynbos"), fynbos)
    world.set_rule(world.get_location("Hill and Dale - Fynbos Completed"), fynbos)
    world.set_rule(world.get_location("Hill and Dale - First Wetlands"), wetlands)
    world.set_rule(world.get_location("Hill and Dale - Wetlands Completed"), wetlands)
    world.set_rule(world.get_location("Hill and Dale - First Rocky Scrublands"), rockyscrubland)
    world.set_rule(world.get_location("Hill and Dale - Rocky Scrublands Completed"), rockyscrubland)
    world.set_rule(world.get_location("Hill and Dale - Tier 2 Completed"), fynbos & forest & wetlands & rockyscrubland)

    photos = tier2 & Has("Hill and Dale - Animal Observatory")

    world.set_rule(world.get_location("Hill and Dale - 3 Photo Stars"), photos)
    world.set_rule(world.get_location("Hill and Dale - 10 Photo Stars"), photos)
    world.set_rule(world.get_location("Hill and Dale - Bronze Photo"), photos)
    world.set_rule(world.get_location("Hill and Dale - Silver Photo"), photos)
    world.set_rule(world.get_location("Hill and Dale - Gold Photo"), photos)

    recyclingbase = tier2 & (
        HasAll(
            "Hill and Dale - Airship",
            "Hill and Dale - Recycling Drone",
            "Hill and Dale - Loading Dock",
        ) | Has("Recycling Silo")
    )
    recyclingfull = recyclingbase & HasAll(
        "Hill and Dale - Airship",
        "Hill and Dale - Recycling Drone",
        "Hill and Dale - Loading Dock",
        "Hill and Dale - Recycling Silo",
        "Hill and Dale - Pound Lock",
        "Hill and Dale - Water Pump",
        "Hill and Dale - Excavator",
    )

    world.set_rule(world.get_location("Hill and Dale - First Recycling"), recyclingbase)
    world.set_rule(world.get_location("Hill and Dale - Recycling Completed"), recyclingfull)

    world.set_rule(world.get_location("Hill and Dale - Liftoff"), photos & recyclingfull)

    if world.options.climate_goals:
        humidity = energy & water & Has("Hill and Dale - Cloud Seeder")
        temperature = energy & greenery & Has("Hill and Dale - Combustor")

        for goal in [
            "Hill and Dale - Migratory Birds Return",
            "Hill and Dale - Fungi In Forests",
        ]:
            world.set_rule(world.get_location(goal), humidity)

        for goal in [
            "Hill and Dale - Salmon Run",
        ]:
            world.set_rule(world.get_location(goal), temperature)

        for goal in [
            "Hill and Dale - Wildflower Bloom",
            "Hill and Dale - Ferns On Riverbanks",
            "Hill and Dale - Waterlilies Blossom",
            "Hill and Dale - Rains Begin",
        ]:
            world.set_rule(world.get_location(goal), humidity & temperature)

def set_all_location_rules_desolate_island(world: TerraNilWorld) -> None:
    tier1 = Has("Desolate Island - Tier 1 Completed")
    tier2 = Has("Desolate Island - Tier 2 Completed")

    energy = Has("Desolate Island - Wind Turbine")
    world.set_rule(world.get_location("Desolate Island - First Energy"), energy)

    world.set_rule(
        world.get_location("Desolate Island - First Pollution Removed"),
        energy & Has("Desolate Island - Toxin Scrubber")
    )

    world.set_rule(
        world.get_location("Desolate Island - First Greenery"),
        energy & (
            HasAll("Desolate Island - Toxin Scrubber", "Desolate Island - Irrigator") |
            Has("Desolate Island - Water Pump")
        )
    )

    water = energy & Has("Desolate Island - Water Pump")
    world.set_rule(world.get_location("Desolate Island - First River"), water)

    partial_greenery = energy & HasAll("Desolate Island - Toxin Scrubber", "Desolate Island - Irrigator")
    full_greenery = partial_greenery & Has("Desolate Island - Mineralizer")
    world.set_rule(world.get_location("Desolate Island - Greenery 25%"), partial_greenery)
    world.set_rule(world.get_location("Desolate Island - Greenery 50%"), partial_greenery)
    world.set_rule(world.get_location("Desolate Island - Greenery 75%"), full_greenery)
    world.set_rule(world.get_location("Desolate Island - Greenery 100%"), full_greenery)
    world.set_rule(world.get_location("Desolate Island - Tier 1 Completed"), full_greenery)

    beach = tier1 & HasAll("Desolate Island - Littarium", "Desolate Island - Combustor")
    world.set_rule(world.get_location("Desolate Island - First Beach"), beach)
    world.set_rule(world.get_location("Desolate Island - Beach Completed"), beach)

    partial_mangrove = tier1 & Has("Desolate Island - Hydroponium")
    full_mangrove = partial_mangrove & Has("Desolate Island - Salinator")
    world.set_rule(world.get_location("Desolate Island - First Mangrove"), partial_mangrove)
    world.set_rule(world.get_location("Desolate Island - Mangrove Completed"), full_mangrove)

    rainforest = tier1 & HasAll("Desolate Island - Shadecloth Pillar", "Desolate Island - Combustor")
    world.set_rule(world.get_location("Desolate Island - First Tropical Forest"), rainforest)
    world.set_rule(world.get_location("Desolate Island - Tropical Forest Completed"), rainforest)

    coralreef = tier1 & HasAll(
        "Desolate Island - Coral Lab",
        "Desolate Island - Combustor",
        "Desolate Island - Sand Bank",
        "Desolate Island - Monorail Node"
    )
    world.set_rule(world.get_location("Desolate Island - First Coral Reef"), coralreef)
    world.set_rule(world.get_location("Desolate Island - Coral Reef Completed"), coralreef)

    world.set_rule(world.get_location("Desolate Island - Tier 2 Completed"), beach & full_mangrove & rainforest & coralreef)

    photos = tier2 & HasAll("Desolate Island - Animal Observatory", "Desolate Island - Sonic Pulse")
    world.set_rule(world.get_location("Desolate Island - 3 Photo Stars"), photos)
    world.set_rule(world.get_location("Desolate Island - 10 Photo Stars"), photos)
    world.set_rule(world.get_location("Desolate Island - Bronze Photo"), photos)
    world.set_rule(world.get_location("Desolate Island - Silver Photo"), photos)
    world.set_rule(world.get_location("Desolate Island - Gold Photo"), photos)

    recyclingbase = tier2 & (
        HasAll(
            "Desolate Island - Airship",
            "Desolate Island - Recycler Station",
            "Desolate Island - Recycling Beacon",
        ) |
        Has("Desolate Island - Recycling Silo")
    )
    recyclingfull = recyclingbase & HasAll(
        "Desolate Island - Airship",
        "Desolate Island - Recycler Station",
        "Desolate Island - Recycling Beacon",
        "Desolate Island - Recycling Silo",
        "Desolate Island - Rock Hopper",
    )

    world.set_rule(world.get_location("Desolate Island - First Recycling"), recyclingbase)
    world.set_rule(world.get_location("Desolate Island - Recycling Completed"), recyclingfull)

    world.set_rule(world.get_location("Desolate Island - Liftoff"), photos & recyclingfull)

    if world.options.climate_goals:
        humidity = water & Has("Desolate Island - Cloud Seeder")
        temperature = partial_greenery & Has("Desolate Island - Combustor")

        for goal in [
            "Desolate Island - Migratory Birds Return",
            "Desolate Island - Crabs Populate Beaches",
            "Desolate Island - Coconut Palms",
            "Desolate Island - Dragonflies",
        ]:
            world.set_rule(world.get_location(goal), temperature)

        for goal in [
            "Desolate Island - Moss On Rock Faces",
            "Desolate Island - Ferns On Riverbanks",
            "Desolate Island - Waterlilies Blossom",
        ]:
            world.set_rule(world.get_location(goal), humidity)

        for goal in [
            "Desolate Island - Ivy Overgrowth",
            "Desolate Island - Jellyfish Return",
            "Desolate Island - Vines Grow",
            "Desolate Island - Thunderstorms Begin",
        ]:
            world.set_rule(world.get_location(goal), humidity & temperature)

def set_all_location_rules_scorched_caldera(world: TerraNilWorld) -> None:
    tier1 = Has("Scorched Caldera - Tier 1 Completed")
    tier2 = Has("Scorched Caldera - Tier 2 Completed")

    energy = Has("Scorched Caldera - Geothermal Plant")
    pollution = energy & Has("Scorched Caldera - Cone Filter")
    first_greenery = pollution & Has("Scorched Caldera - Irrigator")
    greenery = first_greenery & Has("Scorched Caldera - Seismic Detonator")

    world.set_rule(world.get_location("Scorched Caldera - First Energy"), energy)
    world.set_rule(world.get_location("Scorched Caldera - First Pollution Removed"), pollution)
    world.set_rule(world.get_location("Scorched Caldera - First Greenery"), first_greenery)

    world.set_rule(world.get_location("Scorched Caldera - Greenery 25%"), first_greenery)
    world.set_rule(world.get_location("Scorched Caldera - Greenery 50%"), greenery)
    world.set_rule(world.get_location("Scorched Caldera - Greenery 75%"), greenery)
    world.set_rule(world.get_location("Scorched Caldera - Greenery 100%"), greenery)
    world.set_rule(world.get_location("Scorched Caldera - Tier 1 Completed"), greenery)

    water = tier1 & HasAll(
        "Scorched Caldera - Transpirator",
        "Scorched Caldera - Combustor",
        "Scorched Caldera - Rock Hopper",
        "Scorched Caldera - Monorail Node",
        "Scorched Caldera - Seismic Detonator"
    )
    bamboo = tier1 & energy & Has("Scorched Caldera - Mini Bamboo Nursery")
    tropicalforest = tier1 & Has("Scorched Caldera - Shadecloth Pillar")
    lakevegetation = tropicalforest & water & Has("Scorched Caldera - Percolotrium")

    world.set_rule(world.get_location("Scorched Caldera - First Water"), water)
    world.set_rule(world.get_location("Scorched Caldera - First Tropical Forest"), tropicalforest)
    world.set_rule(world.get_location("Scorched Caldera - Tropical Forest Completed"), tropicalforest)
    world.set_rule(world.get_location("Scorched Caldera - First Bamboo"), bamboo)
    world.set_rule(world.get_location("Scorched Caldera - Bamboo Completed"), bamboo)
    world.set_rule(world.get_location("Scorched Caldera - First Lake Vegetation"), lakevegetation)
    world.set_rule(world.get_location("Scorched Caldera - Lake Vegetation Completed"), lakevegetation)
    world.set_rule(world.get_location("Scorched Caldera - Tier 2 Completed"), bamboo & tropicalforest & lakevegetation)

    photos = tier2 & HasAll("Scorched Caldera - Animal Observatory", "Scorched Caldera - Sonic Pulse")
    world.set_rule(world.get_location("Scorched Caldera - 3 Photo Stars"), photos)
    world.set_rule(world.get_location("Scorched Caldera - 10 Photo Stars"), photos)
    world.set_rule(world.get_location("Scorched Caldera - Bronze Photo"), photos)
    world.set_rule(world.get_location("Scorched Caldera - Silver Photo"), photos)
    world.set_rule(world.get_location("Scorched Caldera - Gold Photo"), photos)

    recyclingbase = tier2 & (
        HasAll(
            "Scorched Caldera - Airship",
            "Scorched Caldera - Recycler Station",
            "Scorched Caldera - Recycling Beacon",
        ) |
        Has("Scorched Caldera - Recycling Silo")
    )
    recyclingfull = recyclingbase & HasAll(
        "Scorched Caldera - Airship",
        "Scorched Caldera - Recycler Station",
        "Scorched Caldera - Recycling Beacon",
        "Scorched Caldera - Recycling Silo",
    )

    world.set_rule(world.get_location("Scorched Caldera - First Recycling"), recyclingbase)
    world.set_rule(world.get_location("Scorched Caldera - Recycling Completed"), recyclingfull)

    world.set_rule(world.get_location("Scorched Caldera - Liftoff"), photos & recyclingfull)

    if world.options.climate_goals:
        for goal in [
            "Scorched Caldera - Ivy Overgrowth",
            "Scorched Caldera - Migratory Birds Return",
            "Scorched Caldera - Ferns On Riverbanks",
            "Scorched Caldera - Vines Grow",
            "Scorched Caldera - Waterlilies Blossom",
            "Scorched Caldera - Dragonflies",
            "Scorched Caldera - Cloud Forests",
            "Scorched Caldera - Moss On Rock Faces",
            "Scorched Caldera - Thunderstorms Begin",
        ]:
            world.set_rule(world.get_location(goal), water)

def set_all_location_rules_volcanic_glacier(world: TerraNilWorld) -> None:
    tier1 = Has("Volcanic Glacier - Tier 1 Completed")
    tier2 = Has("Volcanic Glacier - Tier 2 Completed")

    lava = Has("Volcanic Glacier - Seismic Detonator")
    energy = lava & Has("Volcanic Glacier - Geothermal Plant")
    first_greenery = Has("Volcanic Glacier - Irrigator")
    greenery = energy &first_greenery & Has("Volcanic Glacier - Toxin Scrubber")

    world.set_rule(world.get_location("Volcanic Glacier - First Lava"), lava)
    world.set_rule(world.get_location("Volcanic Glacier - First Energy"), energy)
    world.set_rule(world.get_location("Volcanic Glacier - First Greenery"), first_greenery)

    world.set_rule(world.get_location("Volcanic Glacier - Greenery 25%"), greenery)
    world.set_rule(world.get_location("Volcanic Glacier - Greenery 50%"), greenery)
    world.set_rule(world.get_location("Volcanic Glacier - Greenery 75%"), greenery)
    world.set_rule(world.get_location("Volcanic Glacier - Greenery 100%"), greenery)
    world.set_rule(world.get_location("Volcanic Glacier - Tier 1 Completed"), greenery)

    tundra = tier1 & Has("Volcanic Glacier - Biodome")
    fire = energy & Has("Volcanic Glacier - Solar Amplifier") & (tundra | Has("Volcanic Glacier - Dehumidifier"))
    forest = fire & Has("Volcanic Glacier - Arboretum")
    first_lichen = tier1 & Has("Volcanic Glacier - Algae Greenhouse")
    lichen = first_lichen & HasAll("Volcanic Glacier - Radial Excavator", "Volcanic Glacier - Igneous Heatsink")
    kelpforest = first_lichen & Has("Volcanic Glacier - Monorail Node")

    world.set_rule(world.get_location("Volcanic Glacier - First Fire"), fire)
    world.set_rule(world.get_location("Volcanic Glacier - First Forest"), forest)
    world.set_rule(world.get_location("Volcanic Glacier - Forest Completed"), forest)
    world.set_rule(world.get_location("Volcanic Glacier - First Tundra"), tundra)
    world.set_rule(world.get_location("Volcanic Glacier - Tundra Completed"), tundra)
    world.set_rule(world.get_location("Volcanic Glacier - First Lichen"), first_lichen)
    world.set_rule(world.get_location("Volcanic Glacier - Lichen Completed"), lichen)
    world.set_rule(world.get_location("Volcanic Glacier - First Kelp Forest"), kelpforest)
    world.set_rule(world.get_location("Volcanic Glacier - Kelp Forest Completed"), kelpforest)
    world.set_rule(world.get_location("Volcanic Glacier - Tier 2 Completed"), tundra & forest & lichen & kelpforest)

    photos = tier2 & Has("Volcanic Glacier - Animal Observatory")

    world.set_rule(world.get_location("Volcanic Glacier - 3 Photo Stars"), photos)
    world.set_rule(world.get_location("Volcanic Glacier - 10 Photo Stars"), photos)
    world.set_rule(world.get_location("Volcanic Glacier - Bronze Photo"), photos)
    world.set_rule(world.get_location("Volcanic Glacier - Silver Photo"), photos)
    world.set_rule(world.get_location("Volcanic Glacier - Gold Photo"), photos)

    recyclingbase = tier2 & (
        HasAll(
            "Volcanic Glacier - Airship",
            "Volcanic Glacier - Recycler Station",
            "Volcanic Glacier - Recycling Beacon",
        ) |
        Has("Volcanic Glacier - Recycling Silo")
    )
    recyclingfull = recyclingbase & HasAll(
        "Volcanic Glacier - Airship",
        "Volcanic Glacier - Recycler Station",
        "Volcanic Glacier - Recycling Beacon",
        "Volcanic Glacier - Recycling Silo",
        "Volcanic Glacier - Rock Hopper",
    )

    world.set_rule(world.get_location("Volcanic Glacier - First Recycling"), recyclingbase)
    world.set_rule(world.get_location("Volcanic Glacier - Recycling Completed"), recyclingfull)

    world.set_rule(world.get_location("Volcanic Glacier - Liftoff"), photos & recyclingfull)

    if world.options.climate_goals:
        humidity = energy & HasAll("Volcanic Glacier - Cloud Seeder", "Volcanic Glacier - Dehumidifier")
        temperature = energy & greenery & HasAll("Volcanic Glacier - Combustor", "Volcanic Glacier - Flash Freezer")
        radiation = greenery

        world.set_rule(world.get_location("Volcanic Glacier - Snow Melts"), temperature)
        world.set_rule(world.get_location("Volcanic Glacier - Fungi In Forests"), humidity)
        world.set_rule(world.get_location("Volcanic Glacier - Pelagic Fish"), radiation)
        world.set_rule(world.get_location("Volcanic Glacier - Aurora"), radiation)
        world.set_rule(world.get_location("Volcanic Glacier - Migratory Birds Return"), temperature & radiation)
        world.set_rule(world.get_location("Volcanic Glacier - Icebergs Form"), temperature & radiation)
        world.set_rule(world.get_location("Volcanic Glacier - Butterflies"), temperature & radiation)
        world.set_rule(world.get_location("Volcanic Glacier - Moss On Boulders"), humidity & temperature)
        world.set_rule(world.get_location("Volcanic Glacier - Ivy Overgrowth"), humidity & temperature)
        world.set_rule(world.get_location("Volcanic Glacier - Moss On Rock Faces"), humidity & temperature)
        world.set_rule(world.get_location("Volcanic Glacier - Snowfall Begins"), humidity & temperature & radiation)

def set_completion_condition(world: TerraNilWorld) -> None:
    world.set_completion_rule(HasFromListUnique(
        *[f"{level} - Liftoff" for level in levels],
        count = world.options.levels_cleared_to_goal.value
    ))
