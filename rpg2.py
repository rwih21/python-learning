import random

currentRoom = "Hall"
gameState = "explore"
playerHp = 100
enemyHp = 0

rooms = {
    "Hall" : {
        "south": "Kitchen",
        "north": "Garden",
        "west": "Backyard",
        "east": "Classroom"
    },
    "Kitchen" : {
        "enemy": "Zombie Chef",
        "north": "Hall",
        "item": "katana"
    },
    "Garden" : {
        "west": "Storage Room",
        "south": "Hall",
        "item": "rose"
    },
    "Storage Room" : {
        "east": "Garden",
        "item": "shovel"
    },
    "Classroom": {
        "west": "Hall",
        "item": "key"
    },
    "Backyard": {
        "east": "Hall",
        "item": "gold"
    }
}

inventory = []

def showInstruction():
    print(" ")
    print("Text-Based RPG")
    print("==============")
    print("Commands:")
    print("go [direction]")
    print("get [item]")
    print(" ")
    print("Example:")
    print("go south")
    print("get potion")
    print(" ")
    
def enemyAttack(playerHp):
    enemyDamage = random.randrange(5,15)
    playerHp = playerHp - enemyDamage
    print(f"{rooms[currentRoom]['enemy']} attacks!")

def checkPlayerHp():
    if playerHp <= 0:
            print(f"Your HP is 0")
            print("You died")
            print("Game Over")
            exit()
    else:
        print(f"Your HP is currently {playerHp}")

print(f"I am in the {currentRoom}")
showInstruction()

while True:

    move = input("> ")
    # print(move.split(" ", 1)) # split the string in the variable 'move' 1 step and stop until space (" ")
    # move = move.split(" ", 1)
    move = move.split()


    if gameState == "explore":
        if move[0] == "get":
            move = move.split(" ", 1)
            if move[1] == rooms[currentRoom]["item"]:
                print(f"You got a {move[1]}")
                inventory.append(move[1]) # add item to inventory with "append"
                rooms[currentRoom]["item"] = ""
            else:
                print(f"You don't see a {move[1]} here!")

        if move[0] == "go":
            if move[1] in rooms[currentRoom]:
                if rooms[currentRoom][move[1]] == "Backyard" and "key" not in inventory:
                    print("You need a key to unlock the door")
                else:
                    currentRoom = rooms[currentRoom][move[1]]
                    print(f"You are now in {currentRoom}")
                    # check item
                    if "item" in currentRoom:
                        print(f"There is an item in this room consisting {len(rooms[currentRoom]['item'])} letters")
                        print(f"Item name starts with {rooms[currentRoom]['item'][0]}")
                    #check enemy
                    if "enemy" in rooms[currentRoom]:
                        gameState = "battle"
                        enemyHp = 100
                        print(f"You have encountered {rooms[currentRoom]['enemy']}")
            else:
                print(f"You can't go {move[1]}")

        if move[0] == "inventory" or move[0] == "inv":
            print(inventory)
    
    else:
        if playerHp <= 0:
            print("You died.")
            print("Game Over.")
            exit()
        elif enemyHp <= 0:
            gameState = "explore"
            print(f"You have defeated {rooms[currentRoom]['enemy']}!")
            del rooms[currentRoom]["enemy"] # del after appear in placeholder, if not then crash
        else:
            if move[0] == "attack":
                enemyHp = enemyHp - 10
                print(f"You attacked {rooms[currentRoom]['enemy']}!")
                print(f"{rooms[currentRoom]['enemy']}'s current HP is {enemyHp}.")

                if enemyHp == 0:
                    gameState = "explore"
                    print(f"You have defeated {rooms[currentRoom]['enemy']}.")
                    del rooms[currentRoom]["enemy"]
                else:
                    # enemy Attack
                    enemyDamage = random.randrange(5,15)
                    playerHp = playerHp - enemyDamage
                    print(f"{rooms[currentRoom]['enemy']} attacks!")
                    # enemyAttack(playerHp)
                    checkPlayerHp()

            elif move[0] == "heal":
                if playerHp == 100:
                    print("Health is full.")

                    # enemy Attack
                    enemyDamage = random.randrange(5,15)
                    playerHp = playerHp - enemyDamage
                    print(f"{rooms[currentRoom]['enemy']} attacks!")
                    checkPlayerHp()

                else:
                    playerHp += 10
                    if playerHp > 100:
                        playerHp = 100

                    # enemy Attack   
                    enemyDamage = random.randrange(5,15)
                    playerHp = playerHp - enemyDamage
                    print(f"{rooms[currentRoom]['enemy']} attacks!")
                    checkPlayerHp()

            elif move[0] == "run":
                runSuccess = random.randrange(1,10)
                if runSuccess > 5:
                    gameState = "explore"
                    print("Escaped Successfully!")
                else:
                    print("Escape failed!")

                    # enemy Attack
                    enemyDamage = random.randrange(5,15)
                    playerHp = playerHp - enemyDamage
                    print(f"{rooms[currentRoom]['enemy']} attacks!")
                    checkPlayerHp()
            else:
                print("Unknown Command.")
    