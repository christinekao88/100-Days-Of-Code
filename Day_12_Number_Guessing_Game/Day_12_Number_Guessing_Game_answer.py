"""
Day 12 - Beginner - Scope & Number Guessing Game
"""

# Include an ASCII art logo.
from Day_12_art import logo
print(logo)

print("Welcome to the Number Guessing Game!")

import random
answer = random.randint(1,100)

print("I'm thinking of a number between 1 and 100.")

print(f"Pssst, the correct answer is {answer}")

choose=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if choose=='easy':
    chance=10
elif choose=='hard':
    chance=5

def check(guess,answer):
    if guess>answer:
        print("Too high.")
    elif guess<answer:
        print("Too low.")
    else:  
        print(f"You got it! The answer was {guess}")
        
guess=0
while guess!=answer and chance>=0:
    if chance>=1:
        print(f"You have {chance} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))
        check(guess,answer)
    if guess != answer and chance>1:
        print("Guess again.")    
    elif chance==0:
        print("You've run out of guesses, you lose.")
    chance-=1
        
