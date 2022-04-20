"""
Day 8 - Beginner - Function Parameters & Caesar Cipher
"""

#----------------------- Function Parameters ------------------------#
# Call the greet() function and run your code.

def greet():
    print("hi")
    print("hello")
    print("yo")

greet()

def greet_with_name(name):
    print(f"hi {name}")
    print(f"hello {name}")
    print(f"yo {name}")

greet_with_name('christine')

def greet_with_name_loc(name,location):
    print(f"hi {name} in {location}")
    print(f"hello {name} in {location}")
    print(f"yo {name} in {location}")

greet_with_name_loc('christine','Taipei')

greet_with_name_loc(location='Taipei',name='Bob')

#-------------------------- Area Calc ------------------------------#

# Write your code below this line 👇
import math

def paint_calc(height,width,cover):
   #number of cans = (wall height ✖️ wall width) ÷ coverage per can.
   # 無條件進位 
    number__cans=math.ceil((height*width)/cover)
    print(f"You'll need {number__cans} cans of paint.")

# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


#--------------------------Prime Numbers Checker --------------------------#
#Write your code below this line 👇

def prime_checker_2(number):
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime=False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

def prime_checker(number):
    for i in range(2,number):
        if number%i==0:
            print("It's not a prime number.")
            break
        else:
            print("It's a prime number.")
            break
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


#-------------------------- Caesar Cipher Code --------------------------#
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    # keep number in list
    shift_amount =shift_amount % 26

    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
    # What happens if the user enters a number/symbol/space?
        if char in alphabet:
            # index()只會找第一個字母 https://www.w3schools.com/python/ref_list_index.asp
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")

# Import and print the logo from art.py when the program starts.
from Day_8_art import logo
print(logo)

# Can you figure out a way to ask the user if they want to restart the cipher program?
should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    choose=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if choose=="no":
        should_continue=False
        print("Good Bye")

