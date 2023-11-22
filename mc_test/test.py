import os
import main
import zipfile

APPDATA_PATH = os.getenv("APPDATA")
MC_VERSION = "1.20.3-pre2"
WORLD = "SnapShotTest"
DATAPACK = "datapack_example"

IN_PATH_P1 = f"{APPDATA_PATH}/.minecraft/versions/{MC_VERSION}/{MC_VERSION}"
IN_PATH_COMPLETE = IN_PATH_P1 + "/assets/minecraft/textures/item/"
OUT_PATH = APPDATA_PATH + "/.minecraft/saves/SnapShotTest/datapacks/display/data/minecraft/functions/"

if not os.path.isdir(IN_PATH_P1):
    print(f"Extracting {MC_VERSION}.jar ...")
    zipfile.ZipFile(IN_PATH_P1+".jar").extractall(IN_PATH_P1)
    print("Extracted jar file\n")

for filename in os.listdir(IN_PATH_COMPLETE):
    print(f"Converting "+filename)
    item = filename.split(".")[0]
    main.convert_img(IN_PATH_COMPLETE+item+".png", OUT_PATH+item+".mcfunction")
