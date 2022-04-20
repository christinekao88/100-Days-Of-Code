from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0

# 為了把區域變數拿出來使用
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # 取消之前設置的定時器window.after
    window.after_cancel(timer) # -> stop timer

    # timer_text 00:00
    canvas.itemconfig(timer_text,text='00:00')

    # timer_label "Timer"
    title_label.config(text="Timer") 

    # reset check_marks
    check_mark.config(text="")

    # reset working session
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    long_break_sec = LONG_BREAK_MIN*60
    short_break_sec = SHORT_BREAK_MIN *60
    work_sec = WORK_MIN*60

    if reps %8 ==0:
        count_down(long_break_sec)
        title_label.config(text="LONG BREAK",fg=RED)

    elif reps %2 ==0:
        count_down(short_break_sec)
        title_label.config(text="SHORT BREAK",fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="WORK",fg=GREEN)

   
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # 時間格式00:00
    count_min = math.floor(count/60) # 只取整數部分
    count_sec = count % 60

    # python is dynamic typing 
    if count_sec <10:
        count_sec = f'0{count_sec}'

    # 改變canvas的設置方法 -> timer_text改成count
    canvas.itemconfig(timer_text,text=f'{count_min}:{count_sec}')

    if count >0:
        # 為了使用區域變數
        global timer
        # 1秒後調用函數count_down,然後傳入count-1
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks=''
        # 取得正確的work sessions = math.floor(reps/2)
        for _ in range(math.floor(reps/2)):
            marks+="✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("Pomodoro")
# bg=background
window.config(padx=100,pady=50,bg=YELLOW)

# 等待指定毫秒(ms)後，呼叫指定function
def say(thing):
    print(thing)
window.after(1000,say,"hello") # 一秒後呼叫say function並把hello傳入say(thing=hello)

def say_1(a,b,c):
    print(a,b,c)    
window.after(1000,say_1,3,5,8) 

# highlightthickness->去除邊框線
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)

# tk裡一種讀取文件的方法
tomato_img = PhotoImage(file="100 days/Day_28/tomato.png")

# 將圖片放在中心(200/2)
canvas.create_image(100,112,image=tomato_img)

timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

title_label = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,50,"bold"))
title_label.grid(column=1, row=0)

# fg->前景
check_mark = Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,20,"bold"))
check_mark.grid(column=1, row=3)

#Button
start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0, row=2)

#Button
reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2, row=2)

# 每毫秒檢查上面發生什麼事
window.mainloop()