from collections.abc import Mapping
from typing import Any
from worlds.AutoWorld import World  #type: ignore
from . import items, locations, regions, rules, web_world
from . import options as terranil_options

class TerraNilWorld(World):
    """Terra Nil is an intricate environmental strategy game about transforming a barren wasteland into a thriving, balanced ecosystem."""

    game = "TerraNil"

    web = web_world.TerraNilWebWorld()

    options_dataclass = terranil_options.TerraNilOptions
    options: terranil_options.TerraNilOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Menu"

    ut_can_gen_without_yaml = True

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.TerraNilItem:
        return items.create_item(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        data = self.options.as_dict("climate_goals", "levels_cleared_to_goal", "game_difficulty")
        data["starting_level"] = self.starting_level
        return data

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data

    def generate_early(self) -> None:
        # if in ut get options from slot data
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            print("received passthrough")
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]
            for key, value in slot_data.items():
                if key == "starting_level":
                    value = value.lower().replace(" ", "_")
                opt: Optional[Option] = getattr(self.options, key, None)
                if opt is not None:
                    setattr(self.options, key, opt.from_any(value))

        temperate = ["River Valley", "Hill and Dale", "Polluted Bay", "Abandoned Quarry"]
        tropical = ["Desolate Island", "Scorched Caldera"]
        polar = ["Volcanic Glacier"]

        starting_level = self.options.starting_level.current_option_name
        if self.options.starting_level == "any":
            starting_level = self.random.choice(temperate + tropical + polar)
        if self.options.starting_level == "random_temperate":
            starting_level = self.random.choice(temperate)
        if self.options.starting_level == "random_tropical":
            starting_level = self.random.choice(tropical)
        if self.options.starting_level == "random_polar":
            starting_level = self.random.choice(polar)
        #if self.options.starting_level == "random_continental":
        #    starting_level = self.random.choice([])
        #if self.options.starting_level == "random_arid":
        #    starting_level = self.random.choice([])

        # option names are converted to title case by core AP
        # so we need to manually make things match sometimes
        if starting_level == "Hill And Dale":
            starting_level = "Hill and Dale"

        self.starting_level = starting_level
