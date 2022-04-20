import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('100 days/Day_18_Turtle/image.jpg', 30)

rgb_color = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_color.append(new_color)

# print(rgb_color)

import turtle  as turtle_module
import random

john = turtle_module.Turtle()

# 記得要切換顏色模式->要不然會raise TurtleGraphicsError
turtle_module.colormode(255)

john.speed(10)
john.hideturtle()

john.penup()

# 往左下的方向
john.setheading(225)
# 往前移動250到想要開始的位置
john.forward(300)

# 轉回原本的方向
john.setheading(0)

number_of_dots = 100

for doc_count in range(1,number_of_dots+1):
    john.dot(20,random.choice(rgb_color))
    john.forward(50)
    
    if doc_count %10 == 0 :
        # 到上一條的起始點    
        # 1.往上的方向
        john.setheading(90)
        john.forward(50)
        # 2.再往左的方向
        john.setheading(180)
        john.forward(500)
        john.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()