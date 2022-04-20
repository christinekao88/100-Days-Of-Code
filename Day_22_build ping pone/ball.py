from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor()+ self.x_move
        new_y = self.ycor()+ self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        # 往反方向移動
        self.y_move *= -1
        
    def bounce_x(self):
        # 往反方向移動
        self.x_move *= -1
        # 每次越來越快
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        # 返回原來的速度
        self.move_speed = 0.1
        # 往反方向移動
        self.bounce_x()
