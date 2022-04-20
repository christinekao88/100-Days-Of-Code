# import tkinter
# my_label = tkinter.Label()

from tkinter import *
# my_label = Label()

#Creating a new window and configurations -> tkinter module的Tk() Class
window = Tk()

window.title("My first GUI Program")

# scale窗口大小
window.minsize(width=500,height=300)

# Create Label 
my_label = Label(text="I Am a Label",font=("Arial",24,"bold"))
my_label.config(text="This is new text")

# The Packer 為幾何管理系統
# Put Label:要將標籤打包到螢幕上才會顯示 -> 預設為center
my_label.pack(side="bottom")
# 佔據整個螢幕
my_label.pack(expand=True)

def button_clicked():
    print("I Got Clicked")

    # Change label property
    # my_label['text'] = 'Button Got clicked'
    # or
    # my_label.config(text='Button Got clicked')

    # 獲取entry傳回內容
    new_text = input.get()
    my_label.config(text=new_text)
    my_label.pack(expand=True)


# Create Button 
button = Button(text="Click Me", command=button_clicked) # 只需要name of function，不需要call function
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with -> END為INDEX以找出所指的定項目
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30) # 5行
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0 (取得所有文字in the box) -> 從第一行的零號字元開始
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())

#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton-> Pick different value
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()






# 將窗口保持在螢幕上
window.mainloop()