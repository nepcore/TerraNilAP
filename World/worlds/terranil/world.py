from collections.abc import Mapping
from typing import Any
from worlds.AutoWorld import World
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
        return self.options.as_dict("climate_goals")
