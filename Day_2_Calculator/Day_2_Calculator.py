"""
Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings
"""
#--------------------------- BMI Calculator ------------------------------#
# π¨ Don't change the code below π
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# π¨ Don't change the code above π

#Write your code below this line π
print(type(height))
print(type(weight))

# ζ­€ζweightεheightδ»ζ―ε­δΈ²οΌθ2ζ―ζΈε­
bmi = weight/(height**2)
bmi = int(weight/(height**2))

bmi = float(weight)/float(height)**2
print('BMI is '+str(int(bmi)))

#--------------------------- Life Calculator ---------------------------#
# π¨ Don't change the code below π
age = input("What is your current age?")
# π¨ Don't change the code above π

#Write your code below this line π
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

# integer (η¨εΊη·δ»£ζΏιθειε€§ζΈε­)
print(123_456_7789)

# float
# bollean


