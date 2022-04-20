# 3. Control the snake
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall
# 7.  Detect collision with tail

from turtle import Screen , Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# turn off animation : 0
screen.tracer(0)

starting_position = [(0,0),(-20,0),(-40,0)]

segments = []

###### 1. Create a snake body ############
for position in starting_position:
    snake_body = Turtle(shape="square")
    snake_body.color("white")
    snake_body.penup()
    snake_body.goto(position)
    segments.append(snake_body)

####### 2. Move the snake ############
import time
game_is_on = True
while game_is_on:
    # 直到update螢幕才會刷新(移動完才刷新)，才看得到東西
    screen.update()
    time.sleep(0.1)
    
    # 讓蛇的尾巴會跟著頭的方法-> 第三節取代第二節，以此類推，最後在移動第一節
    # reverse orders segments 順序為(start=最後,stop=最頭,step=-1) 
    for seg_num in range(len(segments)-1, 0, -1):
        # 得到前一個方塊的x,y 
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)
    
    # 最後移動第一節 
    segments[0].forward(20)


screen.exitonclick()