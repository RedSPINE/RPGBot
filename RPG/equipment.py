from mechanics import *

UNKNOWN = 0
ONE_HAND = 1
TWO_HAND = 2
HEAD = 3
CHEST = 4
RING = 5

def give(item, target):
    source.inventory += [item]

equipments = {
    "wand1" : {
        "name" : "Baguette sésame-pavot",
        "value" : 30,
        "eqType" : ONE_HAND,
        "minLvl" : 1,
        "bonus" : {
            "magic" : 10
        }
    }
}