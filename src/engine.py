from importlib.machinery import SourceFileLoader

from global_constants import COLOR, clearConsole
from lookup import items, levelInfo
from save_load import modLoader

class player:
    name = None
    health = None
    weapon = None
    armor = None
    inventory = None
    exp = None
    lv = None
    curloc = None

    def loadData(playerDataDict: dict) -> None:
        player.name = playerDataDict["name"]
        player.health = playerDataDict["health"]
        player.weapon = playerDataDict["weapon"]
        player.armor = playerDataDict["armor"]
        player.inventory = playerDataDict["inventory"]
        player.exp = playerDataDict["exp"]
        player.lv = playerDataDict["lv"]
        player.curloc = playerDataDict["curloc"]

    def check() -> None:
        print(
            "\nName      %s" % player.name,
            "\nHealth    %s" % player.health,
            "\nWeapon    %s" % player.weapon["Name"],
            "\nArmor     %s" % player.armor["Name"],
            "\nEXP       %s" % player.exp,
            "\nLV        %s" % player.lv["level"],
            "\nLocation  %s" % player.curloc,
        )
        if player.lv["level"] == 0 and player.lv["level"] < 10:
            print("\nIt's you\n\n")
        elif player.lv["level"] >= 10 and player.lv["level"] < 15:
            print("\nDespite everything, it's still you\n")
        elif player.lv["level"] >= 15 and player.lv["level"] < 20:
            print("\nEvery scar is a medal to your soul\n")
        elif player.lv["level"] == 20:
            print("\nHold your head high, Reach for the sky, Never surrender\n")

    def openInventory() -> None:
        while(True):
            print("Type a command then the item you want to affect")
            print("Commands: c - Check item | u - Use item | d - Discard item | q - Close inventory")
            for item in player.inventory:
                print(item["Name"])
            selection = str(input("\n"))
            command = selection.split(' ')[0]
            if command == 'q':
                break
            itemSelection = selection.split(' ')[1]
            selectedItem = items.get(itemSelection)

            if selectedItem not in player.inventory:
                clearConsole()
                print(COLOR["red"] + f"You don't have this item ({itemSelection})!" + COLOR["reset"])
            elif command == 'c':
                clearConsole()
                print(selectedItem["Name"] + " - " + selectedItem["Description"])
                if selectedItem["Category"] == "weapon":
                    print("Attack: ", selectedItem["Attack"])
                elif selectedItem["Category"] == "armor":
                    print("Defense: ", selectedItem["Defense"])
                elif selectedItem["Category"] == "consumable":
                    print("Health: ", selectedItem["Health"])
                print()
            elif command == 'u':
                pass
            elif command == 'd':
                clearConsole()
                player.inventory.remove(selectedItem)

    def expEarn(exp: int):
        player.exp += exp

        for i in range(0, len(levelInfo)):
            if exp >= 1450:
                player.lv = levelInfo[20]
                break

            if exp < levelInfo[i]["requiredExp"]:
                player.lv = levelInfo[i - 1]
                break

    def changeWeapon(newWeapon: dict):
        player.inventory.append(player.weapon)
        player.weapon = newWeapon
        player.inventory.remove(newWeapon)

    def changeArmor(newArmor: dict):
        player.inventory.append(player.armor)
        player.armor = newArmor
        player.inventory.remove(newArmor)

    def giveItem(itemName: str):
        player.inventory.append(items[itemName])

    def removeItem(itemName: str):
        player.inventory.remove(items[itemName])
        
def checkLocationsSUID(world, playerLocationSUID: str) -> bool:
    for location in world.locations:
        if location["SUID"] == playerLocationSUID:
            return True
    return False

def entry(worldName: str, playerDict: dict):
    clearConsole()
    player.loadData(playerDict)
    world = SourceFileLoader("world", "worlds/%s" % worldName + "_world.py").load_module()
    
    if player.curloc["SUID"] == "64:0000-0000-0000-0000" or not checkLocationsSUID(world, player.curloc["SUID"]):
        player.curloc = world.startLocation