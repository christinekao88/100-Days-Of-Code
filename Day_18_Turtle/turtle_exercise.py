# from turtle (module) import Turtle , Screen(class)
from turtle import Turtle , Screen , colormode

import random 
timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")


# 畫正方形
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# 畫虛線
# for i in range(15):
#     timmy.forward(10)
#     # 空白
#     timmy.penup()
#     timmy.forward(10)
#     # 下筆
#     timmy.pendown()



color=["blue","medium blue","red","green","light blue","gold","light coral","blue violet","tomato","dark orange","olive drab"]
# 多邊形
# def draw_shape(num_side):
#     for i in range(num_side):
#         timmy.right(360/num_side)
#         timmy.forward(100)

# for n in range(3,11):
#     timmy.color(random.choice(color))
#     draw_shape(n)

# E = 0, N = 90, W=180, S = 270
# direction=[0,90,180,270,360]
# timmy.speed(10)
# # timmy.width(20)
# timmy.pensize(20)
# for i in range(200):
#     timmy.color(random.choice(color))
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))
        

# 更改顏色模式為rgb
colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color=(r,g,b)
    return color

# direction=[0,90,180,270,360]
timmy.speed(20)
# timmy.width(20)
timmy.pensize(2)
# for i in range(200):
#     timmy.color(color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timmy.circle(120)
        timmy.setheading(timmy.heading()+size_of_gap)
        timmy.color(random_color())
    
    
draw_spirograph(15)


screen = Screen()
screen.exitonclick()
