"""
Day 3 - Beginner - Control Flow and Logical Operators
"""

#---------------------------Odd or Even ---------------------------#
number = int(input("Which number do you want to check? "))

if number%2==1:
    print("This is an odd number.")
else :
    print("This is an even number.")

#--------------------------- BMI Calculator 2.0 ---------------------------# 

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = round(weight /height**2)

if BMI<=18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif 18.5<BMI<=25 :
        print(f"Your BMI is {BMI}, you have a normal weight.")
elif 25<BMI<=30 :
        print(f"Your BMI is {BMI},  you are slightly overweight.")
elif 30<BMI<=35 :
        print(f"Your BMI is {BMI},   you are obese.")
else :
    print(f"Your BMI is {BMI},  you are clinically obese.")

#--------------------------- Leap Year ---------------------------# 
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 ==0 :
    if  year % 100 ==0 :
        if year % 400 ==0 :
            print(f"{year} is leap year")
        else:
            print(f"{year} is not leap year")
    else:
        print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

#---------------------------  Tickets Calculator ---------------------------# 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")


#--------------------------- Pizza Order ---------------------------# 
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N  :")
extra_cheese = input("Do you want extra cheese? Y or N : ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
price=0
if size == "S":
    price+=15
    if add_pepperoni == "Y":
        price+=2
elif size == "M":
    price+=20
    if add_pepperoni == "Y":
        price+=3
elif size == "L":
    price+=25
    if add_pepperoni == "Y":
        price+=3

if extra_cheese == "Y":
        price+=1

print(f"Your final bill is: {price}")

#--------------------------- Love Calculator ---------------------------# 
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
count_true=0
for i in 'true':  
    nam1 = name1.lower().count(i)
    nam2 = name2.lower().count(i)
    true=nam1+nam2
    count_true+=true
    print(f'{i.capitalize()} occurs {true} times ')

count_love=0
for j in 'love':  
    nam1 = name1.lower().count(j)
    nam2 = name2.lower().count(j)
    love=nam1+nam2
    count_love+=love
    print(f'{j.capitalize()} occurs {love} times ')
    
total = int(str(count_true)+str(count_love))

if total <10 or total>90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >=40 and total<=50:
    print(f"Your score is {total}, you are alright together.")
else :
    print(f"Your score is {total}.")

#--------------------------------- Treasure Island -------------------------------# 
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

q1=input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower
if q1=='left':
    q2=input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower
    if q2 =='wait':
        q3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower
        if q3=='red':
            print('You are burned by fired')    
        elif q3=='blue':
            print('You are eaten by beasts')    
        elif q3=='yellow':
            print("You found the treasure! You Win!!!!!!!')    
        else :
            print('Game Over')    
    else:
        print('You are attacked by trout')    
else:
    print('You fell into a hole')


#------------------------------- Mind Test -------------------------------#
print("""
    .".
                         /  |
                        /  /
                       / ,"
           .-------.--- /
          "._ __.-/ o. o\  
             "   (    Y  )
                  )     /
                 /     (
                /       Y
            .-"         |
           /  _     \    \ 
          /    `. ". ) /' )
         Y       )( / /(,/
        ,|      /     )
       ( |     /     /
        " \_  (__   (__       Kao_oaK
            "-._,)--._,)
""")
print("測你的防備心有多重")
print('\n')
Q1=input("假設你要參加一個旅游挑戰賽，來到了一座迷宮面前，你看到的景色是？ A.陽光明媚、芳草遍地 or B.黑霧繚繞、烏雲密佈---> ").lower()
print('\n')
if Q1 == 'a':
    Q3=input("而能幫助你通向迷宮的工具是？A.一個缺了許多木板的吊橋 or B.一個隨意拼搭的獨木橋---> ").lower()
    print('\n')
    if Q3 == 'a':
        Q4=input("好不容易你來到了迷宮門口，看到門上有一塊木板，上面寫著...A.迷失的人在這迷失,相逢的人在這相逢 or B.死並非生的對立，而作為生的一部分永存--->").lower()
        print('\n')
        if Q4 == 'a':
            print("A型\n你是一個心靈毫無防線的人，生平沒有什麼大志，也沒有什麼企圖心，平安順遂的過完一生就是你最大的願望。在與人交流的時候，你總是全身心的付出，很容易相信別人。但是這樣單純的你容易被城府較深的人利用，雖然你沒有害人之心，可是在這個社會裡，防人之心卻是能夠保護你的工具。")
            print('\n')
        elif Q4 == 'b':
            print("B型\n你的防備心比較低，平常做事有點粗枝大葉的你崇尚自由，與人交流的時候總是先一吐為快，而不會顧及後果。你的生活過得比較輕鬆愜意，有時會抱著得過且過的態度，雖然你的周圍目前看似沒有危機，但卻藏著許多隱患。建議可以把目光放長遠一點，多為日後打算。")
            print('\n')
    elif Q3 == 'b':
        Q5=input("於是直覺告訴你...你會被困在這里 A.你會被困在這里 or B.你會在這遇見想見的人--->").lower()
        print('\n')
        if Q5 == 'a':
            print("C型\n你對他人的防備程度大約是50%，你有著寬廣的心胸，樂意幫助朋友擺脫困境，對很多事情都抱著以和為貴的態度，但是如果有人踩到自己的底線，你也會毫不猶豫地反擊。在生活中你對於自己的問題，常常習慣逃避，且不願意向人訴說，有時讓人覺得你神秘莫測。")
            print('\n')
        elif Q5 == 'b': 
              print("D型\n你是一個心思細膩的人，對於身邊的事物能有很好的安排和計劃，因此大部分事情都在你的掌握之中。雖然不能說你的城府極深，但對於複雜的人際關係卻能處理得很好，是個八面玲瓏的人。") 
              print('\n')

elif Q1 == 'b':
    Q2=input("不僅如此，要到達迷宮終點，還必須經過...A.位置險要的懸崖 or B.深淺莫測的河流---> ").lower()
    print('\n')
    if Q2 == 'a':
        Q3=input("而能幫助你通向迷宮的工具是？A.一個缺了許多木板的吊橋 or B.一個隨意拼搭的獨木橋---> ").lower()
        print('\n')
        if Q3 == 'a':
            print("D型\n你是一個心思細膩的人，對於身邊的事物能有很好的安排和計劃，因此大部分事情都在你的掌握之中。雖然不能說你的城府極深，但對於複雜的人際關係卻能處理得很好，是個八面玲瓏的人。") 
            print('\n')
        elif Q3 == 'b':
            print("C型\你對他人的防備程度大約是50%，你有著寬廣的心胸，樂意幫助朋友擺脫困境，對很多事情都抱著以和為貴的態度，但是如果有人踩到自己的底線，你也會毫不猶豫地反擊。在生活中你對於自己的問題，常常習慣逃避，且不願意向人訴說，有時讓人覺得你神秘莫測。")
            print('\n')
    elif Q2 == 'b':
        Q4=input("好不容易你來到了迷宮門口，看到門上有一塊木板，上面寫著...A.迷失的人在這迷失,相逢的人在這相逢 or B.死並非生的對立，而作為生的一部分永存--->").lower()
        print('\n')
        if Q4 == 'a':
            print("B型\\n你的防備心比較低，平常做事有點粗枝大葉的你崇尚自由，與人交流的時候總是先一吐為快，而不會顧及後果。你的生活過得比較輕鬆愜意，有時會抱著得過且過的態度，雖然你的周圍目前看似沒有危機，但卻藏著許多隱患。建議可以把目光放長遠一點，多為日後打算。")
            print('\n')
        elif Q4 == 'b':
            print("A型\n你是一個心靈毫無防線的人，生平沒有什麼大志，也沒有什麼企圖心，平安順遂的過完一生就是你最大的願望。在與人交流的時候，你總是全身心的付出，很容易相信別人。但是這樣單純的你容易被城府較深的人利用，雖然你沒有害人之心，可是在這個社會裡，防人之心卻是能夠保護你的工具。")
            print('\n')