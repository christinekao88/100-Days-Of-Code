import turtle

screen = turtle.Screen()
screen.title("U.S State Game")

# loading image as new shape
image = "100 days/Day_25_50_states/blank_states_img.gif"
screen.addshape(image)

# 此時就可以用image這個shape
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# # 監聽滑鼠的點擊(get_mouse_click_coor) -> 點擊圖片後的x,y已經存在50_states.csv
# turtle.onscreenclick(get_mouse_click_coor)


import pandas as pd
data = pd.read_csv("100 days/Day_25_50_states/50_states.csv")
all_state = data['state'].to_list()
guessed_state=[]

while len(guessed_state)<50:
    # 彈出提示視窗
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50", 
                                    prompt="What's another state's name").title()


    # if answer_state is one of all state
    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # 把正確答案這行拉出來-> row of data
        state_data = data[data.state==answer_state]
        # 可以在抓出屬性x和y->轉為int
        t.goto(int(state_data.x),int(state_data.y))
        # t.write(answer_state)
        # state_data.state為series -> item 回傳第一個元素
        # get row of data (state_data) from a dataframe -> get perticular value(state) from that row (state_data)
        t.write(state_data.state.item())
    
    if answer_state == 'Exit':
         # missing_state = [state for state in all_state if state not in guessed_state]

        missing_state = []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        # Create a dataframe form scratch
        df = pd.DataFrame (missing_state)
        df.to_csv("100 days/Day_25_50_states/missing_state.csv")
        break    


# 保持螢幕打開的另一種方式
# turtle.mainloop()

# screen.exitonclick()