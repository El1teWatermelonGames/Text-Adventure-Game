from os import path, mkdir, scandir
from json import dumps, loads
from global_constants import COLOR
saveDir = "saves/"
fileExt = "_save.json"
if not path.exists(saveDir):
    mkdir(saveDir)

def newSave(name) -> int:
    saveName = saveDir + name + fileExt
    if path.exists(saveName):
        while True:
            selection = input(COLOR["red"] + f"Save data with this name ({name}) already exists, do you want to overwrite it (y/n): " + COLOR["reset"]).lower().strip(' ')
            if selection == "y":
                break
            elif selection == "n":
                return 1

    saveDict = {
        "name": name,
        "health": 20,
        "weapon": "Stick",
        "armor": "Fabric",
        "inventory": [],
        "exp": 0,
        "lv": 0,
        "curloc": "unassigned"
    }

    data = dumps(saveDict, indent=2)
    with open(saveName, "w") as save:
        save.write(data)
    return 0

def savePlayerData(p) -> int:
    saveName = saveDir + p.name + fileExt
    saveDict = {
        "name": p.name,
        "health": p.health,
        "weapon": p.weapon,
        "armor": p.armor,
        "inventory": p.inventory,
        "exp": p.exp,
        "lv": p.level,
        "curloc": p.curl
    }

    data = dumps(saveDict, indent=2)
    with open(saveName, "w") as save:
        save.write(data)
    return 0

def loadPlayerData(name) -> dict:
    saveName = saveDir + name + fileExt
    try:
        with open(saveName, "r") as save:
            saveDict = loads(' '.join(save.readlines()).replace("\n", ""))
    except FileNotFoundError:
        print(COLOR["red"] + "There is not a save file with this name!" + COLOR["reset"])
    except:
        print(COLOR["red"] + "This save file is not valid!" + COLOR["reset"])
    return saveDict

def showSaves() -> None:
    print("Listed below are all your saves:")
    numOfValidSaves = 0
    for path in scandir(saveDir):
        if path.is_file() and path.name.endswith("_save.json"):
            numOfValidSaves += 1
            print(COLOR["blue"] + path.name.rstrip("_save.json") + COLOR["reset"])
    if numOfValidSaves == 0:
        print(COLOR["red"]+"No saves found!"+COLOR["reset"])