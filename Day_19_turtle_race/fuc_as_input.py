def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def divide(n1,n2):
    return n1/n2

def multiply(n1,n2):
    return n1*n2

# 傳入function -> 此時calculator為 Higher order function
def calculator(n1,n2,fun):
    return fun(n1,n2)

# 只需輸入function名字
result = calculator(4, 6, add)
print(result)

from turtle import Turtle, Screen

marry = Turtle()
screen = Screen()

def move_forwards():
    marry.forward(10)

def move_backwards():
    marry.backward(10)

def turn_left():
    # 每次左轉10度
    new_heading = marry.heading()+10
    marry.setheading(new_heading)

def turn_right():
    new_heading = marry.heading()-10
    marry.setheading(new_heading)

def clear_draw():
    marry.clear()
    marry.penup()
    marry.home()
    marry.pendown()

screen.listen()
screen.onkey(key="w",fun = move_forwards)
screen.onkey(key="s",fun = move_backwards)
screen.onkey(key="a",fun = turn_left)
screen.onkey(key="d",fun = turn_right)
screen.onkey(key="c",fun = clear_draw)


screen.exitonclick()