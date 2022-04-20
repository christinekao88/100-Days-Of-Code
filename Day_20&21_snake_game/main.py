from turtle import Screen , Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# turn off animation : 0
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# 3. Control the snake
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    # 直到update螢幕才會刷新(移動完才刷新)，才看得到東西
    screen.update()
    # 每0.1秒更新一次螢幕 (delay update)
    time.sleep(0.1)

    # 每刷新一次，往前一步
    snake.move_snake()

    # 5. Detect collision with food by 掌握蛇頭和食物之間的距離
    if snake.head.distance(food) < 15 : # food size 10x10
        # 撞到食物時，食物換位置
        food.refresh()
        snake.extend()
        scoreboard.increaseScore()

    # 6. Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        # 蛇停止移動
        game_is_on = False
        scoreboard.game_over()

    # 7. Detect collision with tail
    # if head collides with any segment in the tail 
    for segment in snake.segments[1:]:
        # 略過蛇頭
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    
    
screen.exitonclick()