from datetime import time
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- Read data ------------------------------- #
try:
    data = pd.read_csv("Day_31_Capstone Project/data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("Day_31_Capstone Project/data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")

current_card = {}

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("Day_31_Capstone Project/data/words_to_learn.csv",index=False)

    next_card()
    


def next_card():
    # current_card 被鎖在function裏 -> 創建global current_card 
    global current_card , flip_timer
    # 每一次新卡片時，使之前的定時器flip_timer失效
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    # 每次執行再次回到卡片正面
    canvas.itemconfig(front_image,image=card_front_img)
    # 設置新的timer -> 3000 毫秒後(=3秒) ，執行flip_card()
    flip_timer = window.after(3000,func=flip_card)   
    
def flip_card():
    # To change the image:
    canvas.itemconfig(front_image,image=card_back_img)
    # To change the text:
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *  # *import所有class ,constant 沒有import messagebox 

window =Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

# 3000 毫秒後(=3秒) ，執行flip_card()
flip_timer = window.after(3000,func=flip_card)

# Create canvas object : 創建畫布，可以疊加東西在上面
canvas = Canvas(width=800,height=526)
# 從文件中創建照片圖像->不能再function內建立，因為執行完就結束了，so it will not work.
card_back_img = PhotoImage(file="Day_31_Capstone Project/images/card_back.png")
card_front_img = PhotoImage(file="Day_31_Capstone Project/images/card_front.png")

# 在畫布裡創建圖像
front_image = canvas.create_image(400,260,image=card_front_img)
# back_image = canvas.create_image(400,260,image=card_back_img)

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2) # column橫跨兩格

# 在畫布裡創建文字-> 為了要修改創建變數
card_title = canvas.create_text(400,150,text="title",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))

# Button
wrong_button_img = PhotoImage(file="Day_31_Capstone Project/images/wrong.png")
wrong_button = Button(image=wrong_button_img,highlightthickness=0,command=next_card)
wrong_button .grid(column=0,row=1)

right_button_img = PhotoImage(file="Day_31_Capstone Project/images/right.png")
right_button = Button(image=right_button_img,highlightthickness=0,command=is_known)
right_button .grid(column=1,row=1)

# 再進入主循環之前調用叫出下一張卡，佔位文字被替代掉
next_card()

window.mainloop()