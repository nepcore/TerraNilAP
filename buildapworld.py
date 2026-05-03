import shutil
import os
        

print("Building apworld...")
        
if os.path.exists("TerraNil"):
    print("TerraNil folder already exists. Overwrite?")
    if input("Type Y to overwrite: ").upper() != "Y":
        print("Aborted.")
        exit()
    else: 
        shutil.rmtree("TerraNil")

if os.path.exists("TerraNilZipArchive.zip"):
    print("TerraNilZipArchive.zip already exists. Overwrite?")
    if input("Type Y to overwrite: ").upper() != "Y":
        print("Aborted.")
        exit()

if os.path.exists("TerraNil.apworld"):
    print("TerraNil.apworld already exists. Overwrite?")
    if input("Type Y to overwrite: ").upper() != "Y":
        print("Aborted.")
        exit()
        
try:
    shutil.copytree("apworld", "TerraNil/TerraNil")
except FileNotFoundError:
    raise FileNotFoundError("Could not find the apworld folder. Make sure this script is running from the root directory and the apworld folder exists.")

new_zip = shutil.make_archive("TerraNilZipArchive", "zip", "TerraNil")

shutil.move(new_zip, "TerraNil.apworld")

shutil.rmtree("TerraNil")

print("Done!")


