from classes import *

#--------------------------------- GAME MECHANICS ---------------------------------#

def damage(target, amount:int):
    target.HP -= amount
    output(str(target.name) + " subit " + str(amount) + " points de dégâts !")
    if target.HP <= 0 :
        target.HP = 0
        target.kill()

def heal(target, amount):
    HP = target.HP
    target.HP += amount
    if target.HP > target.maxHP :
        target.HP = target.maxHP
    output(str(target.name) + " est soigné de " + str(target.HP - HP) + " points de vie !")

def output(msg):
    print(msg)

#------------------------------------ EFFECTS ------------------------------------#

