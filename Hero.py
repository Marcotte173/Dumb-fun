class Hero:
    def __init__(self, name, pClass, damage, health, energy,):
        self.name = name
        self.damage = damage
        self.health = health
        self.pClass = pClass
        self.energy = energy
        self.potions = 1
        self.xp = 0
        self.startEnergy = self.energy
        self.startHealth = self.health
        self.startDamage = self.damage
        self.maxEnergy = energy
        self.maxHealth = health
        self.gold = 100
        self.pLevel = 1
        self.xpRequired = self.pLevel *20+5