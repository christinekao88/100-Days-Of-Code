"""
Day 10 - Beginner - Functions with Outputs

"""
#------------------------- Function without output -------------------------#
def format_name(f_name,l_name):
    first_name=f_name.title()
    last_name=l_name.title()
    print(f"{first_name} {last_name}")

format_name("cHIOSJ","dkoK")

# Function with output
def format_name(f_name,l_name):
    first_name=f_name.title()
    last_name=l_name.title()
    return f"{first_name} {last_name}"

# store output with viable
output=format_name("cHIOSJ","dkoK")
print(output)

#------------------------- Days in Month -------------------------#
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return False
            else:
                return True
        else:
            return False
    else:
        return True

def days_in_month(year,month):
    """
    Here is docstring
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    
    if month>12 or month<1:
        return "Invalid month"
    if is_leap(year) == True and month ==2:
        return 29
    else:
        return month_days[month-1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

#------------------------- Calculator -------------------------#
# add
def add(n1,n2):
    return n1+n2

# subtract
def subtract(n1,n2):
    return n1-n2

# multiply
def multiply(n1,n2):
    return n1*n2

# divide
def divide(n1,n2):
    return n1/n2

operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide,
}

num1 = int(input("What's the first number ? : "))

for key in operations:
    print(key)

symbol = input("Pick an operation from the line before : ")

num2 = int(input("What's the first number ? : "))

calculation=operations[symbol]
first_answer=calculation(num1,num2)

print(f"{num1}{symbol}{num2} = {first_answer}")

symbol = input("Pick another operation from the line before : ")

num3 = int(input("What's the next number ? : "))

# second_answer = 5 * 3 = 18 (correct)
calculation=operations[symbol]
second_answer=calculation(first_answer,num3)

# second_answer = 2 * 3 * 3 = 18 (wrong)
second_answer=calculation(calculation(num1,num2),num3)

print(f"{first_answer}{symbol}{num3} = {second_answer}")

