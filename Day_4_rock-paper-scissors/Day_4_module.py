"""
Day 4 - Beginner - Randomisation and Python Lists
"""

#------------------------------- Randomisation -------------------------------# 
import random
# 1-100
random_integer=random.randint(1,100)
print(random_integer)

# 0.000000000000-0.99999999999999
random_float=random.random()
print(random_float)

# how to get random float in 0.00000000000-4.9999999999999
randomFloat = random_float*5
print(randomFloat)

#------------------------------- import own module -------------------------------# 
import Day_4_my_module
# printing all variables and function names of the  module
print(dir(Day_4_my_module))
print(Day_4_my_module.pi)

#------------------------------- Heads or Tails -------------------------------# 
#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
import random
choice = random.randint(0,1)
if choice ==0:
    print('Heads')
else:
    print('Tails')


#------------------------------- Who's Paying  -------------------------------# 
# Split string method # https://www.askpython.com/python/string/convert-string-to-list-in-python
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random
# print(names)
# print(type(names))
# print(len(names))

# remember from 0
pay = random.randint(0,len(names)-1)

# or you caan use
pay = random.choice(names)

print(f"{names[pay]} is going to buy the meal today!")

#-------------------------------Treasure Map -------------------------------#
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizonal = int(position[0])
vertical = int(position[1])

# index error-> map[vertical]
# 列出指定的list ->print(map[vertical-1])

# way 1
select_row = map[vertical-1]
select_row[horizonal-1]='x'

# way 2
map[vertical-1][horizonal-1]='x'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

