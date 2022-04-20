"""
Day 5 - Beginner - Python Loops
"""

#------------------------ Average Height ------------------------# 
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
total_height=0
for total in student_heights:
    total_height+=total
# print(total_height)

num=0
for len in student_heights:
    num+=1
# print(num)
print('Average Height is '+str(total_height/num))


#------------------------ Highest Score ------------------------# 
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

 # store highest_score
highest_score=0 
for score in student_scores:
    if score>highest_score:
        highest_score=score
print(f'The highest score in the class is: {highest_score}')


#------------------------ Adding Evens ------------------------# 
total=0
for number in range(2,101,2):
    total+=number
print(total)

for number in range(1,101):
    # need to check both first
    if  number % 3 ==0 and  number % 5 ==0:
        print("FizzBuzz")
    elif  number % 5 ==0:
        print("Buzz")
    elif  number % 3 ==0 :
        print("Fizz")
    else:
        print( number)

#------------------------ Password Generator Project ------------------------#
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# way 1
passward_order=[]
for letter in range(1, nr_letters+1):
    num=random.randint(1,len(letters)-1)
    passward_order.append(letters[num])
for symbol in range(1, nr_symbols+1):
    num=random.randint(1,len(symbols)-1)
    passward_order.append(symbols[num])
for number in range(1, nr_numbers+1):
    num=random.randint(1,len(numbers)-1)
    passward_order.append(numbers[num])
passward_order = ''.join(passward_order)
print(passward_order)

# way 2
password=''
for char in range(1,nr_letters+1):
    password+=random.choice(letters)
for char in range(1,nr_symbols+1):
    password+=random.choice(symbols)
for char in range(1,nr_numbers+1):
    password+=random.choice(numbers)
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_random = ''
for char in password:
    password_random+=random.choice(password)
print(password_random)

# way 2
password_list=[]
for char in range(1,nr_letters+1):
    # 兩種加到list的方式都可以
    password_list.append(random.choice(letters))
for char in range(1,nr_symbols+1):
    password_list+=random.choice(symbols)
for char in range(1,nr_numbers+1):
    password_list+=random.choice(numbers)

# reorder list
random.shuffle(password_list)
print(password_list)

password_list = ''.join(password_list)
print(password_list)