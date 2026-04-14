from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld
from .options import option_groups, option_presets

class TerraNilWebWorld(WebWorld):
    game = "TerraNil"
    theme = "grassFlowers"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Terra Nil for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["nepcore"]
    )
    tutorials = [setup_en]
    option_groupd = option_groups
    options_presets = option_presets
