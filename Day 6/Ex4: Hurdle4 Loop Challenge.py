#Reeborg's World Hurdle 4 Loop Challenge
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def step():
    turn_left()
    move()
    while right_is_clear() == False:
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear() == True:
        move()
    turn_left()
    
while at_goal() != True:
    if front_is_clear() != True:
        step()
    else:
        move()
