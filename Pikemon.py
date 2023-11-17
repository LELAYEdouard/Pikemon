from random import randint
from math import floor

class Pikemon:
    def __init__(self,name,type:str,attack,lvl):
        self.type=type
        self.name=name
        self.attack=attack
        self.lvl=lvl
        self.xp=0
        self.goal_lvl=10+(self.lvl-1)*5 
        self.iv=randint(1,31)
        self.base=randint(1,255)
        self.hp=floor((2*(self.base+self.iv)*self.lvl)/50)+self.lvl+100
        self.tiredness=100
    def getName(self):
        return self.name.capitalize()

    def TakeXP(self,xp):
        self.xp+=xp
        if self.xp ==self.goal_lvl:
            self.xp=0
            self.lvl+=1
            self.goal_lvl+=5

    def TakeDamage(self,nb):
        self.hp-=nb
        if self.hp<0:
            self.hp=0

    def getAttack(self,index):
        return self.attack[index]

    def Attack(self,attack_name):
        for elt in self.attack:
            if elt[0] == attack_name  :
                if self.tiredness > elt[2]: 
                    x = round(elt[1]*(1+self.lvl/10))
                    self.tiredness-=elt[2]
                    return x
                else: 
                    print("too tired, dodge to regain tire points\n")
                    return 0

    def resetHP(self):
        self.hp = floor((2*(self.base+self.iv)*self.lvl)/50)+self.lvl+100
    
    def __repr__(self):
        return self.getName()
    
    