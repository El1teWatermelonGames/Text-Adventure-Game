import random
import json
import os

os.system("") # On Windows 10+ colors may not show unless a system() call is made, no clue why but it works so ¯\_(ツ)_/¯
savesDir = "saves/"

COLOR = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "reset": "\u001b[0m"
}

def clearConsole():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
        
class player:
    def editName(self, newName):
        self.name = newName
    
    def changeWeapon(self, weapon):
        pass

    def changeArmour(self, armor):
        pass

    def printData(self):
        print(f"""
        Name      | {self.name}
        Weapon    | {self.weapon}
        Health    | {self.health}
        Armor     | {self.armor}
        Exp       | {self.exp}
        Inventory | {self.inventory}
        Location  | {self.curloc}
        """)

    def saveData(self):
        if os.path.exists(savesDir+self.name+"-save.json"):
            while(True):
                selection = input("Save data with this name already exists, do you want to overwrite it? (y/n): ")
                if selection == "y":
                    break
                elif selection == "n":
                    newSaveMenu()

        playerDat_dict = {
            "name": f"{self.name}",
            "weapon": f"{self.weapon}",
            "health": f"{self.health}",
            "armor": f"{self.armor}",
            "exp": f"{self.exp}",
            "inventory": f"{self.inventory}",
            "curloc": f"{self.curloc}",
        }
        playerDat = json.dumps(playerDat_dict, indent=4)
        playerSave = open(savesDir+self.name+"-save.json", "w")
        playerSave.write(playerDat)
        playerSave.close()

    def loadData(self, name):
        playerSave = open(savesDir+name+"-save.json", "r")
        playerDat = playerSave.readlines()
        playerSave.close()
        playerDat = " ".join(playerDat).replace("\n", "")
        playerDat_dict = json.loads(playerDat)

        self.name = playerDat_dict["name"]
        self.weapon = playerDat_dict["weapon"]
        self.health = playerDat_dict["health"]
        self.armor = playerDat_dict["armor"]
        self.exp = playerDat_dict["exp"]
        self.inventory = playerDat_dict["inventory"]
        self.curloc = playerDat_dict["curloc"]

    def listData():
        print("Listed below are all your current saves:")
        numOfValidSaves = 0
        saves_dir = savesDir
        for path in os.scandir(saves_dir):
            if path.is_file() and path.name.endswith("-save.json"):
                numOfValidSaves += 1
                print(COLOR["blue"]+path.name.rstrip("-save.json")+COLOR["reset"])
        if numOfValidSaves == 0:
            print(COLOR["red"]+""+COLOR["reset"])

    def initiate(self):
        if not os.path.exists(savesDir):
            os.mkdir(savesDir)

        self.name = "Player"
        self.weapon = "Stick"
        self.health = 20
        self.armor = "Fabric"
        self.exp = 0
        self.inventory = []
        self.curloc = "plains"

class enemy:
    def __init__(self, name, description, damage, health, defense, expMin, expMax) -> None:
        self.name = name
        self.description = description
        self.damage = damage
        self.health = health
        self.defense = defense
        self.exp = random.randint(expMin, expMax)

    def printData(self):
        print(f"Name: {self.name}\nDamage: {self.damage}\nHealth: {self.health}\nDefense: {self.defense}\nExp Reward: {self.exp}")


# ---- Commands ----

def commandCheck(userIn):
    if userIn.startswith("/"):
        if userIn == "/q":
            quit(0)
        elif userIn == "/s":
            player.saveData()
        elif userIn == "/l":
            loadSaveMenu()
        elif userIn == "/cp":
            player.printData()

# ---- Menus ----

def loadSaveMenu():
    player.listData()
    dataName = input("\nEnter the name of the save file you want to use: ")
    player.loadData(player, dataName)

def newSaveMenu():
    name = input("Name your character: ")
    player.editName(player, name)
    player.saveData(player)

def init():
    player.initiate(player)
    saveDataSelected = False

    while(True):
        if saveDataSelected: print(f"Current save selected: {player.name}")
        print("Would you like to:\nq. Exit the game\n1. Create a save\n2. Load a save")
        if saveDataSelected: print("3. View current save data\n4. Start Game")
        selection = input("\n")

        if selection == "q":
            exit(0)

        elif selection == "1":
            saveDataSelected = True
            newSaveMenu()

        elif selection == "2":
            saveDataSelected = True
            loadSaveMenu()

        elif saveDataSelected and selection == "3":
            player.printData(player)

        elif saveDataSelected and selection == "4":
            game()

        else:
            print(COLOR["red"]+"Not a valid option!"+COLOR["reset"])

def game():
    pass
    
if __name__ == "__main__":
    init()