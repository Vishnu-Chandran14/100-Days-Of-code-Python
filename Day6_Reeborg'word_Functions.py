#copy the link in browser to view code and usage in game method

#define the function to avoid the repeatative in full code

#function to turn the robot in right side.

def turn_right():
    turn_left()
    turn_left()    
    turn_left()
    


while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
