"""
Day 1 - Beginner - Working with Variables in Python to Manage Data
"""
#--------------------- Band Name Creator ---------------------#
#1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")
#2. Ask the user for the city that they grew up in.
city = input("What's name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet = input("What's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city + " " + pet)


# 計算字串長度1
letter=0
for i in (input("what's your name ? ")):
  letter+=1
print(letter)

# 計算字串長度2
print(len(input("what's your name ? ")))

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c=a
a=b
b=c
#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

