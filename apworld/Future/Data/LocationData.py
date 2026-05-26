# Imports
## TODO: Make Relative
from dataclasses import dataclass
from .MapData import map_displayname_to_data

## Map specific location data. Name might need rework.
@dataclass
class MapLocationData:
    map_name: str #The name of the map
    
    biome_names_id_dict: dict[str, int] # A list of names and given AP ids of all the biomes (is that what they're called?) of the map.
    
    climate_goal_names_list: list[str]
    
    has_ocean: bool = False     # True if the region has a location because of poluted ocean
    has_river: bool = False     # True if the region has a location for rivers
    has_lava: bool = False      # True if the region has a location for lava
    has_fire: bool = False      # True if the region has a location for burning
    has_rocket: bool = False    # True if there are goals for the rocket; i.e., flooded city and the other one in the arid region.
    
    
    def __post_init__(self):
        self.map_id_full: int = (1 << 31) | (map_displayname_to_data[self.map_name].InternalID << 12)
        self.generate_all_locations()
        map_locationdata_name_to_data[self.map_name] = self
    
    ## TODO: Update IDs here and in the client
    def generate_tier1_locations(self) -> None:
        """
        Generate all the locations for the first tier of a map.
        These are:
        
        - First energy
        - First removed pollution
        - First greenery
        - Greenery goals, 4 per level
        - First water, if the location has water
        - First lava, if the location has lava
        - First ocean, if the location has ocean
        """
        self.tier1_location_name_to_id: dict[str, int] = {}
        
        self.tier1_location_name_to_id |= {f"{self.map_name} - Energy": (self.map_id_full | 1)}
        self.tier1_location_name_to_id |= {f"{self.map_name} - Pollution Removed": (self.map_id_full | 2)}
        self.tier1_location_name_to_id |= {f"{self.map_name} - Greenery Begin": (self.map_id_full | 3)}
        
        if self.has_river:
            self.tier1_location_name_to_id |= {f"{self.map_name} - River": (self.map_id_full | 4)}
        
        if self.has_ocean:
            self.tier1_location_name_to_id |= {f"{self.map_name} - Ocean Pollution Removed": (self.map_id_full | 9)}
        
        if self.has_lava:
            self.tier1_location_name_to_id |= {f"{self.map_name} - Lava": (self.map_id_full | 9)}
        
        for i in range(4):
            self.tier1_location_name_to_id |= {f"{self.map_name} - Greenery {((i+1)*100)//4}%": (self.map_id_full | 5 + i)}
        
        return



    def generate_tier2_locations(self) -> None:
        """
        Generate all the locations for the second tier of a map.
        These are:
        
        - Biome goals, one for starting the biome and one for completing it.
        - First fire, if the location has fire
        """
        self.tier2_location_name_to_id: dict[str, int] = {}
        
        for biome_name, biome_givenid in self.biome_names_id_dict.items():
            self.tier2_location_name_to_id |= {f"{self.map_name} - {biome_name} Begun" :      self.map_id_full | biome_givenid + 10}
            self.tier2_location_name_to_id |= {f"{self.map_name} - {biome_name} Completed" :  self.map_id_full | biome_givenid + 10}
        
        if self.has_fire:
            self.tier2_location_name_to_id |= {f"{self.map_name} - Fire" : self.map_id_full | 13}

        return



    def generate_tier3_locations(self) -> None:
        """
        Generate all the locations for the final tier of a map.
        These are:
        
        - Recycling goals, amount set by player
        - Photo star goals, amount set by player
        - Photo quality goals
        """
        self.tier3_location_name_to_id: dict[str, int] = {}
        
        self.tier3_location_name_to_id |= {f"{self.map_name} - Recycling Begins" :    self.map_id_full | 20}
        self.tier3_location_name_to_id |= {f"{self.map_name} - Recycling Completed" : self.map_id_full | 21}

        self.tier3_location_name_to_id |= {f"{self.map_name} - Photo Stars 3" : self.map_id_full | 22}
        self.tier3_location_name_to_id |= {f"{self.map_name} - Photo Stars 10" : self.map_id_full | 23}
        
        self.tier3_location_name_to_id |= {f"{self.map_name} - Photo Quality Bronze" : self.map_id_full | 100}
        self.tier3_location_name_to_id |= {f"{self.map_name} - Photo Quality Silver" : self.map_id_full | 101}
        self.tier3_location_name_to_id |= {f"{self.map_name} - Photo Quality Gold"   : self.map_id_full | 102}
        
        return



    def generate_climate_locations(self) -> None:
        """
        Generate all the locations for the climate goals of a map.
        These are:
        
        - Climate Goals
        """
        self.climategoals_location_name_to_id: dict[str, int] = {}
        
        for i, climate_challenge_name in enumerate(self.climate_goal_names_list):
            self.climategoals_location_name_to_id |= {
                f"{self.map_name} - Climate - {climate_challenge_name}" : self.map_id_full | (i + 30)
            }
        
        return



    def generate_all_locations(self) -> None:
        """
        Generate ALL the locations for ALL goals of a map.
        These are:
        
        - Tier 1 goals:
            - First energy
            - First removed pollution
            - First greenery
            - Greenery goals, 4 per level
            - First water, if the location has water
            - First lava, if the location has lava
            - First ocean, if the location has ocean
            
        - Tier 2 goals:
            - Biome goals, one for starting the biome and one for completing it.
            - First fire, if the location has fire

        - Tier 3 goals:
            - Recycling goals, amount set by player
            - Photo star goals, amount set by player
            - Photo quality goals
        
        - Climate Goals
        """
        self.generate_tier1_locations()
        self.generate_tier2_locations()
        self.generate_tier3_locations()
        self.generate_climate_locations()
        
        self.location_tier_to_name_to_id: dict[str, dict[str, int]] = {
                "Tier 1": self.tier1_location_name_to_id, 
                "Tier 2": self.tier2_location_name_to_id, 
                "Tier 3": self.tier3_location_name_to_id, 
                "Climate Goals": self.climategoals_location_name_to_id
            }

        return
    
    
    
    def get_location_tier_to_name_to_id(self):
        return self.location_tier_to_name_to_id
    


