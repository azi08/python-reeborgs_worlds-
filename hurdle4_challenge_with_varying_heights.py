def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    x = 0
    while wall_in_front():
        turn_left()
        move()
        x += 1
        turn_right()
    else:
        move()
        turn_right()
        while x > 0:
            move()
            x -= 1
    turn_left()
    
while not at_goal():    
    if front_is_clear():
        move()  
    else:
        jump()
        
       
 ###########OR###############

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    x = 0
    turn_left()
    while wall_on_right():
        move()
        x += 1
    else:
        turn_right()
        move()
        turn_right()
        while x > 0:
            move()
            x -= 1
    turn_left()
    
while not at_goal():    
    if front_is_clear():
        move()  
    else:
        jump()
