from turtle import Turtle, Screen

screen = Screen()

# 中心點為0,0 ， (+250,-250)=500
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color : ")
colors=["red","green","blue","yellow","purple","orange"]

all_turtle = []
y=-130
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color)
    turtle.goto(x=-200,y=y)
    all_turtle.append(turtle)
    y+=55

is_race_on = False
if user_bet:
    is_race_on = True
import random
while is_race_on:
    # 如果x座標>230
    if turtle.xcor()>230:
        is_race_on = False
        # color include pencolor and fillcolor
        winning_color = turtle.pencolor()
        if winning_color == user_bet:
            print(f"You've won! The {winning_color } is winner")
        else:
            print(f"You've lost! The {winning_color } is winner")

    for turtle in all_turtle:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()