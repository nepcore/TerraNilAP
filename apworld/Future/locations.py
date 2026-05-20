from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Location
from .Data.LocationData import map_locationdata_name_to_data, MapLocationData
from .items import TerraNilItem
if TYPE_CHECKING:
    from .world import TerraNilWorld

class TerraNilLocation(Location):
    game = "TerraNil"

LOCATION_NAME_TO_ID = {}
for map_name, map_data in map_locationdata_name_to_data.items():
    for tier, name_to_id in map_data.get_location_tier_to_name_to_id().items():
        for name, id in name_to_id.items():
            LOCATION_NAME_TO_ID[name] = id
            

def create_all_locations(world: TerraNilWorld) -> None:
    for map_name, map_data in map_locationdata_name_to_data.items():
        for tier, name_to_id in map_data.get_location_tier_to_name_to_id().items():
            if tier != "Climate Goals": #Is it possible to not generate locationdata for Climate Goals if this option is disabled, saving this workaround?
                world.get_region(f"{map_name} {tier}").add_locations(name_to_id, TerraNilLocation)
            elif world.options.climate_goals:
                world.get_region(f"{map_name} {tier}").add_locations(name_to_id, TerraNilLocation)

    create_events(world)


def create_events(world: TerraNilWorld) -> None:
    for map_name, map_data in map_locationdata_name_to_data.items():
        t1 = world.get_region(f"{map_name} Tier 1")
        t2 = world.get_region(f"{map_name} Tier 2")
        t3 = world.get_region(f"{map_name} Tier 3")
        t1.add_event(
            f"{map_name} - Tier 1 Completed",
            f"{map_name} - Tier 1 Completed",
            location_type=TerraNilLocation,
            item_type=TerraNilItem
        )
        t2.add_event(
            f"{map_name} - Tier 2 Completed",
            f"{map_name} - Tier 2 Completed",
            location_type=TerraNilLocation,
            item_type=TerraNilItem
        )
        t3.add_event(
            f"{map_name} - Liftoff",
            f"{map_name} - Liftoff",
            location_type=TerraNilLocation,
            item_type=TerraNilItem
        )
        

def generate_plaintext_locations(output_file_name: str) -> bool:
    print("Want to generate plaintext locations name?")
    if input("Type Y to continue: ").upper() != "Y":
        print("Aborted.")
        return False
    
    try:
        with open(output_file_name, "x") as output_file:
            for locationname, locationid in LOCATION_NAME_TO_ID.items():
                print(locationname, file = output_file)
        return True
    
    except FileExistsError:
        print("Failed to generate plaintext locations; file already exists.")
        return False
            

def main():
    
    status = generate_plaintext_locations("apworld/Data/List of all Locations.txt")
    if status:
        print("Done!")
    else:
        print("Failed...")
    
        
if __name__ == "__main__":
    main()