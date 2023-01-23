from random import randint
from pickle import dump, load
from os import system

class colors:
    def __init__(self) -> None:
        self.black = "\u001b[30m"
        self.red = "\u001b[31m"
        self.green = "\u001b[32m"
        self.yellow = "\u001b[33m"
        self.blue = "\u001b[34m"
        self.magenta = "\u001b[35m"
        self.cyan = "\u001b[36m"
        self.white = "\u001b[37m"
        self.reset = "\u001b[38m"

    def initiate():
        system("clear")

class player:
    def __init__(self) -> None:
        self.name = "Player"
        self.damage = 2
        self.health = 20
        self.defense = 0
        self.exp = 0
        self.inventory = []
    
    def changeWeapon(self, weapon):
        pass

    def changeArmour(self, armor):
        pass

    def printData(self):
        print(f"Name: {self.name}\nDamage: {self.damage}\nHealth: {self.health}\nDefense: {self.defense}")

    def saveData(self):
        saveFile = open("{name}.save", "w")

        dump(self.name, saveFile)
        dump(self.damage, saveFile)
        dump(self.health, saveFile)
        dump(self.defense, saveFile)
        dump(self.exp, saveFile)
        dump(self.inventory, saveFile)

        saveFile.close()

    def loadData(self, name):
        saveFile = open(name+".save", "r")

        self.name = load(self.name, saveFile)
        self.damage = load(self.damage, saveFile)
        self.health = load(self.health, saveFile)
        self.defense = load(self.defense, saveFile)
        self.exp = load(self.exp, saveFile)
        self.inventory = load(self.inventory, saveFile)

        saveFile.close()

class enemy:
    def __init__(self, name, description, damage, health, defense, expMin, expMax) -> None:
        self.name = name
        self.description = description
        self.damage = damage
        self.health = health
        self.defense = defense
        self.exp = randint(expMin, expMax)

    def printData(self):
        print(f"Name: {self.name}\nDamage: {self.damage}\nHealth: {self.health}\nDefense: {self.defense}\nExp Reward: {self.exp}")

def init():
    colors.initiate()

if __name__ == "__main__":
    init()