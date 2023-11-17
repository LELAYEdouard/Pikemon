from initinput import intinput

class Player:
    def __init__(self, name):
        self.deck = []
        self.name = name

    def getPikemon(self, i):
        return self.deck[i]

    def addPikemon(self, pikemon):
        if len(self.deck)<3:
            self.deck.append(pikemon)
        else:
            x = True
            while x:
                print("Maximum Pikemon in inventory, please delete one or cancel")
                choice = input("delete: 1\ncancel: 2\nchoice: ")
                if choice == "1":
                    print(f"select which one you want to delete:")
                    for i in range(len(self.deck)):
                        print(f"{self.deck[i]}(lvl {self.deck[i].lvl()}): {i+1} ")

                    choice = intinput("choice: ")-1
                    
                    if choice < len(self.deck):
                        self.deck.pop(choice)
                        x = False
                    else:
                        print("select a valid choice")
                    
                elif choice =="2":
                    print(f"You released {pikemon}!")
                    x = False
                else:
                    print("select a valid choice")

    def getName(self):
        return self.name
    
    def __repr__(self):
        return self.getName()
    
    def BestPiklvl(self):
        max_lvl=0
        for i in range(len(self.deck)):
            if self.getPikemon(i).lvl>max_lvl:
                max_pik=self.getPikemon(i)
                max_lvl=max_pik.lvl
        return max_lvl
