#Reeborg's World Hurdle 1 Loop Challenge using for loop

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


for in in range(0,5):
    step()
