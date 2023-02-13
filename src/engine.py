from global_constants import COLOR, clearConsole
from sfx import audio
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

# Lvl up formula: (Last Level + Next Level) * 20 * Current Skill Multiplier
# This could probably be more efficient & will likely end up on r/badcode if anyone finds it
levelInfo = {
    0: {
        "level": 0,
        "requiredExp": 0,
        "health": 20,
        "skillMultiplier": 1
    },
    1: {
        "level": 1,
        "requiredExp": 63,
        "health": 22,
        "skillMultiplier": 1.05
    },
    2: {
        "level": 2,
        "requiredExp": 173,
        "health": 25,
        "skillMultiplier": 1.1
    },
    3: {
        "level": 3,
        "requiredExp": 334,
        "health": 29,
        "skillMultiplier": 1.15
    },
    4: {
        "level": 4,
        "requiredExp": 550,
        "health": 34,
        "skillMultiplier": 1.2
    },
    5: {
        "level": 5,
        "requiredExp": 825,
        "health": 40,
        "skillMultiplier": 1.25
    },
    6: {
        "level": 6,
        "requiredExp": 1163,
        "health": 47,
        "skillMultiplier": 1.3
    },
    7: {
        "level": 7,
        "requiredExp": 1568,
        "health": 55,
        "skillMultiplier": 1.35
    },
    8: {
        "level": 8,
        "requiredExp": 2044,
        "health": 64,
        "skillMultiplier": 1.4
    },
    9: {
        "level": 9,
        "requiredExp": 2595,
        "health": 74,
        "skillMultiplier": 1.45
    },
    10: {
        "level": 10,
        "requiredExp": 3225,
        "health": 85,
        "skillMultiplier": 1.5
    },
    11: {
        "level": 11,
        "requiredExp": 3938,
        "health": 97,
        "skillMultiplier": 1.55
    },
    12: {
        "level": 12,
        "requiredExp": 4738,
        "health": 110,
        "skillMultiplier": 1.6
    },
    13: {
        "level": 13,
        "requiredExp": 5629,
        "health": 124,
        "skillMultiplier": 1.65
    },
    14: {
        "level": 14,
        "requiredExp": 6615,
        "health": 139,
        "skillMultiplier": 1.7
    },
    15: {
        "level": 15,
        "requiredExp": 7700,
        "health": 155,
        "skillMultiplier": 1.75
    },
    16: {
        "level": 16,
        "requiredExp": 8888, # Google's DNS address, odd coincidence
        "health": 172,
        "skillMultiplier": 1.8
    },
    17: {
        "level": 17,
        "requiredExp": 10183,
        "health": 190,
        "skillMultiplier": 1.85
    },
    18: {
        "level": 18,
        "requiredExp": 11589,
        "health": 209,
        "skillMultiplier": 1.9
    },
    19: {
        "level": 19,
        "requiredExp": 13110,
        "health": 229,
        "skillMultiplier": 1.95
    },
    20: {
        "level": 20,
        "requiredExp": 14750,
        "health": 250,
        "skillMultiplier": 2
    }
}

def modLoader() -> int:
    if not path.exists(modsDir):
        return 1
    # Load extra items from a .json file & add them to the items dictionary
    # Load extra sound effects from a .json file & add them to sfx.audio.clips
    # Load extra music tracks from a .json file & add them to [WIP]

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
            audio.playAudio(audio.clip["menuSelection"])
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
        

def entry(worldName, playerDict: dict):
    clearConsole()
    player.loadData(player, playerDict)
    modLoader()

    
    player.inventory.append(items["Apple"])
    player.inventory.append(items["Stick"])
    player.inventory.append(items["Fabric"])
    player.expEarn(player, 50000)
    player.check(player)
    input()
    player.openInventory(player)