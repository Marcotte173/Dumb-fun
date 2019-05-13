from CreatureClass import *

class Hero:
    def __init__(self, name,pClass):
        self.name = name
        self.className = pClass.C
        self.gold = 100
        self.pLevel = 1
        self.xpRequired = self.pLevel *20+5