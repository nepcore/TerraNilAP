## Deprecated for Items, still used for Locations.

from enum import Enum

class Mission(Enum):
    All = 0, "All"
    RiverValley = 10, "River Valley"
    DesolateIsland = 20, "Desolate Island"

    def __int__(self):
        return self.value[0]

    def __str__(self):
        return self.value[1]
