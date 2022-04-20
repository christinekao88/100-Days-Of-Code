from turtle import Turtle


# 繼承Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)
        self.color("white")
    
        
    def go_up(self):
        # 原有的y座標+20
        new_y = self.ycor()+20
        # x座標位置不變
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y)


