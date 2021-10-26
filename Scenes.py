from main import *
from battles import *
cartLooted = False
import random

##Current issue
def testBattle(stat,level,enemy,show = True):
    roll = random.randrange(1,20) + stat
    if show == True:
        print("You rolled a ",roll)
    if level == "NA":
        print("Level not specified")
        level = 0
    elif roll >= level:
        return
    else:
        battle(enemy)
def testFunc(stat,level,func,show = True):
    roll = random.randrange(1,20)+ stat
    if show == True:
        print("You rolled a ",roll)
        if level == "NA":
            print("Level not specified")
            level = 0
        elif roll >= level:
            return
        else:
            func()
##End of Current Issue


def giveItems():
    print("You got the item")

def forestStart():
    global reprint
    reprint = "You awaken in the middle of a deep woods. Your head is buzzing. As you stand to your feet, you notice\n"\
          "a grisly scene. The bodies of many dead hoomans lay around, and the smell of burning fills your nostrils.\n"\
          "The source of this smell seems to be coming from a burning cart a few feet in front of you.\n"\
          "There is a path leading further down the woods.\n"\
          "Did you cause this death and chaos? Were you a defender of this cart, or the attacker?\n"\
          "These questions that flow through your mind are interrupted by the sound of the cart violently exploding\n"\
          "You should probably leave...\n What will you do?"
    global cartlooted


    print(reprint)
    forestQuestions()
def forestQuestions():
    restate = ("1. Search The "+b+"Burning Cart"+R+"\n"
          "2. Look at The "+b+"Path"+R+"\n"
          "3. Look at The "+b+"Woods"+R+"\n")
    print(restate)

    # Should make this into a *args or **Kwargs function at some point. It will make duplication easier.

    def choices():
        def C1():
            global cartLooted

            if cartLooted == True:
                print("The cart has nothing unburnt left in it, but you do scorch yourself on it.")
                print(line)
                forestQuestions()
            else:
                print(
                    "The Cart is on fire. It burns with an intense heat that even from a few feet away still feels unbareably hot.\n"
                    "You should probably leave.")
                print("1. No, look in the cart.\n"
                      "2. Leave.")

                def choices():
                    global cartLooted
                    choice = input(">")

                    if choice == "1":
                        print(
                            "You go through the fire and search the cart. It hurts, your hands are burned, but you find a sweet\n"
                            "looking dagger.")
                        cartLooted = True
                        player1.inv.append(ironDagger())
                        print(line)
                        forestQuestions()
                    elif choice == "2":
                        print("The fire crackles evilly.")
                        cartLooted = True
                        print(line)
                        forestQuestions()
                    else:
                        print("Please Restate")
                        choices()
                choices()
        def C2():
            print("The path leads away, down through the forest. It looks well walked\n"
                  "and pretty maintained. Perhaps this path leads to a village...\n"
                  "Follow the path?\n"
                  "y/n")
            def choices():
                choice = input(">")
                if choice == "y":
                    print("You go down the path")
                    downPath(Gobin(),town1)
                if choice == "n":
                    forestQuestions()

                else:
                    choices()

            choices()
        def C3():
            print("C3")
            print("The woods extend far out. If you went out there, who knows where you would turn up.\n"+
                  r+"Warning: You will end up in a random position"+R+
                  "\n Not implemented yet.\n(y/n)")
            def choices():

                choice = input(">")
                if choice == "y":
                    print("Choice not implimented")
                    forestQuestions()
                elif choice == "n":
                    forestQuestions()
                else:
                    print("Please Restate")
                choices()
            choices()





        choice = input(">")
        asks(choice,restate)
        print(line)
        if choice == "1":
            C1()
        elif choice == "2":
            C2()
            choices()
        elif choice == "3":
            C3()
        elif choice in asksQuests:
            forestQuestions()
        elif choice == "restate":
            forestQuestions()
            choices()
        else:
            print("Please Restate")
            choices()
    choices()