map_locationdata_name_to_data: dict[str, MapLocationData] = {}



RiverValleyLocationData =       MapLocationData("River Valley", 
                                    biome_names_id_dict = {"Wetlands": 0, "Fynbos": 1, "Forest": 2}, 
                                    climate_goal_names_list = ["Waterlillies Blossom", "Migratory Birds Return", "Ferns On Riverbanks", "Fungi In Forests", "Rains Begin", "Wildflower Blooms", "Salmon Run"], 
                                    has_river = True,
                                    has_fire = True
                                )

AbandonedQuarryLocationData =   MapLocationData("Abandoned Quarry", 
                                    biome_names_id_dict = {"Wetlands": 0, "Fynbos": 1, "Forest": 2}, 
                                    climate_goal_names_list = ["Wildflower Bloom", "Migratory Birds Return", "Fungi In Forests", "Ferns On Riverbanks", "Waterlilies Blossom", "Salmon Run", "Rains Begin"], 
                                    has_river = True,
                                    has_lava = True,
                                    has_fire = True
                                )

PollutedBayLocationData =       MapLocationData("Polluted Bay", 
                                    biome_names_id_dict = {"Wetlands": 0, "Fynbos": 1, "Forest": 2}, 
                                    climate_goal_names_list = ["Wildflower Bloom", "Migratory Birds Return", "Fungi In Forests", "Ferns On Riverbanks", "Cliff Foiliage", "Waterlilies Blossom", "Salmon Run", "Vegetation Boom", "Rains Begin"], 
                                    has_river = True,
                                    has_fire = True
                                )

HillAndDaleLocationData =       MapLocationData("Hill and Dale", 
                                    biome_names_id_dict = {"Wetlands": 0, "Fynbos": 1, "Forest": 2, "Rocky Shrublands": 3}, 
                                    climate_goal_names_list = ["Wildflower Bloom", "Migratory Birds Return", "Fungi In Forests", "Ferns On Riverbanks", "Waterlilies Blossom", "Salmon Run", "Rains Begin"], 
                                    has_river = True,
                                    has_fire = True
                                )

DesolateIslandLocationData =    MapLocationData("Desolate Island", 
                                    biome_names_id_dict = {"Mangrove": 0, "Tropical Forest": 1, "Beach": 2, "Coral Reef": 3}, 
                                    climate_goal_names_list = ["Moss On Rock Faces", "Migratory Birds Return", "Crabs Populate Beaches", "Coconut Palms", "Dragonflies", "Jellyfish Return", "Ferns On Riverbanks", "Ivy Overgrowth", "Vines Grow", "Waterlilies Blossom", "Thunderstorms Begin"], 
                                    has_river = True,
                                    has_ocean = True
                                )

ScorchedCalderaLocationData =   MapLocationData("Scorched Caldera", 
                                    biome_names_id_dict = {"Bamboo": 0, "Lake Vegetation": 1, "Tropical Forest": 2, "Coral Reef": 3}, 
                                    climate_goal_names_list = ["Ivy Overgrowth", "Migratory Birds Return", "Ferns on Riverbanks", "Vines Grow", "Waterlilies Blossom", "Dragonflies", "Cloud Forests", "Moss on Rock Faces", "Thunderstorms Begin"], 
                                    has_river = False, # Because the lake is just a consequence of rain, I feel like adding river to this feel unneeded. If we want to change this we do need to modify the generator code to change it so it is based on tier rather than just true/false -Lily
                                    has_lava = True,
                                    has_ocean = False
                                )

VolcanicGlacierLocationData =   MapLocationData("Volcanic Glacier", 
                                    biome_names_id_dict = {"Tundra": 0, "Forest": 1, "Lichen": 2, "Kelp Forest": 3}, 
                                    climate_goal_names_list = ["Snow Melts", "Fungi in Forests", "Icebergs Form", "Moss on Boulders", "Ivy Overgrowth", "Butterflies", "Migratory Birds Return", "Moss on Rock Faces", "Pelagic Fish", "Snowfall Begins", "Aurora"], 
                                    has_lava = True,
                                    has_ocean = True,
                                    has_fire = True
                                )



def main():
    for i in map_locationdata_name_to_data.items():
        print(i)
        print()

if __name__ == "__main__":
    main()