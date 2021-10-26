# Slicer
class woodenSword:
    type = "slicer"
    name = "Wooden Sword"
    metal = "wood"
    description = "It is a small wooden sword, mainly used as a children's toy."
    StrReq = 1
    armDam = 1
    damage = 1


class ironDagger:
    type = "slicer"
    name = "Iron Dagger"
    metal = "iron"
    description = "It's a small dagger, perfectly weighted for your hands."
    StrReq = 1
    armDam = 0
    damage = 2


class ironSword:
    type = "slicer"
    name = "Iron Sword"
    metal = "iron"
    description = "It's a decently balanced sword, which looks quite clean. Want to change that?"
    StrReq = 2
    armDam = 1
    damage = 3


# Blunt
class woodenBat:
    type = "Blunt"
    name = "Wooden Bat"
    metal = "wood"
    description = "A simple wooden shaft used for violently smashing your enemies skulls in."
    StrReq = 4
    armDam = 0
    damage = 2


# Ranged
class bow:
    type = "ranged"
    name = "Bow"
    metal = "wood"
    description = "This bow has seen better days, but still can cause some mayhem."
    armDam = 1
    StrReq = 1
    damage = 2


# Magic
class smelly:
    type = "magic"
    smellyTime = 3
    damage = 1


# Fist
class fist:
    type = "melee"
    name = "fist"
    description = "The sacred art of punching something till it dies."
    damage = 0


# Other
class fireball:
    type = "other"
    name = "Fireball"
    damage = 3

class mothWings:
    type = "other"
    name = "Moth Wings"

class bestSword:
    type = "devTool"
    name = "QSword"
    damage = 100000000

