from enum import Enum

class Mission(Enum):
    All = 0, "All"
    RiverValley = 10, "River Valley"

    def __int__(self):
        return self.value[0]

    def __str__(self):
        return self.value[1]
