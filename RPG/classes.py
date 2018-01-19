from skills import *
from equipment import *

class Player:
    def __init__(self, profession):
        self.profession = profession
        self.maxHP = profession.maxHP[0]
        self.maxEP = profession.maxEP[0]
        self.inventory = []
        self.skills = profession.skills
        self.attak = profession.attak[0]
        self.magic = profession.magic[0]
        self.armor = profession.armor[0]
        self.HP = self.maxHP
        self.EP = self.maxEP
        self.effects = []
        self.dead = False
        self.name = "undefinedName"
        self.equipment = []
        self.level = 1
        self.exp = 0

    def levelUp(self):
        self.level += 1
        self.statUpdate()
        self.HP = self.maxHP
        self.EP = self.maxEP
        output("**DING**  " + self.name + " passe au niveau " + str(self.level) + " !  **DING**")
    
    def statUpdate(self):
        self.skills = self.profession.skills
        self.maxHP = self.profession.maxHP[0] + (self.level-1)*self.profession.maxHP[1]
        self.maxEP = self.profession.maxEP[0] + (self.level-1)*self.profession.maxEP[1]
        self.attak = self.profession.attak[0] + (self.level-1)*self.profession.attak[1]
        self.magic = self.profession.magic[0] + (self.level-1)*self.profession.magic[1]
        self.armor = self.profession.armor[0] + (self.level-1)*self.profession.armor[1]
        for i in range(len(self.equipment)):
            if self.equipment[i] in equipments :
                for key in equipments[self.equipment[i]]["bonus"]:
                    if key == "attak":
                        self.attak += equipments[self.equipment[i]]["bonus"]["attak"]
                    if key == "magic":
                        self.magic += equipments[self.equipment[i]]["bonus"]["magic"]
                    if key == "armor":
                        self.armor += equipments[self.equipment[i]]["bonus"]["armor"]

    def equip(self, equipment):
        self.equipment += [equipment]
        self.statUpdate()

    def maxHeal(self):
        self.HP = self.maxHP

    def kill(self):
        output(str(self.name)+ " meurt.")
        self.dead = True
    
    def revive(self):
        self.dead = False
        self.HP = int(self.maxHP/2)

    def displayInventory(self):
        output("Contenu de l'inventaire de " + self.name + ":")
        for i in range(len(self.inventory)):
            output("    " + self.inventory[i].name)
    
    def displayEquipment(self):
        output("Equipement de " + self.name + ":")
        for i in range(len(self.equipment)):
            output("  -  " + equipments[self.equipment[i]]["name"])
    

class Warrior:
    maxHP = [120,10]
    maxEP = [40,5]
    skills = {}
    attak = [25,5]
    magic = [0,0]
    armor = [40,5]

class Rogue:
    maxHP = [100,8]
    maxEP = [70,5]
    skills = {}
    attak = [35,5]
    magic = [0,0]
    armor = [20,3]

class Priest:
    maxHP = [90,8]
    maxEP = [100,7]
    skills = {}
    attak = [20,3]
    magic = [30,7]
    armor = [20,4]

class Wizard:
    maxHP = [70,7]
    maxEP = [110,8]
    skills = {}
    attak = [15,3]
    magic = [40,8]
    armor = [20,4]