from dataclasses import dataclass
from Options import PerGameCommonOptions, Toggle, DefaultOnToggle

class ClimateGoals(DefaultOnToggle):
    """Adds climate goals as checks"""

    display_name = "Climate Goals"

class RainLogic(Toggle):
    """Allows logic to require using rain for water instead of water pumps"""

    display_name = "Rain Logic"

@dataclass
class TerraNilOptions(PerGameCommonOptions):
    rain_logic: RainLogic
    climate_goals: ClimateGoals

option_groups = []
option_presets = {}
