"""

from random import randint
from math import floor
class Player:
    def __init__(self,name):
        self.Pikemon=[]
        self.name=name
        
    def getPikemons(self):
        return self.Pikemon
    
    def getPikemon(self,i):
        return self.Pikemon[i]
    
    def addPikemon(self,pikemon):
        if len(self.Pikemon)<3:
            self.Pikemon.append(pikemon)
        else:
            x=True
            while x:
                print("Maximum Pikemon in inventory, please delete one or cancel")
                choice=input("delete:1\ncancel:2\nchoice:")
                if choice=="1":
                    while x:
                        print(f"select which one you want to delete:\n{self.getPikemons()[0]}(lvl {player.getPikemons()[0].getLVL()}):1\n{self.getPikemons()[1]}(lvl {player.getPikemons()[1].getLVL()}):2\n{self.getPikemons()[2]}(lvl {player.getPikemons()[2].getLVL()}):3")
                        choice=input("choice:")
                        print()
                        if choice=="1":
                            self.Pikemon.pop(0)
                            self.Pikemon.insert(0,pikemon)
                            x=False
                        elif choice=="2":
                            self.Pikemon.pop(1)
                            self.Pikemon.insert(1,pikemon)
                            x=False
                        elif choice=="3":
                            self.Pikemon.pop(2)
                            self.Pikemon.insert(2,pikemon)
                            x=False
                        else:
                            print("select a valid choice")
                elif choice =="2":
                    print(f"You released {pikemon.getName()}!")
                    x=False
                else:
                    print("select a valid choice")
    
    def getName(self):
        return self.name.capitalize()
    
class Pikemon:
    def __init__(self,name,hp,type,attack,lvl):
        
        self.type=type
        self.name=name
        self.attack=attack
        self.lvl=lvl
        self.xp=0
        self.goal_lvl=10+(self.lvl-1)*5

        iv=randint(1,31)
        base=randint(1,255)
        self.hp=floor((2*(base+iv)*self.lvl)/50)+self.lvl+100

    def getName(self):
        return self.name.capitalize()
    
    def TakeXP(self,xp):
        self.xp+=xp
        if self.xp ==self.goal_lvl:
            self.xp=0
            self.lvl+=1
            self.goal_lvl+=5

    def getLVL(self):
        return self.lvl
    
    def getType(self):
        return self.type

    def getHP(self):
        return self.hp
    
    def TakeDamage(self,nb):
        self.hp-=nb
        if self.hp<0:
            self.hp=0

    def getAttack(self,index):
        return self.attack[index]
    
    def Attack(self,attack_name):
        if attack_name == self.attack[0]:
            if self.lvl>1:
                return round(10*(1+self.lvl/10))
            else:
                return 10
        elif attack_name == self.attack[1]:
            if self.lvl>1:
                return round(10*(1+self.lvl/10))
            else:
                return 10   
        elif attack_name == self.attack[2]:
            if self.lvl>1:
                return round(20*(1+self.lvl/10))
            else:
                return 20
    
    def resetHP(self,hp):
        self.hp = hp
    def __repr__(self):
        return self.name.capitalize()



def fight_npc(p1_pik,npc_pik,coef_npc):
    dodge=randint(0,100)
    if dodge>15:
        npc_attack_name=npc_pik.getAttack(randint(0,2))
        npc_attack=round(npc_pik.Attack(npc_attack_name)*coef_npc)
        p1_pik.TakeDamage(npc_attack)
        print(f"{npc_pik.getName()} uses {npc_attack_name}")
        print(f"Your {p1_pik.getName()} takes {npc_attack} damage, he remains {p1_pik.getHP()} HP\n")
    else:
        print(f"{p1_pik.getName()} dodged {npc_pik.getName()}'s attack")

def fight_player(p1_pik,npc_pik,coef_p1,nb_attack):
    dodge=randint(0,100)
    if dodge>15:
        print(f"{p1_pik.getName()} uses {p1_pik.getAttack(nb_attack)}")
        Attack=round(p1_pik.Attack(p1_pik.getAttack(nb_attack))*coef_p1)
        npc_pik.TakeDamage(Attack)
        print(f"{npc_pik.getName()} takes {Attack} damage, he remains {npc_pik.getHP()} HP")
    else:
        print(f"{npc_pik.getName()} dodged {p1_pik.getName()}'s attack")

def fight(p1_pik,npc_pik):
    if (p1_pik.getType()=="water" and npc_pik.getType()=="fire")or(p1_pik.getType()=="fire" and npc_pik.getType()=="earth")or(p1_pik.getType()=="earth" and npc_pik.getType()=="electric")or(p1_pik.getType()=="electric" and npc_pik.getType()=="water"):
        coef_p1=1.2
        coef_npc=0.8
    elif (npc_pik.getType()=="water" and p1_pik.getType()=="fire")or(npc_pik.getType()=="fire" and p1_pik.getType()=="earth")or(npc_pik.getType()=="earth" and p1_pik.getType()=="electric")or(npc_pik.getType()=="electric" and p1_pik.getType()=="water"):
        coef_p1=0.8
        coef_npc=1.2
    else:
        coef_p1=1
        coef_npc=1
    i=1
    while p1_pik.getHP()>0 and npc_pik.getHP()>0:
        print(f"--------------------round {i}-------------------")
        print(f"{p1_pik.getAttack(0)} :1\n{p1_pik.getAttack(1)} :2\n{p1_pik.getAttack(2)} :3")
        choose=input("choose attack:")
        print()
        if choose=="1":
            fight_player(p1_pik,npc_pik,coef_p1,0)
            if npc_pik.getHP()==0:
                print(f"{p1_pik.getName()} won with {p1_pik.getHP()}HP")
                print(f"-------------------GAME OVER-------------------")
                return True
            
            fight_npc(p1_pik,npc_pik,coef_npc)
            if p1_pik.getHP()==0:
                print(f"{p1_pik.getName()} looses")
                print(f"-------------------GAME OVER-------------------")
                return False
            i+=1
        elif choose=="2":
            fight_player(p1_pik,npc_pik,coef_p1,1)
            if npc_pik.getHP()==0:
                print(f"{p1_pik.getName()} won with {p1_pik.getHP()}HP")
                print(f"-------------------GAME OVER-------------------")
                return True

            fight_npc(p1_pik,npc_pik,coef_npc)
            if p1_pik.getHP()==0:
                print(f"{p1_pik.getName()} looses")
                print(f"-------------------GAME OVER-------------------")
                return False
            i+=1
        elif choose=="3":
            fight_player(p1_pik,npc_pik,coef_p1,2)
            if npc_pik.getHP()==0:
                print(f"{p1_pik.getName()} won with {p1_pik.getHP()}HP")
                print(f"-------------------GAME OVER-------------------")
                return True

            fight_npc(p1_pik,npc_pik,coef_npc)
            if p1_pik.getHP()==0:
                print(f"{p1_pik.getName()} looses")
                print(f"-------------------GAME OVER-------------------")
                return False
            i+=1
        else:
            print("error, please select an attack\n")

def select_pik(player):
    if len(player.getPikemons())==1:
        while True:
            choice_pik =input(f"{player.getPikemons()[0]}(lvl {player.getPikemons()[0].getLVL()}):1\nselect which Pikemon fight:")
            if choice_pik =="1":
                return player.getPikemons()[0]
            else:
                print("please select a valid Pikemon\n")
    elif len(player.getPikemons())==2:
        while True:
            choice_pik =input(f"{player.getPikemons()[0]}(lvl {player.getPikemons()[0].getLVL()}):1\n{player.getPikemons()[1]}(lvl {player.getPikemons()[1].getLVL()}):2\nselect which Pikemon fight:")
            if choice_pik =="1":
                return player.getPikemons()[0]
            elif choice_pik=="2":
                return player.getPikemons()[1]
            else:
                print("please select a valid Pikemon:\n")

    elif len(player.getPikemons())==3:
        while True:
            choice_pik =input(f"{player.getPikemons()[0]}(lvl {player.getPikemons()[0].getLVL()}):1\n{player.getPikemons()[1]}(lvl {player.getPikemons()[1].getLVL()}):2\n{player.getPikemons()[2]}(lvl {player.getPikemons()[2].getLVL()}):3\nselect which Pikemon fight:")
            if choice_pik =="1":
                return player.getPikemons()[0]
            elif choice_pik=="2":
                return player.getPikemons()[1]
            elif choice_pik=="3":
                return player.getPikemons()[2]
            else:
                print("please select a valid Pikemon\n")

def capture(player,pikemon):
    while True:
        choice=input(f"Try to capture {pikemon.getName()}(lvl {pikemon.getLVL()}):1\nLet {pikemon.getName()} leave:2\nchoice:")
        if choice=="1":
            rand=randint(0,100)
            if rand<100:
                print(f"You captured {pikemon.getName()}!\n")
                player.addPikemon(pikemon)
                break
            else:
                print(f"You don't captured {pikemon.getName()}...\n")
                break
        elif choice=="2":
            print(f"You let {pikemon.getName()} leave\n")
            break
        else:
            print("please select a valid choice\n")

def first(n: str):
    pik = Pikemon(name[n][randint(0,2)],100,n,attack[n],1)
    print(f"You've got {pik}!\n")
    player.addPikemon(pik)
    return pik


type=["earth","water","fire","electric"]
attack={"earth":["Dig","Spikes","Earthquake"],
        "water":["Bubble","Jet Punch","Bubble_Beam"],
        "fire":["Overheat","Flame Charge","Eruption"],
        "electric":["Spark","Discharge","Thunderbolt"]}
name={"earth":["Onyx","Geodude","Nidoking"],
        "water":["Squirtle","Magikarp","Totodile"],
        "fire":["Charmander","Fennekin","Flareon"],
        "electric":["Pikachu","Zapdos","Magnemite"]}

print("---------------------------------------------------------------------------------------")
print(" ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  \n▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌\n▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌ ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌\n▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌  ▐░▌          ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌\n▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▐░▌ ▐░▌▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌\n▐░░░░░░░░░░░▌     ▐░▌     ▐░░▌    ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌\n▐░█▀▀▀▀▀▀▀▀▀      ▐░▌     ▐░▌░▌   ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▀   ▐░▌▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌\n▐░▌               ▐░▌     ▐░▌▐░▌  ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌\n▐░▌           ▄▄▄▄█░█▄▄▄▄ ▐░▌ ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌\n▐░▌          ▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌\n ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀    ")
print("---------------------------------------------------------------------------------------\n")
player=Player(input("enter your name: ").capitalize())

#choix starter
x=True
while x:
    print("\n-Earth:1\n-Water:2\n-Fire:3\n-Electric:4")
    choice= input("choose a starter: ")
    if choice=="1":
        player_pik=Pikemon(name["earth"][randint(0,2)],100,"earth",attack["earth"],1)
        print(f"You've got {player_pik}!\n")
        player.addPikemon(player_pik)
        x=False
    elif choice=="2":
        player_pik=Pikemon(name["water"][randint(0,2)],100,"water",attack["water"],1)
        print(f"You've got {player_pik}!\n")
        player.addPikemon(player_pik)
        x=False
    elif choice=="3":
        player_pik=Pikemon(name["fire"][randint(0,2)],100,"fire",attack["fire"],1)
        print(f"You've got {player_pik}!\n")
        player.addPikemon(player_pik)
        x=False
    elif choice=="4":
        player_pik=Pikemon(name["electric"][randint(0,2)],100,"electric",attack["electric"],1)
        print(f"You've got {player_pik}!\n")
        player.addPikemon(player_pik)
        x=False
    else:
        print("please select a valid starter pack\n")
#combat ou quitter
print(player.getPikemon(0).hp)
x=True
while x:
    choice = input("fight:1\ninfo:2\nleave the game:leave\nselect choice: ")
    if choice =="1":
        npc_type=type[randint(0,3)]
        npc_pik_lvl=randint(1,5)
        npc_pik=Pikemon(name[npc_type][randint(0,2)],100,npc_type,attack[npc_type],npc_pik_lvl)
        print(f"\nYou are fighting a {npc_pik.getName()} level {npc_pik.getLVL()}!")
        player_pik=select_pik(player)
        win=fight(player_pik,npc_pik)
        player_pik.resetHP(100)
        if win==True:
            player_pik.TakeXP(5)
            capture(player,npc_pik)

    elif choice =="2":
        print(f"------------------INFO------------------\nYour name:{player.getName()}\nYour Pikemon:{player.getPikemon()}")
        if len(player.getPikemons())==1:
            print(f"-{player.getPikemons()[0]} is level {player.getPikemons()[0].getLVL()}")
        elif len(player.getPikemons())==2:
            print(f"-{player.getPikemons()[0]} is level {player.getPikemons()[0].getLVL()}\n-{player.getPikemons()[1]} is level {player.getPikemons()[1].getLVL()}")
        elif len(player.getPikemons())==3:
            print(f"-{player.getPikemons()[0]} is level {player.getPikemons()[0].getLVL()}\n-{player.getPikemons()[1]} is level {player.getPikemons()[1].getLVL()}\n-{player.getPikemons()[2]} is level {player.getPikemons()[2].getLVL()}")
        print(f"------------------INFO------------------\n")        
    elif choice =="leave":
        x=False
    else :
        print("please select a valid choice\n")


"""

x = "a"
if int(x) == True:
    x = int(x)
else:
    x = x
print(x)