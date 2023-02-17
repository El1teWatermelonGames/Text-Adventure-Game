from global_constants import COLOR, clearConsole
from os import path
from lookup import items, levelInfo
from save_load import modLoader

modsDir = ("mods/")

class player:
    def loadData(self, playerDataDict: dict) -> None:
        self.name = playerDataDict["name"]
        self.health = playerDataDict["health"]
        self.weapon = playerDataDict["weapon"]
        self.armor = playerDataDict["armor"]
        self.inventory = playerDataDict["inventory"]
        self.exp = playerDataDict["exp"]
        self.lv = playerDataDict["lv"]
        self.curloc = playerDataDict["curloc"]

    def check(self) -> None:
        print(
            "\nName      %s" % self.name,
            "\nHealth    %s" % self.health,
            "\nWeapon    %s" % self.weapon["Name"],
            "\nArmor     %s" % self.armor["Name"],
            "\nEXP       %s" % self.exp,
            "\nLV        %s" % self.lv["level"],
            "\nLocation  %s" % self.curloc,
        )
        if self.lv["level"] == 0 and self.lv["level"] < 10:
            print("\nIt's you\n\n")
        elif self.lv["level"] >= 10 and self.lv["level"] < 15:
            print("\nDespite everything, it's still you\n")
        elif self.lv["level"] >= 15 and self.lv["level"] < 20:
            print("\nEvery scar is a medal to your soul\n")
        elif self.lv["level"] == 20:
            print("\nHold your head high, Reach for the sky, Never surrender\n")

    def openInventory(self) -> None:
        while(True):
            print("Type a command then the item you want to affect")
            print("Commands: c - Check item | u - Use item | d - Discard item | q - Close inventory")
            for item in self.inventory:
                print(item["Name"])
            selection = str(input("\n"))
            command = selection.split(' ')[0]
            if command == 'q':
                break
            itemSelection = selection.split(' ')[1]
            selectedItem = items.get(itemSelection)

            if selectedItem not in self.inventory:
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
                self.inventory.remove(selectedItem)

    def expEarn(self, exp: int):
        self.exp += exp

        for i in range(0, len(levelInfo)):
            if exp >= 1450:
                self.lv = levelInfo[20]
                break

            if exp < levelInfo[i]["requiredExp"]:
                self.lv = levelInfo[i - 1]
                break

    def changeWeapon(self, newWeapon: dict):
        self.inventory.append(self.weapon)
        self.weapon = newWeapon
        self.inventory.remove(newWeapon)

    def changeArmor(self, newArmor: dict):
        self.inventory.append(self.armor)
        self.armor = newArmor
        self.inventory.remove(newArmor)

    def giveItem(self, itemName: str):
        self.inventory.append(items[itemName])

    def removeItem(self, itemName: str):
        self.inventory.remove(items[itemName])
        

def entry(worldName, playerDict: dict):
    clearConsole()
    player.loadData(player, playerDict)
    modLoader()

    input()
    
    player.inventory.append(items["Apple"])
    player.inventory.append(items["Stick"])
    player.inventory.append(items["Fabric"])
    player.expEarn(player, 34)
    player.check(player)
    input()
    player.openInventory(player)