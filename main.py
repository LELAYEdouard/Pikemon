from random import randint
from Player import Player
from Pikemon import Pikemon
from entities import initpik, randompik, attacks, reducers, types

def attack(a: Pikemon, b: Pikemon, coef: float, nb: int):
    hit = randint(0,100) + a.tiredness
    attackname=a.getAttack(nb)
    if hit > 30:
        damage = round(a.Attack(attackname)*coef)
        b.TakeDamage(damage)
        print(f"{a} uses {attackname}")
        print(f"{b} takes {damage} damage, he remains {b.hp} HP\n")
    else:
        print(f"{a} tried to use {attackname} but missed")

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
        print(f"{p1.getAttack(0)}: 1\n{p1.getAttack(1)}: 2\n{p1.getAttack(2)}: 3")
        choice = int(input("choose attack:"))-1
        
        if choice < len(p1.attack):
            attack(p1,p2,coef_p1,choice)
            if p2.hp == 0:
                print(f"{p1} won with {p1.hp}HP")
                print(f"-------------------GAME OVER-------------------")
                return True
            
            n = randint(0,2)
            attack(p2,p1,coef_p2,n)
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
            choice = int(input("select which Pikemon fight: "))-1
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

def first(n: str):
    p = initpik(n,1)
    print(f"You've got {p}!\n")
    player.addPikemon(p)
    return p

print("---------------------------------------------------------------------------------------")
print(" ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  \n▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌\n▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌ ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌\n▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌  ▐░▌          ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌\n▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▐░▌ ▐░▌▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌\n▐░░░░░░░░░░░▌     ▐░▌     ▐░░▌    ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌\n▐░█▀▀▀▀▀▀▀▀▀      ▐░▌     ▐░▌░▌   ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▀   ▐░▌▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌\n▐░▌               ▐░▌     ▐░▌▐░▌  ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌\n▐░▌           ▄▄▄▄█░█▄▄▄▄ ▐░▌ ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌\n▐░▌          ▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌\n ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀    ")
print("---------------------------------------------------------------------------------------\n")
player = Player(input("enter your name: ").capitalize())

#choix starter
y = True
while y:
    print("\n-Earth: 1\n-Water: 2\n-Fire: 3\n-Electric: 4")
    choice = int(input("choose a starter: "))-1
    if choice < 4:
        first(types[choice])
        y = False
    else:
        print("please select a valid starter pack\n")
    
#combat ou quitter
x = True
while x:
    choice = input("fight: 1\ninfo: 2\nleave the game: leave\nselect choice: ")
    if choice == "1":
        npc_pik = randompik(3,5)
        print(f"\nYou are fighting a {npc_pik} level {npc_pik.lvl}!")
        player_pik = select_pik(player)
        win = fight(player_pik,npc_pik)
        player_pik.resetHP()
        
        if win == True:
            player_pik.TakeXP(5)
            capture(player,npc_pik)

    elif choice == "2":
        print(f"------------------INFO------------------\nYour name:{player}\nYour Pikemons:{player.deck}")
        for elt in (player.deck):
            print(f"{elt} is level {elt.lvl},HP:{elt.hp}")
        print(f"------------------INFO------------------\n")        
    elif choice == "leave":
        x = False
    else :
        print("please select a valid choice\n")