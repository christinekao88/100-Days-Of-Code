"""
Day 14 - Beginner - Higher Lower Game Project
            1. break down the problems
            2. start with the easiest
            3. turn the problem into comments
            4. write ->run -> fix code
"""
from Day_14_art import logo,vs
from Day_14_game_data import data
import random

def get_info(data):
    person_option=random.choice(data)
    person=data[data.index(person_option)]
    name=person['name']
    follower_count=person['follower_count']
    description=person['description']
    country=person['country']
    return [name,follower_count,description,country]

from replit import clear

guess_wrong=0
score=0
while guess_wrong<3:
    print(logo)
    print(f"You're right! Current score:  {score}.")

    person_A = get_info(data)
    print(f"Compare A : {person_A[0]}, {person_A[2]}, from {person_A[3]}. {person_A[1]}")

    print(vs)

    person_B = get_info(data)
    print(f"Against B : {person_B[0]}, {person_B[2]}, from {person_B[3]}. {person_B[1]}\n")

    choose = input("Who has more followers? Type 'A' or 'B': ")

    if choose=='A':
        if person_A[1] > person_B[1]:
            person_A=person_A
            person_B = get_info(data)
            score+=1
        elif person_A[1]<person_B[1]:
            person_A=person_B
            person_B = get_info(data)
            guess_wrong+=1

    clear()

print(f"Sorry, that's wrong. Final score: {score}")
