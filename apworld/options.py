from dataclasses import dataclass
from Options import PerGameCommonOptions, Toggle, DefaultOnToggle, Range

class ClimateGoals(DefaultOnToggle):
    """Adds climate goals as checks"""

    display_name = "Climate Goals"

class RainLogic(Toggle):
    """Allows logic to require using rain for water instead of water pumps"""

    display_name = "Rain Logic"

class LevelsClearedToGoal(Range):
    """How many levels you need to clear to goal"""

    display_name = "Levels cleared to goal"

    range_start = 1
    range_end = 7
    default = 7

@dataclass
class TerraNilOptions(PerGameCommonOptions):
    rain_logic: RainLogic
    climate_goals: ClimateGoals
    levels_cleared_to_goal: LevelsClearedToGoal

option_groups = []
option_presets = {}