def town1():


    def Sewer1():
        battleMSG = "While wandering around in the sewers, you are attacked by a Gobin!"
        print('You arrive in the town, and see a great wooden wall with a large opening in the middle.\n'
              'As you walk towards the village, the two guards shout almost in unison, "It\'s a Durgonborn! Get \'em!".\n'
              "\n"
              "You run as the guards chase you. However, just as you begin to catch your breath, the leaves beneath you give way\n"
              "and you fall down into a dank, dark, smelly tunnel system. This is... probably a sewer...")


        def sewerDirection(room):
            smellyLooted = False
            print(room)
            if room != 1 or room != 5 or room != 7 or room != 8 or room!= 9 or room != 10 or room != 11:
                testBattle(player1.stats.dex,5,Gobin(),show = False)

            if room == 1:
                print("You start this maze with a light above you. You probably can't climb up that way...")
                print("The only direction to go is to the east...")
                sewerDirection(2)

            if room == 2:
                print("This room has openings to the East, South and West.\nWhere will you go?\n"
                      "1.East\n"
                      "2.South\n"
                      "3.West\n")
#Room 2 Choice
                def choose():
                    choice = input(">")
                    asks(choice)
                    if choice == "1":
                        sewerDirection(3)
                    elif choice == "2":
                        sewerDirection(4)
                    elif choice == "3":
                        sewerDirection(1)
                    else:
                        print("Please restate")
                        choose()
                choose()

            if room == 3:
                print("This room is a dead end. You decide to turn back.")
                sewerDirection(2)

            if room == 4:
                restate = ("This room has openings to the North,East,and West.\n "
                      "To the East you hear a strange cackling and see a light flickering in the dark.\n"
                      "Where will you go?\n"
                      "1.North\n"
                      "2.East\n"
                      "3.West\n")
                print(restate)

# Room 4 Choice
                def choose():
                    choice = input(">")
                    asks(choice,restate)
                    if choice == "1":
                        sewerDirection(2)
                    elif choice == "2":
                        sewerDirection(5)
                    elif choice == "3":
                        sewerDirection(6)
                    else:
                        print("Please Restate")
                        choose()
                choose()
            if room == 5:
                if smellyLooted == False:
                    print("You enter the room, but as soon as you do, you are ambushed by a Gobin!")
                    player1.health -= 5
                    battle(Gobin())
                    print("After the battle, you look around the room. There is a book on the floor near a burning fire.\n"
                          'Picking up the book, you notice it has the name "The worst smells to smell". What an interesting find!\n'
                          '(Added Smelly to spells)')
                    player1.spells.append(smelly)
                    smellyLooted = True
                else:
                    print("This room has nothing in it. The area is looten. All that is here is a fire which is only made of\n"
                          "embers...")
                print("There are no other ways to go, so you decide to go to the South.")
                sewerDirection(4)
            if room == 6:
                restate =("This room has openings to the North, East,and West.\n "
                      "To the East, you feel a slight wind that smells of clean, sweet and freeing air.\n"
                      "To the South, you hear a strange gurgling...\n"
                      "Where will you go?\n"
                      "1. East\n"
                      "2. South")
                print(restate)
                def choice(choice, restate):
                    choice = input(">")
                    if choice == "1":
                        sewerDirection(7)
                    elif choice == "2":
                        sewerDirection(8)
                    else:
                        print("Please Restate")
                    choices()
            if room == 7:
                print("You have reached the exit. Hooray!")
            if room == 8:
                restate = "Those gurglings have been replaced with groans. This does not sound good\n" \
                "You should turn back...\n" \
                "(y/n)"
                def choices():
                    choice = input(">")
                    asks(choice)
                    if choice == "y":
                        sewerDirection(9)
                    elif choice == "n":
                        sewerDirection(6)
                    else:
                        print("Please Restate")
                        choices()
                    choices()
            if room == 9:
                restate = ("The gurglings are roars. Seriously. Don't go that way. Those sounds are awful!\n" \
                          "Go forward?\n"
                           "(y/n)")
                def choices(choice,restate):
                    choice = input(">")
                    if choice == "y":
                        sewerDirection(10)
                choices()
            if room == 10:
                print("You enter the room and before you stands a giagantic monsterous beast of a creature, it's teeth dripping\n"
                      "with blood and it's eyes filled with anger and hatred. It begins to lumber towards you!")
                battle(GaveGnoll)
                print("You beat the Gave Gnoll. Proceeding forwards, you find yourself in a large revine, where the waters of the sewers\n"
                      "run out and the light from the sun overwhelms you!")



#Start Point
        sewerDirection(1)
    Sewer1()


def downPath(enemy,path):
    print("While walking down the path, you stumble upon a ",enemy.name)
    battle(enemy)
    if player1.health >= 0:
        print(line)
        path()
    else:
        print("Looser")
        exit()



