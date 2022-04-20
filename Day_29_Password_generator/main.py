import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import choice,randint,shuffle

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    # new_list = [new_item for item in range in range(nr_letters)]
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    # pick random symbols in new list 做 range(nr_symbols)次
    symbols_letters = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_letters = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters+symbols_letters+numbers_letters
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password) 

    # 自動複製字串password
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
import pandas as pd
import json

def save():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    data_dict= {
        website_data :{
            "Email":email_data,
            "Password":password_data
        }
    }

    if len(website_data)==0 or len(password_data)==0:
        messagebox.showinfo(title="OOPS!!" ,message="Please make sure you haven't left any fields empty!")
    else:
        # is_ok = messagebox.askokcancel(title=website_data ,message=f'These are the details entered:\n Email:{email_data}'
        #         f"\nPassword:{password_data}\nIs it ok to save?")
        # if is_ok:
        #     # 創建一個檔案data.txt, mode=append
        #     with open("100 days/Day_29_Password_generator/data.txt","a") as data_file:
        #         data_file.write(f" {website_data} | {email_data } | {password_data} \n")
        
        # 試圖open file
        try:
            with open("Day_29_Password_generator/data.json","r") as data_file:
                # Reading old data (json) -> 反序列化為python dictionatry (easily change information)
                new_data = json.load(data_file)

        # 如果找不到file的話，創建一個file
        except FileNotFoundError:
            with open("Day_29_Password_generator/data.json","w") as data_file:
                # write json : 把data_dict 寫到data_file
                json.dump(data_dict,data_file,indent=4)

        # 只有try block 運行成功才會執行 (有new_data時)
        else:        
            #  Updating old data with new data (利用新的數據來更新字典)
            new_data.update(data_dict)

            with open("Day_29_Password_generator/data.json","w") as data_file:
                # Saving updating data (把new_data再寫回原有data)
                json.dump(new_data,data_file,indent=4)
        finally:  
            website_entry.delete(0,END) # delete的範圍
            password_entry.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_data = website_entry.get()
    try:
        with open("100 days\Day_29_Password_generator\data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error" ,message=f"No data file found")
    else:
        if website in data:
            messagebox.showinfo(title=website ,message=f"Email is : {data[website]['Email']}\n Password is : {data[website]['Password']}")
        else:
            messagebox.showinfo(title="Error" ,message=f"No details for the {website} exists")
    
# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *  # *import所有class ,constant 沒有import messagebox 
from tkinter import messagebox 

window =Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200,highlightthickness=0)
lock_img = PhotoImage(file="100 days\Day_29_Password_generator\logo.png")

# 將圖片放在position中心(200/2)
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0)

# website
website = Label(text="Website:")
website.grid(column=0,row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1,row=1)
website_entry.focus() # 增加游標

# email/username
email = Label(text="Email/Username:")
email.grid(column=0,row=2)

email_entry = Entry(width=35)
email_entry .grid(column=1,row=2,columnspan=2)
# 預設文字 insert(index,text) 0:在開始的位置插入文字  END:在最後的位置插入
email_entry.insert(0,'s100250@hotmail.com.tw') 

# password
password = Label(text="Password:")
password.grid(column=0,row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

# Button - generate
generate_password = Button(text="Generate Password",command=generate_password)
generate_password.grid(column=2,row=3)

# Button - add -> 需要橫跨兩個column
add = Button(text="Add",width=36, command=save)
add.grid(column=1,row=4,columnspan=2)

# Button - Search 
search  = Button(text="Search ",width=16,command=find_password)
search.grid(column=2,row=1)

window.mainloop()
