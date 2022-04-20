# 從別的模組匯入class()
import turtle
# turtle模組裡的class()，叫做Turtle(字首為大寫)
# timmy object 現在有一隻叫做timmy的烏龜
timmy = turtle.Turtle()
print(timmy)

from turtle import Turtle, Screen
john = Turtle()
print(john)
# method : shape
john.shape("turtle")
john.color("orange")
john.forward(100)
# Object : my_screen
my_screen = Screen()

# attributes : canvheight
print(my_screen.canvheight)

# method : exitonclick()
my_screen.exitonclick()
