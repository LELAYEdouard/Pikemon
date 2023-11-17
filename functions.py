from random import randint
from pikemon import Pikemon
from player import Player
from entities import initpik, reducers
from initinput import intinput

def attack(a: Pikemon, b: Pikemon, coef: float, nb: int, dodge: bool):
    hit = randint(0,100) + a.tiredness
    attackname=a.getAttack(nb)
    mod = 0
    if dodge == True:
        mod = 30
    if hit > 30 + mod:
        damage = round(a.Attack(attackname[0])*coef)
        b.TakeDamage(damage)
        return f"{a} uses {attackname[0]}\n {b} takes {damage} damage, he remains {b.hp} HP\n"
    else:
        return f"{a} tried to use {attackname[0]} but missed"

def fight(p1: Pikemon, p2: Pikemon):
    if reducers[p1.type] == p2.type:
        coef_p1=1.2
        coef_p2=0.8
    elif reducers[p2.type] == p1.type:
        coef_p1=0.8
        coef_p2=1.2
    else:
        coef_p1=1
        coef_p2=1
    
    i=1
    while p1.hp > 0 and p2.hp > 0:
        print(f"--------------------round {i}-------------------")
        print(f"{p1.getAttack(0)[0]}: 1\n{p1.getAttack(1)[0]}: 2\n{p1.getAttack(2)[0]}: 3\n{p1.getAttack(3)[0]}: 4")
        choice = intinput("choose attack:")-1
        n = randint(0,3)
        if choice < len(p1.attack):
            if n == 3:
                print(attack(p1,p2,coef_p1,choice,True))
            else:
                print(attack(p1,p2,coef_p1,choice,False))
            
            if p2.hp == 0:
                print(f"{p1} won with {p1.hp}HP")
                print(f"-------------------GAME OVER-------------------")
                return True
            
            if choice == 3:
                print(attack(p2,p1,coef_p2,n,True))
            else:
                print(attack(p2,p1,coef_p2,n,False))
            
            if p1.hp == 0:
                print(f"{p1} looses")
                print(f"-------------------GAME OVER-------------------")
                return False
            i+=1
        else:
            print("error, please select an attack\n")

def select_pik(player: Player):
        while True:
            i = 1
            for elt in player.deck:
                print(f"{elt}(lvl {elt.lvl}): {i}")
                i += 1
            choice = intinput("select which Pikemon fight: ")-1
            if choice < len(player.deck):
                return player.getPikemon(choice)
            else:
                print("please select a valid Pikemon\n")

def capture(player: Player,pikemon: Pikemon):
    while True:
        choice = input(f"Try to capture {pikemon}(lvl {pikemon.lvl}): 1\nLet {pikemon} leave: 2\nchoice: ")
        if choice == "1":
            rand=randint(0,100)
            if rand < 40:
                print(f"You captured {pikemon}!\n")
                player.addPikemon(pikemon)
                return
            else:
                print(f"You don't capture {pikemon}...\n")
                return

        elif choice == "2":
            print(f"You let {pikemon} leave\n")
            return
            
        else:
            print("please select a valid choice\n")

def first(n: str, p: Player):
    pik = initpik(n,1)
    print(f"You've got {pik}!\n")
    p.addPikemon(pik)
    return pik
