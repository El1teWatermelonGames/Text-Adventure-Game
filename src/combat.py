# **Combat Actions**
# Fight, Deal your weapons damage to the enemy
# Check, Check the oponent's health, attack & defense plus show their description
# Items, Open you inventory & possibly use an item

from random import randint
from engine import player

class enemy:
    def __init__(self, name, description, damage, health, defense, expMin, expMax) -> None:
        self.name = name
        self.description = description
        self.damage = damage
        self.health = health
        self.defense = defense
        self.exp = randint(expMin, expMax)

def enterCombat(Enemy: enemy):
    pass