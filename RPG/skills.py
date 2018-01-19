from mechanics import *
import random as rng

def fireBall(source, target):
    baseDmg = 15
    dmgMod = 0.5
    skillDmg = int((baseDmg + dmgMod * source.magic) * (rng.random()/10 + 0.9))
    damage(target, skillDmg)

def flameStrike(source, target):
    baseDmg = 10
    dmgMod = 0.7
    skillDmg = int((baseDmg + dmgMod * source.magic) * (rng.random()/10 + 0.9))
    damage(target, skillDmg)

def meteor(source, target):
    baseDmg = 15
    dmgMod = 0.8
    skillDmg = int((baseDmg + dmgMod * source.magic) * (rng.random()/10 + 0.9))
    damage(target, skillDmg)

skills = {
    'Fireball' : [fireBall, 15],
    'Flamestrike' : [flameStrike, 30],
    'Meteor' : [meteor, 40]
}

def cast(source, target, skill):
    if not (skill in source.skills) :
        output(str(source.name) + " ne connaît pas le sort " + skill + ".")
        return False
    if source.level < source.skills[skill] :
        output(str(source.name) + " n'a pas le niveau requis pour utiliser " + skill + ".")
        return False
    EPcost = skills[skill][1]
    if source.EP < EPcost :
        output(str(source.name) + " n'a pas assez d'EP pour lancer " + skill + ".")
        return False
    source.EP -= EPcost
    output(str(source.name) + " utilise " + str(EPcost) + " EP pour lancer " + skill + " sur " + str(target.name) + ".")
    skills[skill][0](source, target)
    return True

    
