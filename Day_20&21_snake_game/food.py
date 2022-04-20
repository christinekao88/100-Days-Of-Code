from turtle import Turtle
import random

# 繼承class Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    # food random location
    def refresh(self):
        # 畫布寬600(-300~+300),往內縮一點蛇蛇才不會撞牆壁
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)