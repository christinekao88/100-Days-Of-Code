COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. 

from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # generate a new car only every 6th time the game loop runs. 
        # 為了降低產生車子的速度，骰子骰到1的時候時才創造一輛車
        random_chance = random.randint(1,6)
        if random_chance ==1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # No cars should be generated in the top and bottom 50px of the screen 
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


        
               