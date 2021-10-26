from Weapons import *
class Gobin:
    def __init__(self):
        self.name = "Gobin"
        self.size = "small"
        self.type = "Goblinoid"
        self.weapon = ironDagger()
        self.desc = "Gobins are a normal sight in the forests of Hysteria. They like to take take from to rich\n" \
                    "and cool, so this one must be mistaken."
        self.maxHealth = 7
        self.health = 7
        self.attackBo = 1
        self.defebo = 1
        self.comWeight = 2
        self.expGive = 2

class Woggy:
    def __init__(self):
        self.name = "Woggy"
        self.size = "med"
        self.type = "monstrosity"
        self.weapon = "woggyJaws"
        self.desc = "It's a large, dog-like beast. It occasionally sputters out a small, whimpering growl."
        self.maxHealth = 12
        self.health = 12
        self.attackBo = 2
        self.defebo = 1
        self.comWeight = 2
        self.expGive = 2
class GaveGnoll:
    def __init__(self):
        self.name = "Gave Gnoll"
        self.size = "large"
        self.type = "Monstrosity"
        self.weapon = "Gnolljaws"
        self.desc = "It's a giant, man eating monster that is ready to chow down on your flesh!"
        self.maxHealth = 30
        self.health = 30
        self.attackBo = 3
        self.defebo = 2
        self.comWeight = 4
        self.expGive = 20

woodEnemies = [Woggy(),Gobin()]
