from colorama import Fore, Back, Style
from Weapons import *
line = f"{'-'*37}\n"
g = Fore.GREEN
b = Fore.BLUE
r = Fore.RED
R = Style.RESET_ALL

asksQuests = ["name","stats","abilities","race","help","comhelp","credits","equip","inv"]

def equippingCom(x):
    print("What will you equip?")
    choice = input(">")
    for i in x.inv:
        if choice == x.weapon.name:
            print("You already have that equipped.")
            break
        if i.name == choice:
            x.weapon = i
            print("Equipped ",x.weapon.name)
            break
        elif "fist" == choice:
            print("Punching mode engaged.")
            x.weapon = fist
            break
        elif "inv" == choice:
            for i in x.inv:
                print(i.name)
                equippingCom(x)
        elif "exit" == choice:
            break
        elif choice == "inspect":
            inspect(x)
        else:
            print("You don't have that.")
            equippingCom(x)
        equippingCom(x)

def inspect(x):
    print("What will you inspect?")
    choice = input(">")
    for i in x.inv:
        if choice == x.weapon.name:
            print("Equipped")
            print(i.description)
            inspect(x)
        if i.name == choice:
            print(i.description)
            inspect(x)
        elif "exit" == choice:
            break
        else:
            print("You don't have that.")
            inspect(x)
