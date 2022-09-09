#This is the solution for the Maze Challenge on Reeborg's World
#The link is https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

#####First Solution####

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear() == False:
        turn_left()
        if front_is_clear() == False:
            turn_left()
            if front_is_clear() == False:
                turn_left()
            else:
                move()
                turn_right()
        else:
           move()
           turn_right()
    else:
        move()
        turn_right()

        
###Second Solution###
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def deadEnd():
    if (front_is_clear() == False) and (wall_on_right() == True):
        turn_left()
        if not front_is_clear():
            turn_left()
            move()
            return True
            
while not at_goal():
    if front_is_clear() and :
        move()
        if deadEnd():
            while right_is_clear():
                turn_right()
                move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
