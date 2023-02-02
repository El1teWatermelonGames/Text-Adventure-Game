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
        "healing": 2
    }
}

class player:
    def loadData(self, playerDataDict) -> None:
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
            "\nWeapon    %s" % self.weapon,
            "\nArmor     %s" % self.armor,
            "\nEXP       %s" % self.exp,
            "\nLV        %s" % self.lv,
            "\nLocation  %s" % self.curloc,
            "\n\nDespite everything, it's still you\n"
        )

    def openInventory(self) -> None:
        print("\nType a command then the item you want to affect")
        print("Commands: c - Check item | u - Use item | d - Discard item | q - Close inventory")
        print("\n".join(self.inventory))

def entry(worldName, playerDict):
    player.loadData(player, playerDict)