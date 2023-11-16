from random import randint
from Pikemon import Pikemon

types=["earth","water","fire","electric"]
attacks={"earth":[("Dig",10, 25),("Spikes",10, 25),("Earthquake",20, 50),"dodge"],
        "water":[("Bubble",10, 25),("Jet Punch",10, 25),("Bubble_Beam",20, 50),"dodge"],
        "fire":[("Overheat",10, 25),("Flame Charge",10, 25),("Eruption",20, 50),"dodge"],
        "electric":[("Spark",10, 25),("Discharge",10, 25),("Thunderbolt",20, 50),"dodge"]}

name={"earth":["Onyx","Geodude","Nidoking"],
        "water":["Squirtle","Magikarp","Totodile"],
        "fire":["Charmander","Fennekin","Flareon"],
        "electric":["Pikachu","Zapdos","Magnemite"]}

#left reduces right
reducers = {"earth":"electric",
            "water":"fire",
            "fire":"earth",
            "electric":"water"}

def initpik(type,lvl):
    p = Pikemon(name[type][randint(0,2)],type,attacks[type],lvl)
    return p

def randompik(t: int, maxlvl: int):
    rtype = randint(0,t)
    rtype = types[rtype]
    rlvl = randint(1, maxlvl)
    return initpik(rtype,rlvl)
    