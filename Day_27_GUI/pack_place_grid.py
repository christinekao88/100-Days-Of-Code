"""
Layout management
1. pack()

2. place() -> 利用座標定位
    # my_label.place(x=8,y=8)

3. grid():relative to other componet

* 創建的物件如果沒有指定任何布局的話就不會顯示出來
* 三者間不能混用

"""

from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# 在四周增加padding(增加更多空間)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# 第一列第一行
my_label.grid(column=0, row=0)
# # 沒有改變layout，因為沒有其他的widget  
# my_label.grid(column=5, row=1)

# 在文字四周添加空間
my_label.config(padx=50, pady=50)



#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)









window.mainloop()