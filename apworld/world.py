from collections.abc import Mapping
from typing import Any
from worlds.AutoWorld import World  #type: ignore
from . import items, locations, regions, rules, web_world
from . import options as terranil_options
from Options import OptionError

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
        data["levels_enabled"] = self.levels_enabled
        return data

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data

    def generate_early(self) -> None:
        # if in ut get options from slot data
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]
            for key in ["climate_goals", "levels_cleared_to_goal", "game_difficulty"]:
                opt = getattr(self.options, key, None)
                setattr(self.options, key, opt.from_any(slot_data[key]))
            self.starting_level = slot_data["starting_level"]
            self.levels_enabled = slot_data["levels_enabled"]
        else:
            # find which levels are allowed to end up in logic
            available_levels = [level for level, weight in self.options.level_likeliness.value.items() if weight > 0]
            if len(available_levels) == 0:
                raise OptionError("All levels disabled, cannot generate")

            # resolve starting level
            starting_level = self.options.starting_level.current_option_name
            if self.options.starting_level == "any":
                starting_level = self.random.choice(available_levels)

            if self.options.starting_level == "random_temperate":
                options = list(set(["River Valley", "Hill and Dale", "Polluted Bay", "Abandoned Quarry"]) & set(available_levels))
                if len(options) == 0:
                    raise OptionError("No levels from temperate region enabled, cannot pick random temperate starting level")
                starting_level = self.random.choice(options)

            if self.options.starting_level == "random_tropical":
                options = list(set(["Desolate Island", "Scorched Caldera"]) & set(available_levels))
                if len(options) == 0:
                    raise OptionError("No levels from tropical region enabled, cannot pick random tropical starting level")
                starting_level = self.random.choice(options)

            if self.options.starting_level == "random_polar":
                options = list(set(["Volcanic Glacier"]) & set(available_levels))
                if len(options) == 0:
                    raise OptionError("No levels from polar region enabled, cannot pick random polar starting level")
                starting_level = self.random.choice(options)

            #if self.options.starting_level == "random_continental":
            #    options = set([]) & set(available_levels)
            #    if len(options) == 0:
            #        raise OptionError("No levels from continental region enabled, cannot pick random continental starting level")
            #    starting_level = self.random.choice(options)

            #if self.options.starting_level == "random_arid":
            #    options = set([]) & set(available_levels)
            #    if len(options) == 0:
            #        raise OptionError("No levels from arid region enabled, cannot pick random arid starting level")
            #    starting_level = self.random.choice(options)

            # option names are converted to title case by core AP
            # so we need to manually make things match sometimes
            if starting_level == "Hill And Dale":
                starting_level = "Hill and Dale"

            if not starting_level in available_levels:
                raise OptionError(f"Selected starting level '{starting_level}' is disabled")

            self.starting_level = starting_level

            # resolve enabled levels
            level_weights = self.options.level_likeliness.value
            keys = list(level_weights.keys())
            weights = list(level_weights.values())
            max_levels = self.options.number_of_levels
            num_levels = len([w for w in weights if w > 0])
            min_levels = self.options.levels_cleared_to_goal
            if num_levels < min_levels:
                raise OptionError("There must be at least as many levels with a non-zero weight as required to goal")
            if max_levels < min_levels:
                raise OptionError("Maximum number of levels must be at least equal to the number of levels required to goal")
            if num_levels < max_levels:
                self.levels_enabled = available_levels
            else:
                self.levels_enabled = [self.starting_level]
                i = keys.index(starting_level)
                keys.pop(i)
                weights.pop(i)
                for _ in range(min(num_levels, max_levels) - 1): # subtract one to account for the guaranteed enabled starting level
                    choice = self.random.choices(population=keys, weights=weights, k=1)[0]
                    i = keys.index(choice)
                    self.levels_enabled.append(choice)
                    keys.pop(i)
                    weights.pop(i)
