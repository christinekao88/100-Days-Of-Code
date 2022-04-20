#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# 在 Python 中，字串的最前方加上 r，代表的是這是一個完整的字串
with open(r"100 days/Day_24_mail_merge/Input/Names/invited_names.txt") as n:
    # readlines 將文件中所有行以list的方式返回
    names = n.readlines()

with open(r"100 days/Day_24_mail_merge/Input/Letters/starting_letter.txt") as s:
    letter = s.read()
    for name in names:
        name = name.strip()
        text = letter.replace("[name]", name)
        with open(f"100 days/Day_24_mail_merge/Output/{name}.txt",'w') as o:
            o.write(text)
