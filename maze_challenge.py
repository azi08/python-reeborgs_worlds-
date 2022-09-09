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
