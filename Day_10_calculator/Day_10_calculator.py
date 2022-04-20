"""
Day 10 - Beginner - Functions with Outputs

"""
#------------------------- Calculator with while loop ------------------------#
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

from Day_10_art import logo

def calculator():
    print(logo)
    
    num_first = float(input("What's the first number ? : "))

    for key in operations:
        print(key)

    cal_continue=True
    while cal_continue:
        symbol = input("Pick an operation from the line before : ")

        num_next = float(input("What's the next number ? : "))

        calculation=operations[symbol]
        answer=calculation(num_first,num_next)

        print(f"{num_first}{symbol}{num_next} = {answer}")

        choose = input(f'Type "y" to continue calculating with {answer} or "n" to start a new calculator :' ).lower()

        if choose=='y':
            num_first= answer
        else:
            cal_continue=False
            # 再次呼叫自己
            calculator()

calculator()