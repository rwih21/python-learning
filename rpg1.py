class Player:
    def __init__(self, name, playerClass):
        self.name = name
        self.playerClass = playerClass
        self.hp = 100
        if(playerClass == "Mage"):
            self.str = 1
            self.int = 3
        elif(playerClass == "Rogue"):
            self.str = 3
            self.int = 1
        else:
            self.str = 2
            self.int = 2
    
    def attack(self, target):
        print(f"{self.name} attacks {target.name}")
        target.hp = target.hp - (10 + (0.25 * self.str))
        print(f"{target.name}'s hp is currently {target.hp}")
    
    def magic(self, target):
        print(f"{self.name} casts a spell on {target.name}")
        target.hp = target.hp - (10 + (0.25 * self.int))
        print(f"{target.name}'s hp is currently {target.hp}")


player1 = Player("Orin", "Rogue")

player2 = Player("Demooni", "Mage")

player1.attack(player2)

player2.attack(player1)

player1.attack(player2)

player2.magic(player1)
