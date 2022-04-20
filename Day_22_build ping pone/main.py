from turtle import Screen
from paddle import Paddle
from ball import Ball
import random
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")

# 關閉動畫->後面就必須手動刷新螢幕，不然甚麼都看不到
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    # 手動刷新螢幕，顯示目前螢幕發生了甚麼事
    screen.update()
    ball.move()

    # Detect collision with wall (ball寬度20)
    if ball.ycor() >280 or ball.ycor() <-280:
       ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor() >320 or ball.distance(l_paddle)<50 and ball.xcor() >-320:
       ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() >380 :
       ball.reset_position()
       scoreboard.l_point()
           
    # Detect L paddle misses
    if ball.xcor() <-380 :
       ball.reset_position()
       scoreboard.r_point()


screen.exitonclick()