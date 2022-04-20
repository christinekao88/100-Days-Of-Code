"""
Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings
"""
#--------------------------- BMI Calculator ------------------------------#
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(type(height))
print(type(weight))

# 此時weight和height仍是字串，而2是數字
bmi = weight/(height**2)
bmi = int(weight/(height**2))

bmi = float(weight)/float(height)**2
print('BMI is '+str(int(bmi)))

#--------------------------- Life Calculator ---------------------------#
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
year_left = (90-int(age))
days = year_left*365
weeks = year_left*52
months = year_left*12
print(f"you have {days} days ,  {weeks} weeks, {months} months left.")

#--------------------------- Tip Calculator ---------------------------#
print("Welcome to the tip calculator!")
bill = float(input('what was th total bill ? $'))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
pay = round((bill +bill * (tip/100))/people,2)
print(f"Each person should pay: ${pay}")


################################################################################
#Data Types

# string
print("123456")

# integer (用底線代替逗號分隔大數字)
print(123_456_7789)

# float
# bollean


