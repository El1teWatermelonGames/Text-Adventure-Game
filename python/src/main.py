# Code by Elite Watermelon Games


# External dependencies


# Internal dependencies
from global_constants import clearConsole
from save_load import newSave, loadPlayerData, showSaves, showWorlds
from engine import entry


# Initialization
clearConsole()


class playerSave:
    def init(self) -> None:
        self.name = None
        self.health = None
        self.weapon = None
        self.armor = None
        self.inventory = None
        self.exp = None
        self.lv = None
        self.curloc = None

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

    def load(self, name) -> None:
        playerDict = loadPlayerData(name)
        self.name = playerDict["name"]
        self.health = playerDict["health"]
        self.weapon = playerDict["weapon"]
        self.armor = playerDict["armor"]
        self.inventory = playerDict["inventory"]
        self.exp = playerDict["exp"]
        self.lv = playerDict["lv"]
        self.curloc = playerDict["curloc"]

    def exportDataToDict(self) -> dict:
        return {
            "name": self.name,
            "health": self.health,
            "weapon": self.weapon,
            "armor": self.armor,
            "inventory": self.inventory,
            "exp": self.exp,
            "lv": self.lv,
            "curloc": self.curloc
        }


def main(saveDataSelected = False):
    while(True):
        if saveDataSelected: print("Current save selected: %s" % playerSave.name)
        print("Would you like to:\nq. Exit the game\n1. Create a save\n2. Load a save")
        if saveDataSelected: print("3. Check current save\n4. Start Game")
        selection = input("\n")

        if selection == "q":
            exit(0)

        elif selection == "1":
            name = input("Name your character: ")
            newSave(name)
            playerSave.load(playerSave, name)
            clearConsole()

        elif selection == "2":
            showSaves()
            dataName = input("\nEnter the name of the save file you want to use: ")
            playerSave.load(playerSave, dataName)
            clearConsole()

        elif saveDataSelected and selection == "3":
            clearConsole()
            playerSave.check(playerSave)

        elif saveDataSelected and selection == "4":
            showWorlds()
            worldName = input("\nEnter the name of the world you want to play: ")
            entry(worldName, playerSave.exportDataToDict(playerSave))
        
        if playerSave.name != None: saveDataSelected = True


if __name__ == "__main__":
    playerSave.init(playerSave)
    main()