from Weapons import *


# Basic Character Class
# Basic Stats list


class stats:
    def __init__(self, str, dex, chr, int, wis):
        self.str = str
        self.dex = dex
        self.chr = chr
        self.int = int
        self.wis = wis


class char:

    def __init__(self, level, race, name):
        self.level = level
        self.name = name
        self.size = "med"
        self.race = race
        self.inv = []
        self.weapon = fist
        self.maxHealth = level * 2 + 20
        self.health = self.maxHealth
        self.attackBo = 1 + self.weapon.damage
        self.exp = 0
        self.expMax = 10 * self.level
        self.spells = []
        self.extra = []
        # global stats
        self.stats = stats(1, 1, 1, 1, 1)


# Races
class races:
    def __init__(self, name, desc, atr = "NA"):
        self.name = name
        self.desc = desc
        self.atr = atr


# Health & LVL ups
def resetHealth(player):
    player.health = player.maxHealth


def levelUp(player):
    player.level += 1
    player.expMax = 10 * player.level
    player.attackBo += 1
    player.maxHealth = player.level * 2 + 20
    resetHealth(player)
    print("You Leveled Up!")
    print("Health: ", player.health, "/", player.maxHealth)


def giveEXP(amount, player):
    player.exp += amount
    if player.exp >= player.expMax:
        player.exp -= player.expMax
        levelUp(player)
