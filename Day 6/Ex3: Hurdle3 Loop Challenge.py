#Reeborg's Hurdle 3 Loop Challenge
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def step():
    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()



while at_goal() != True:
    if front_is_clear() != True:
        step()
    else:
        move()
