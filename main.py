from textStuff import *
from Player import *
race = "NA"


player1 = char(1, "NA", "NA")


# (Test Delete after if not working)


durgonBorn = races(r + "Durgonborn" + R,
                   "A tall, strong creature descended from dragons and equipped with their signature fiery breath.",
                   "NA")

habit = races(r + "Habit" + R,
              "A small humanoid who is known for their quick wit and dexterous stature.",
              "NA")

hooman = races(r + 'Hooman' + R,
               "A very average creature, known for their conquests across the world",
               "NA")
mothPerson = races(r+"Mothling"+R,
"A shorter creature with delicate wings, they can travel short distances in the air, but deal less damage. ","Na")

# Stop Deleting past this point.


def start():
    global race

    def raceQuest():
        choice = input(">")
        if choice == "1":
            player1.race = durgonBorn
            player1.extra.append(fireball)
            player1.stats.str += 1
        elif choice == "2":
            player1.race = habit
            player1.stats.dex += 2
        elif choice == "3":
            player1.race = hooman
            player1.stats.chr += 1
            player1.stats.int += 1
            print(player1.stats.int)
        elif choice == "4":
            player1.race = mothPerson
            player1.stats.dex += 1
            player1.extra.append(mothWings)
        else:
            print("Please Repeat.")
            raceQuest()

    player1.name = input("What is your name?\n"
                         ">")
    print(line)
    name = player1.name
    print(name, "... Yes... That does seem like a name.")
    print("Well then," + g, name, R + ", who are you?")
    print("1.", r, "DurgonBorn:", R, durgonBorn.desc)
    print("2.", r, "Habit:", R, habit.desc)
    print("3.", r, "Hooman:", R, hooman.desc)
    print("(Type 1,2,or 3 for choice)")
    raceQuest()
    if player1.name == "Qadon":
        player1.inv.append(bestSword)
        player1.weapon = bestSword
        print("got and equiped bestSword")


def sayPlayerDesc():
    print("You're name is", player1.name,
          "\nYou are a", player1.race.name)
    print("STR:", player1.stats.str, "\n"
          "DEX:", player1.stats.dex, "\n"
          "CHR:", player1.stats.chr, "\n"
          "INT:", player1.stats.int, "\n"
          "WIS:", player1.stats.wis, "\n")
    for i in player1.extra:
        print("Your abilities :", i.name)


def asks(quest,restate = "NA"):
    if quest == "name":
        print(player1.name)
    if quest == "stats":
        print("STR:", player1.stats.str, "\n"
                                         "DEX:", player1.stats.dex, "\n"
                                                                    "CHR:", player1.stats.chr, "\n"
                                                                                               "INT:",
              player1.stats.int, "\n"
                                 "WIS:", player1.stats.wis, "\n")
    if quest == "abilities":
        for i in player1.extra:
            print("Your abilities :", i.name)
    if quest == "race":
        print(player1.race.name)
    if quest == "help":
        print(
            "In the game, 'Durgons and Habits', you play as your character:" + player1.name + " and follow their adventures\n"
            "In the game, you are presented with questions which you can respond with.\n."
            "In most cases, problems can be solved by answering with one of the numbers of a listed responce, or typing Y/N for yes or no.\n"
            "The player has various abilities given to them during the quest and based on their race and level.\n"
            "Depending on these abilities, the player can sometimes be presented with various extra questions, usually presented in a special color.\n"
            "Some nouns may be colored differently. This is due to them being important to the player. Things such as choices, NPC names,\n"
            "and player names can be colored differently.\n"
            "For help with combat, type 'comhelp', for credits and version, type 'credits'. To continue the game, answer the question presented.\n"
            "(You can also type 'restate' to be refreshed on your options)")

    if quest == "comhelp":
        print(
            "Combat can be triggered either by random battles or specifically scripted events. In combat, the player,\n"
            "allies, and enemies take turns to attack (mainly decided by the dexterity stat and/or other bonuses. \n"
            "The player can attack with a weapon they have equipped. Certain weapons have better stats or have special powers...\n"
            "Enemies also have items and weapons, some of which can be dropped upon their death.\n"
            "As well, many monsters give EXP upon death, which, when the amount of EXP exceeds a certain point, the player 'levels up,\n"
            "gaining more abilities, such as health and such.\n"
            "In Battle, the player can equip various items (sacraficing their turn to do so) by typing 'equip' and selecting the item they wish to use.\n"
            "Be wary, as some items will be consumed if used.\n"
            "For help with general play, type 'help' for credits and version, type 'credits'. ")
    if quest == "credits":
        print("Durgons and Habits:\n"
              "Lead Developer:Quinn Donahue (Qadon)\n"
              "Art and Music:Quinn Donahue (Qadon)\n"
              "Voice Actor:Quinn Donahue (Qadon)\n"
              "Lead Researcher:Quinn Donahue (Qadon)\n"
              "Game tester:Quinn Donahue (Qadon), and Samuel Bucknell")
    if quest == "equip":
        equippingCom(player1)
    if quest == "inv":
        for i in player1.inv:
            print(i.name)
    if quest == "restate":
        print(restate)


def tryQuestions():
    print("Want Knowledge?")
    choice = input(">")
    asks(choice)
    tryQuestions()


