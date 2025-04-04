from player import Player
from entities import randompik, types
from functions import select_pik, fight, capture, first
from intinput import intinput
print("---------------------------------------------------------------------------------------")
print(" ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  \n▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌\n▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌ ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌\n▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌  ▐░▌          ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌\n▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▐░▌ ▐░▌▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌\n▐░░░░░░░░░░░▌     ▐░▌     ▐░░▌    ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌\n▐░█▀▀▀▀▀▀▀▀▀      ▐░▌     ▐░▌░▌   ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▀   ▐░▌▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌\n▐░▌               ▐░▌     ▐░▌▐░▌  ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌\n▐░▌           ▄▄▄▄█░█▄▄▄▄ ▐░▌ ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌\n▐░▌          ▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌\n ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀    ")
print("---------------------------------------------------------------------------------------\n")
player = Player(input("enter your name: ").capitalize())

#choix starter
y = True
while y:
    print("\n-Earth: 1\n-Water: 2\n-Fire: 3\n-Electric: 4")
    choice = intinput("choose a starter: ")-1
    if choice < 4:
        first(types[choice],player)
        y = False
    else:
        print("please select a valid starter pack\n")
    
#combat ou quitter
x = True
while x:
    choice = input("fight: 1\ninfo: 2\nleave the game: leave\nselect choice: ")
    if choice == "1":
        
        npc_pik = randompik(3,player.BestPiklvl())
        print(f"\nYou are fighting a {npc_pik} level {npc_pik.lvl}!")
        player_pik = select_pik(player)
        win = fight(player_pik,npc_pik)
        player_pik.resetHP()
        npc_pik.resetHP()
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