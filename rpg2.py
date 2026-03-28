import random
import time

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
        "item": "knife"
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
    # print(" ")
    
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

def delayPrint(message):
    print(message)
    time.sleep(1)

print(f"I am in the {currentRoom}")
showInstruction()

while True:
    print(" ")
    move = input("> ")
    # print(move.split(" ", 1)) # split the string in the variable 'move' 1 step and stop until space (" ")
    # move = move.split(" ", 1)


    if gameState == "explore":
        move = move.split(" ", 1)
        if move[0] == "get":
            if move[1] == rooms[currentRoom]["item"]:
                delayPrint(f"You got a {move[1]}")
                inventory.append(move[1]) # add item to inventory with "append"
                rooms[currentRoom]["item"] = ""
            else:
                delayPrint(f"You don't see a {move[1]} here!")

        if move[0] == "go":
            if move[1] in rooms[currentRoom]:
                if rooms[currentRoom][move[1]] == "Backyard" and "key" not in inventory:
                    delayPrint("You need a key to unlock the door.")
                else:
                    currentRoom = rooms[currentRoom][move[1]]

                    if currentRoom == "Backyard": #check what is current room
                        delayPrint("You unlocked the door with a key.")

                    delayPrint(f"You are now in {currentRoom}")

                    #check enemy
                    if "enemy" in rooms[currentRoom]:
                        gameState = "battle"
                        enemyHp = 100
                        delayPrint(f"You have encountered {rooms[currentRoom]['enemy']}!")

                    # check item
                    if gameState == "explore":
                        if "item" in rooms[currentRoom]:
                            delayPrint(f"There is an item in this room consisting {len(rooms[currentRoom]['item'])} letters.")
                            delayPrint(f"Item name starts with {rooms[currentRoom]['item'][0]}.")
            else:
                delayPrint(f"You can't go {move[1]}")

        if move[0] == "inventory" or move[0] == "inv":
            delayPrint(inventory)
    
    else:
        move = move.split()
        delayPrint(" ")
        if playerHp <= 0:
            delayPrint("You died.")
            delayPrint("Game Over.")
            exit()
        elif enemyHp <= 0:
            gameState = "explore"
            delayPrint(f"You have defeated {rooms[currentRoom]['enemy']}!")
            del rooms[currentRoom]["enemy"] # del after appear in placeholder, if not then crash
        else:
            if move[0] == "attack":
                enemyHp = enemyHp - random.randrange(10,15)
                delayPrint(f"You attacked {rooms[currentRoom]['enemy']}!")
                if enemyHp <= 0:
                    gameState = "explore"
                    delayPrint(f"You have defeated {rooms[currentRoom]['enemy']}.")
                    del rooms[currentRoom]["enemy"]
                else:
                    delayPrint(f"{rooms[currentRoom]['enemy']}'s current HP is {enemyHp}.")
                    # enemy Attack
                    enemyDamage = random.randrange(5,15)
                    playerHp = playerHp - enemyDamage
                    delayPrint(f"{rooms[currentRoom]['enemy']} attacks!")
                    # enemyAttack(playerHp)
                    checkPlayerHp()

            elif move[0] == "heal":
                if playerHp == 100:
                    delayPrint("Health is full.")

                    # enemy Attack
                    enemyDamage = random.randrange(5,15)
                    playerHp = playerHp - enemyDamage
                    delayPrint(f"{rooms[currentRoom]['enemy']} attacks!")
                    checkPlayerHp()

                else:
                    playerHp += 10
                    if playerHp > 100:
                        playerHp = 100
                    
                    delayPrint("You healed")
                    delayPrint(f"Your health is now {playerHp}")

                    # enemy Attack   
                    enemyDamage = random.randrange(5,15)
                    playerHp = playerHp - enemyDamage
                    delayPrint(f"{rooms[currentRoom]['enemy']} attacks!")
                    checkPlayerHp()

            elif move[0] == "run":
                runSuccess = random.randrange(1,10)
                if runSuccess > 5:
                    gameState = "explore"
                    delayPrint("Escaped Successfully!")
                else:
                    delayPrint("Escape failed!")

                    # enemy Attack
                    enemyDamage = random.randrange(5,15)
                    playerHp = playerHp - enemyDamage
                    delayPrint(f"{rooms[currentRoom]['enemy']} attacks!")
                    checkPlayerHp()
            else:
                print("Unknown Command.")
    