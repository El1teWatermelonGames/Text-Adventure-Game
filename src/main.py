# Internal dependencies
from global_constants import clearConsole, COLOR
from save_load import newSave, loadPlayerData, showSaves, showWorlds, showMods, modLoader
from engine import entry

# Initialization
clearConsole()

class playerSave:
    name = None
    health = None
    weapon = None
    armor = None
    inventory = None
    exp = None
    lv = None
    curloc = None

    def check() -> None:
        print(
            "\nName      %s" % playerSave.name,
            "\nHealth    %s" % playerSave.health,
            "\nWeapon    %s" % playerSave.weapon["Name"],
            "\nArmor     %s" % playerSave.armor["Name"],
            "\nEXP       %s" % playerSave.exp,
            "\nLV        %s" % playerSave.lv["level"],
            "\nLocation  %s" % playerSave.curloc,
        )
        if playerSave.lv["level"] == 0 and playerSave.lv["level"] < 10:
            print("\nIt's you\n\n")
        elif playerSave.lv["level"] >= 10 and playerSave.lv["level"] < 15:
            print("\nDespite everything, it's still you\n")
        elif playerSave.lv["level"] >= 15 and playerSave.lv["level"] < 20:
            print("\nEvery scar is a medal to your soul\n")
        elif playerSave.lv["level"] == 20:
            print("\nHold your head high, Reach for the sky, Never surrender\n")

    def load(name: str) -> None:
        playerDict = loadPlayerData(name)
        playerSave.name = playerDict["name"]
        playerSave.health = playerDict["health"]
        playerSave.weapon = playerDict["weapon"]
        playerSave.armor = playerDict["armor"]
        playerSave.inventory = playerDict["inventory"]
        playerSave.exp = playerDict["exp"]
        playerSave.lv = playerDict["lv"]
        playerSave.curloc = playerDict["curloc"]

    def exportDataToDict() -> dict:
        return {
            "name": playerSave.name,
            "health": playerSave.health,
            "weapon": playerSave.weapon,
            "armor": playerSave.armor,
            "inventory": playerSave.inventory,
            "exp": playerSave.exp,
            "lv": playerSave.lv,
            "curloc": playerSave.curloc
        }

def TEST_MENU():
    print(COLOR["magenta"])

    while(True):
        selection = input()

        if selection == "q": break

    print(COLOR["reset"])
    clearConsole()

def main(saveDataSelected = False):
    while(True):
        if saveDataSelected: print("Current save selected: %s" % playerSave.name)
        print("Would you like to:\nq. Exit the game\n1. Create a save\n2. Load a save\n3. Show Installed Mods")
        if saveDataSelected: print("4. Check current save\n5. Start Game")
        selection = input("\n")

        if selection == "q":
            exit(0)

        elif selection == "1":
            name = input("Name your character: ")
            newSave(name)
            playerSave.load(name)
            clearConsole()

        elif selection == "2":
            showSaves()
            dataName = input("\nEnter the name of the save file you want to use: ")
            playerSave.load(dataName)
            clearConsole()

        elif selection == "3":
            clearConsole()
            showMods()

        elif saveDataSelected and selection == "4":
            clearConsole()
            playerSave.check()

        elif saveDataSelected and selection == "5":
            showWorlds()
            worldName = input("\nEnter the name of the world you want to play: ")
            entry(worldName, playerSave.exportDataToDict())

        elif selection == "TEST_MENU":
            TEST_MENU()
        
        if playerSave.name != None: saveDataSelected = True


if __name__ == "__main__":
    status:tuple = modLoader()
    if not status[0] == 0:
        print(COLOR["red"] + status[1] + COLOR["reset"])
        exit(status[0])
    main()