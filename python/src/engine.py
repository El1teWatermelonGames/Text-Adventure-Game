from global_constants import COLOR, clearConsole
from os import path

modsDir = ("mods/")

items = {
    # ---- Weapons ----
    "Stick": {
        "Name": "Stick",
        "Description": "A pointy stick, not the greatest weapon of all time",
        "Category": "weapon",
        "Attack": 1
    },

    # ---- Armor ----
    "Fabric": {
        "Name": "Fabric",
        "Description": "Thin fabric cloth, poor protection against any weapon",
        "Category": "armor",
        "Defense": 1
    },

    # ---- Misc. ----
    "Apple": {
        "Name": "Apple",
        "Description": "An apple a day keeps the eldritch horrores away",
        "Category": "consumable",
        "Health": 2
    }
}

def modLoader() -> int:
    if not path.exists(modsDir):
        return 1
    # Load extra items from a .json file & add them to the items dictionary

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
            "\nLV        %s" % self.lv,
            "\nLocation  %s" % self.curloc,
        )
        if self.lv >= 0 and self.lv < 5:
            print("\nIt's you\n")
        elif self.lv >= 5 and self.lv < 10:
            print("\nDespite everything, it's still you\n")
        elif self.lv >= 10 and self.lv < 15:
            print("\nEvery scar is a medal to your soul\n")
        elif self.lv >= 15 and self.lv < 20:
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
        pass

def entry(worldName, playerDict: dict):
    clearConsole()
    player.loadData(player, playerDict)
    modLoader()

    
    player.inventory.append(items["Apple"])
    player.inventory.append(items["Stick"])
    player.inventory.append(items["Fabric"])
    player.openInventory(player)