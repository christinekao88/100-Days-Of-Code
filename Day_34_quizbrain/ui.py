from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    # 為了獲得quiz_brain的題目而將quiz_brain當作參數傳入
    # 但實際上這裡不知道這個特定對象的數據類型是什麼-->新增數據類型
    # 在初始化class QuizInterface時，必須pass一個quiz_brain object which 數據類型為QuizBrain
    def __init__(self,quiz_brain:QuizBrain):

        # access quiz_brain
        self.quiz = quiz_brain
    
        # make window as property of class
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)

        # canvas
        self.canvas = Canvas(width=300, height=250 ,bg="white")
        self.question_text = self.canvas.create_text(
            150,125,
            # get tkinter text in canvas to wrap
            width=280,
            text="Question", 
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)

        # 只在y軸加，讓畫布的頂部和底部都有填充    
        self.canvas.grid(row=1, column=0,columnspan=2,pady=50)

        # Button
        false_img = PhotoImage(file=r"Day_34_/images/false.png")
        true_img = PhotoImage(file=r"Day_34_/images/true.png")

        self.false_button = Button(image=false_img, highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.true_button = Button(image=true_img, highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        # label
        self.score_label = Label(text="Score:0",bg=THEME_COLOR ,fg="white")
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    # 目的在取得quiz_brain裡的next_question
    def get_next_question(self):

        # 背景色改回白色
        self.canvas.config(bg="white")

        # check 是否有下一個問題
        if self.quiz.still_has_questions():
            # set score
            self.score_label.config(text=f"Score: {self.quiz.score}")

            # 取得題目
            q_text = self.quiz.next_question()

            # 更新畫布text為q_text
            self .canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the question")

            # 進用true和false button
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        # call quiz 的 check_answer
        # 當調用ture_pressed的時候，我們可以把"True"傳過去
        # is_right = self.quiz.check_answer("True")
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        # is_right = self.quiz.check_answer("False")
        self.give_feedback(self.quiz.check_answer("False"))

    def change_bg(self):
        self.convas.itemconfig()

    def give_feedback(self,is_right):
        # if user answer correctly
        if is_right:
            # 背景色改為綠色
            self.canvas.config(bg="green")
        else:
            # 背景色改為紅色
            self.canvas.config(bg="red")

        # time.sleep(1) # 不能亂用time，因為main.py裡有mainloop不斷的在進行，因此必須使用tkinter方法
        # 一秒後，調用next_question
        self.window.after(1000,self.get_next_question)