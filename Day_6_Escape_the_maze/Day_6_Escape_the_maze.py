"""
Day 6 - Beginner - Python Functions & Karel
"""

# defining function
def my_function():
        print("hello")
        print("bye")

# Calling function
my_function()


"""
reeborg :https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_in_front() and right_is_clear():
        turn_right()
    if wall_on_right() and front_is_clear():
        move()
    else:
        turn_left()
    while not wall_on_right():
        turn_right()
        move()
        turn_right()
        move()


#### maze ######
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    if wall_on_right() and front_is_clear():
       turn_left()
    if wall_in_front() and  wall_on_right():
        turn_left()
    if wall_in_front() and right_is_clear():
        turn_right()
"""