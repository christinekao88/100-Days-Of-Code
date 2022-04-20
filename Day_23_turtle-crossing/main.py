import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect when the turtle player collides with a car(20*40) and stop the game if this happens.
    for car in car_manager.all_cars:
        if player.distance(car)<20:
            game_is_on = False
            scoreboard.game_over()


    # Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). 
    # When this happens, return the turtle to the starting position and increase the speed of the cars. 
    # Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. 
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()


screen.exitonclick()