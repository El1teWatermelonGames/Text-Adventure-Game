from os import path, mkdir, scandir
from json import dumps, loads
from global_constants import COLOR
from lookup import items, levelInfo
saveDir = "saves/"
saveExt = "_save.json"
worldDir = "worlds/"
worldExt = "_world.py"
modDir = "mods/"
modExt = "_mod.json"
if not path.exists(saveDir):
    mkdir(saveDir)
if not path.exists(worldDir):
    mkdir(worldDir)
if not path.exists(modDir):
    mkdir(modDir)

def newSave(name: str) -> int:
    saveName = saveDir + name + saveExt
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
        "weapon": items["Stick"],
        "armor": items["Fabric"],
        "inventory": [],
        "exp": 0,
        "lv": levelInfo[0],
        "curloc": "unassigned"
    }

    data = dumps(saveDict, indent=2)
    with open(saveName, "w") as save:
        save.write(data)
    return 0

def savePlayerData(p: dict) -> int:
    saveName = saveDir + p.name + saveExt
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

def loadPlayerData(name: str) -> dict:
    saveName = saveDir + name + saveExt
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
        if path.is_file() and path.name.endswith(saveExt):
            numOfValidSaves += 1
            print(COLOR["blue"] + path.name.rstrip(saveExt) + COLOR["reset"])
    if numOfValidSaves == 0:
        print(COLOR["red"]+"No saves found!"+COLOR["reset"])

def showWorlds() -> None:
    print("Listed below are all your installed worlds:")
    numofValidWorlds = 0
    for path in scandir(worldDir):
        if path.is_file() and path.name.endswith(worldExt):
            numofValidWorlds += 1
            print(COLOR["blue"] + path.name.rstrip(worldExt) + COLOR["reset"])
    if numofValidWorlds == 0:
        print(COLOR["red"]+"No worlds found!"+COLOR["reset"])

def showMods() -> None:
    numofValidMods = 0
    modNames = []
    for path in scandir(modDir):
        if path.is_file() and path.name.endswith(modExt):
            numofValidMods += 1
            modNames.append(COLOR["blue"] + path.name.rstrip(modExt) + COLOR["reset"])
    if numofValidMods == 0:
        print(COLOR["red"] + "No mods are installed!\n" + COLOR["reset"])
        return 0
    print("Listed below are all your installed mods:")
    for modName in modNames:
        print(modName)
    print()

def modLoader() -> None:
    for path in scandir(modDir):
        if path.is_file() and path.name.endswith(modExt):
            with open(modDir + path.name, "r") as modFile:
                modDict = loads(' '.join(modFile.readlines()).replace("\n", ""))

            # Load items
            modItems = loads(dumps(modDict["items"]))
            print(modItems)
            for modItem in modItems.items():
                modItem = ''.join(map(str, modItem))
                for i in range(len(modItem)):
                    if modItem[i] == '{':
                        modItem = modItem[i:]
                        break
                modItemDict = loads(modItem.replace('\'', '"'))
                print(type(modItem), "\n", modItem)
                items[modItemDict["Name"]] = modItemDict

    modItemOutput = open("mods/itemsLog.txt", "w")
    modItemOutput.write(dumps(items, indent=4))
    modItemOutput.close()