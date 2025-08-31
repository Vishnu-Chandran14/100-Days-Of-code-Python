#100-Days-Of-code-Python
#Documenatation of Python Course-Learning 100 days of code



print(r'''
 _                                                           
| |                                                          
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __  
| __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \ 
| |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/ 
                                                      | |    
                                                      |_|   
-------------------------------------------------------------------
''')

print("Welcome to Treasure Island.Your mission is to find the treasure!\n")
Direction = input("You're at a cross road. Where do you want to go? "
                  "Type 'Left' or 'Right'\n").lower()
if Direction =="left":
    print("You've come to a lake."
          "There is an island in the middle of the lake.")
    level_1 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if level_1 == "wait":
        print("You arrive at the island unharmed. "
              "There is a house with 3 doors. One red, one yellow and one blue.\n")
        level_2 = input("Which colour do you choose?").lower()
        if level_2 == "red":
            print("Burned by fire.Game Over.")
        elif level_2 == "blue":
            print("Eaten by beasts.Game Over.")
        else:
            print("You win")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("Game Over")





