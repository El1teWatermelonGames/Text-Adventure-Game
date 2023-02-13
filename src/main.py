# Code by Elite Watermelon Games

# External Dependancies
from playsound import playsound

# Internal dependencies
from global_constants import clearConsole, COLOR
from save_load import newSave, loadPlayerData, showSaves, showWorlds
from sfx import audio
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
            "\nWeapon    %s" % self.weapon["Name"],
            "\nArmor     %s" % self.armor["Name"],
            "\nEXP       %s" % self.exp,
            "\nLV        %s" % self.lv,
            "\nLocation  %s" % self.curloc,
        )
        if self.lv >= 0 and self.lv < 5:
            print("\nIt's you\n\n")
        elif self.lv >= 5 and self.lv < 10:
            print("\nDespite everything, it's still you\n")
        elif self.lv >= 10 and self.lv < 15:
            print("\nEvery scar is a medal to your soul\n")
        elif self.lv >= 15 and self.lv < 20:
            print("\nHold your head high, Reach for the sky, Never surrender\n")

    def load(self, name: str) -> None:
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

def TEST_MENU():
    print(COLOR["magenta"])

    while(True):
        selection = input()

        if selection == "q": break
        elif selection == "AUDIO":
            print(COLOR["cyan"])
            while(True):
                clip = input()
                if clip == "q": break
                try: playsound(audio.clip[clip])
                except: clearConsole()
                clearConsole()
            print(COLOR["magenta"])

    print(COLOR["reset"])
    clearConsole()

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

        elif selection == "TEST_MENU":
            TEST_MENU()
        
        if playerSave.name != None: saveDataSelected = True


if __name__ == "__main__":
    playerSave.init(playerSave)
    main()