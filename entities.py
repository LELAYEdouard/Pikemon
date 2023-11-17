from random import randint
from pikemon import Pikemon
from player import Player
types=["earth","water","fire","electric"]
attacks={"earth":[("Dig", 10, 25),("Spikes", 10, 25),("Earthquake", 20, 50),("dodge", 0, -25)],
        "water":[("Bubble", 10, 25),("Jet Punch", 10, 25),("Bubble_Beam", 20, 50),("dodge", 0, -25)],
        "fire":[("Overheat", 10, 25),("Flame Charge", 10, 25),("Eruption", 20, 50),("dodge", 0, -25)],
        "electric":[("Spark", 10, 25),("Discharge", 10, 25),("Thunderbolt", 20, 50),("dodge", 0, -25)]}

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

def randompik(t: int,player_lvl:Player):
    rtype = randint(0,t)
    rtype = types[rtype]
    rlvl = player_lvl + randint(-2, 2)
    if rlvl<=0:
        rlvl=1
    return initpik(rtype,rlvl)
    