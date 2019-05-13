from Hero import *
import sys
from CreatureClass import *


Warrior = CreatureClass("Warrior",12,4,0,0)
Mage = CreatureClass("Mage",8,2,3,3)
Rogue = CreatureClass("Rogue",10,5,1,1)

def pClassSelect():
    choice = input("choose your class\n[W]arrior\n[M]age\n[R]ogue\n\n")
    choice = choice.lower()
    if choice == "w":
        global pClass
        global baseDamage
        global baseHealth
        global baseEnergy
        confirm = input("Are you sure you want to be a Warrior?\n[Y]es   [N]o\n\n")
        confirm = confirm.lower()
        if confirm == "y":
            pClass = Warrior
        else:
            pClassSelect()
    elif choice == "m":
        confirm = input("Are you sure you want to be a Mage?\n[Y]es   [N]o\n\n")
        confirm = confirm.lower()
        if confirm == "y":
            pClass = Mage
        else:
            pClassSelect()
    elif choice == "r":
        confirm = input("Are you sure you want to be a Rogue?\n[Y]es   [N]o\n\n")
        confirm = confirm.lower()
        if confirm == "y":
            pClass = Rogue
        else:
            pClassSelect()
    else:
        pClassSelect()

def LevelMaster():
    choice = input("\n\nYou walk into the level master hut. She looks up at you. \n\n'Are you here to level up?'\n\n[Y]es       [N]o")
    if choice == "y":
        LevelCheck()

def LevelCheck():
    if p.xp < p.xpRequired:
        print("Come back when you are more experienced")
    else:
        print("Congrats! You have gained a level!")
        p.maxEnergy += p.startEnergy
        p.maxHealth += p.startHealth
        p.health = p.maxHealth
        p.energy = p.maxEnergy
        p.xp -= p.xpRequired
        p.pLevel += 1
        p.damage += p.startDamage

def Heal():
    if p.health == p.maxHealth:
        print("You don't need healing!")
    elif p.potions < 1:
        print("You don't have enough potions!")
    else:
        p.health = p.maxhealth
        p.potions -= 1
        print("You heal to full health")

def pNameSelect():
    global pName
    pName = input("What is your name?\n\n")
    print(pName)
    confirm = input("Is that your name?\n[Y]es   [N]o\n\n")
    confirm = confirm.lower()
    if confirm == "y":
        return pName
    else:
        pNameSelect()

def Quit():
    sys.exit()

#This is where the game functions begin

def GameStart():
    pNameSelect()
    pClassSelect()
    global p
    p = Hero(pName,pClass,baseDamage,baseHealth,baseEnergy )
    GameTown()

def GameTown():
    print("You are in a town. You see a several places to go\n[W]eapon shop      [A}rmor shop            [D]ungeon ")
    print                                                   ("[C]haracter        [V]isit level master    [H]eal")
    print                                                   ("[Q]uit")
    choice = input("\n\nWhat would you like to do?\n\n")
    choice = choice.lower()
    #if choice == "w":
        #GameWeaponShop()
    #elif choice == "a":
        #GameArmorShop()
    #elif choice == "d":
        #GameDungeon()
    if choice == "h":
        Heal()
    elif choice == "c":
        Character()
    elif choice == "v":
        LevelMaster()
    elif choice == "q":
        Quit()

#def GameWeaponShop():

def Character():
    print("Name: ",p.name)
    print("Health: ", p.health,"/",p.maxHealth)
    print("")
    print("")
    print("")

GameStart()















