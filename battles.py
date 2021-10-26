import random
endBattle = False
from main import *
from monsters import *
simpleMonsters = [Gobin(), Woggy()]

def playerWin(enemy):
    player1.exp += enemy.expGive
    print("You Gained ",enemy.expGive,"exp.")
    giveEXP(enemy.expGive, player1)
    print("Exp: ", player1.exp, "/",player1.expMax)


player1.health = player1.maxHealth

def showStats(enemy):
    print(enemy.name, "'s health: ",enemy.health,"/",enemy.maxHealth)
    print(line)
    print(player1.name,"'s health: ",player1.health, "/", player1.maxHealth)
def enemyAttack(enemy):
    print(enemy.name, "attacks!")
    player1.health -= enemy.attackBo
    print(enemy.attackBo,"Damage.")

def playerAttack(enemy):
    print("What will you do?")
    choice = input(">")

    if choice == "attack" or choice == "a":
        print("Attacking ",enemy.name," with ",player1.weapon.name," dealing",\
        player1.attackBo+player1.weapon.damage, "Damage.")
        enemy.health -= player1.attackBo+player1.weapon.damage
    elif choice == "equip" or choice == "e":
        equippingCom(player1)

    elif choice == "fireball":
        if fireball in player1.extra:
            print("You attack ",enemy.name," with ",fireball.name,"dealing",\
                  fireball.damage, "Damage.")
            enemy.health -= fireball.damage
        else:
            print("You do not have: '",fireball.name,"'In your inventory.")

    else:
        print("Please Restate")
        playerAttack(enemy)
def battle(enemy):
    while enemy.health >= 1 and player1.health >= 1:
        enemyAttack(enemy)
        playerAttack(enemy)
        showStats(enemy)
        if player1.health < 1:
            print("Game Over...")
            exit()
            break
        elif enemy.health < 1:
            print(enemy.name, "defeated.")

            playerWin(enemy)

            break

    enemy.health = enemy.maxHealth
    global RandomForestEnemy
    RandomForestEnemy = random.choice(simpleMonsters)




