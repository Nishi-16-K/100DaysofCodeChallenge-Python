#Reeborg's World Hurdle 2 Loop Challenge using while loop

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def step():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()



while at_goal() == False:
    step()
