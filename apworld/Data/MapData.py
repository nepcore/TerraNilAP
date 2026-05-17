from dataclasses import dataclass

@dataclass
class TerraNilMapData:
    """
    A dataclass containing the internal name, internal id, displayname as well as the region of a certain map.

    Methods:
    __str__: returns the display name.
    __int__: returns the internal id.
    read_data: returns all the data as a string in a human-readable format.
    as_dict: returns the data as a dictionary
    """
    displayname:  str
    InternalID:   int
    region:       str

    def __str__(self) -> str:
        return self.displayname

    def __int__(self) -> int:
        return self.InternalID

    def read_data(self) -> str:
        "Provides a human-readable oversight of the stored data."
        return f"Map {self.displayname} of region {self.region} with internal ID {self.InternalID}"


RiverValleyData =            TerraNilMapData(displayname = "River Valley",          region = "Temperate", InternalID = 10)
AbandonedQuarryData =        TerraNilMapData(displayname = "Abandoned Quarry",      region = "Temperate", InternalID = 11)
PollutedBayData =            TerraNilMapData(displayname = "Polluted Bay",          region = "Temperate", InternalID = 12)
HillAndDaleData =            TerraNilMapData(displayname = "Hill and Dale",         region = "Temperate", InternalID = 13)

DesolateIslandData =         TerraNilMapData(displayname = "Desolate Island",       region = "Tropical", InternalID = 20)
ArchipelagoData =            TerraNilMapData(displayname = "Archipelago",           region = "Tropical", InternalID = 21)
ScorchedCalderaData =        TerraNilMapData(displayname = "Scorched Caldera",      region = "Tropical", InternalID = 22)

VolcanicGlacierData =        TerraNilMapData(displayname = "Volcanic Glacier",      region = "Polar", InternalID = 30)
PollutedFjordData =          TerraNilMapData(displayname = "Polluted Fjord",        region = "Polar", InternalID = 31)
SubpolarRiverData =          TerraNilMapData(displayname = "Subpolar River",        region = "Polar", InternalID = 32)

FloodedCityData =            TerraNilMapData(displayname = "Flooded City",          region = "Continental", InternalID = 50)
IrradiatedSprawlData =       TerraNilMapData(displayname = "Irradiated Sprawl",     region = "Continental", InternalID = 51)
ContinentalOutskirtsData =   TerraNilMapData(displayname = "Continental Outskirts", region = "Continental", InternalID = 52)

ParchedDunesData =           TerraNilMapData(displayname = "Parched Dunes",         region = "Arid", InternalID = 41)
CanyonPeaksData =            TerraNilMapData(displayname = "Canyon Peaks",          region = "Arid", InternalID = 42)
FrackedFloodplainData =      TerraNilMapData(displayname = "Fracked Floodplain",    region = "Arid", InternalID = 43)


map_displayname_to_data: dict[str, TerraNilMapData] = {
    "River Valley":          RiverValleyData,
    "Abandoned Quarry":      AbandonedQuarryData,
    "Polluted Bay":          PollutedBayData,
    "Hill and Dale":         HillAndDaleData,

    "Desolate Island":       DesolateIslandData,
    # "Archipelago":           ArchipelagoData,
    "Scorched Caldera":      ScorchedCalderaData,

    "Volcanic Glacier":      VolcanicGlacierData,
    # "Polluted Fjord":        PollutedFjordData,
    # "Subpolar River":        SubpolarRiverData,

    # "Flooded City":          FloodedCityData,
    # "Irradiated Sprawl":     IrradiatedSprawlData,
    # "Continental Outskirts": ContinentalOutskirtsData,

    # "Parched Dunes":         ParchedDunesData,
    # "Canyon Peaks":          CanyonPeaksData,
    # "Fracked Floodplain":    FrackedFloodplainData,
}

def get_map_id(map_name: str) -> int:
    "Returns the ID for a given display name for a map."
    return map_displayname_to_data[map_name].InternalID