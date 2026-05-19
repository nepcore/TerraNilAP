from dataclasses import dataclass
from Options import PerGameCommonOptions, Toggle, DefaultOnToggle, Range, Choice

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

class StartingLevel(Choice):
    """
    The level you will start with

    The options Temparate, Tropical and Polar pick a random level from the selected region
    """

    display_name = "Starting Level"

    option_any = 0
    option_random_temperate = 1
    option_random_tropical = 2
    option_random_polar = 3
    #option_random_continental = 4
    #option_random_arid = 5

    option_river_valley = 6
    option_hill_and_dale = 7
    option_polluted_bay = 8
    option_abandoned_quarry = 9

    option_desolate_island = 10
    #option_archipelago = 11
    option_scorched_caldera = 12

    option_volcanic_glacier = 13
    #option_polluted_fjord = 14
    #option_subpolar_river = 15

    #option_flooded_city = 16
    #option_irradiated_sprawl = 17
    #option_continental_outskirts = 18

    #option_parched_dunes = 19
    #option_canyon_peaks = 20
    #option_fracked_floodplain = 21

    default = 6

class GameDifficulty(Choice):
    """
    The difficulty you want to play at. This can be changed in the games options menu.

    Monk: Money doesn't exist
    Gardener: Start with 1500 money, buildings cost 50% normal price
    Ecologist: Start with 1000 money, buildings cost normal price
    Environmental Engineer: Start with 1000 money, buildings cost 125% normal price
    """

    option_monk = 0
    option_gardener = 1
    option_ecologist = 2
    option_environmental_engineer = 3

    default = 2

@dataclass
class TerraNilOptions(PerGameCommonOptions):
    rain_logic: RainLogic
    climate_goals: ClimateGoals
    levels_cleared_to_goal: LevelsClearedToGoal
    starting_level: StartingLevel
    game_difficulty: GameDifficulty

option_groups = []
option_presets = {}
