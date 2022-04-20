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
from replit import clear


# Format the account data into printable format
def format_data(person_dic):
    name=person_dic['name']
    description=person_dic['description']
    country=person_dic['country']
    return f"{name} , {description} , from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    # 如果猜測為b，則返回False
    return guess == "a"
  else: # if b>a
    return guess == "b"

# Display art
print(logo)


# score keeping
score=0
game_should_continue=True

person=random.choice(data)

while game_should_continue:
    # Generate a random account from the game data
    person_a=person
    person_b=random.choice(data)
    while person_a==person_b:
        person_b=random.choice(data)


    print(f"Compare A : {format_data(person_a)}")
    print(vs)
    print(f"Against B : {format_data(person_b)}")

    # ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # get follower count of each account
    person_a_count=person_a["follower_count"]
    person_b_count=person_b["follower_count"]

    # check if user is correct
    is_correct=check_answer(guess,person_a_count,person_b_count)

    # Clear the screen between rounds 
    clear()
    print(logo)
    # use if statement to check if user is correct
    if is_correct:
        print(f"You are right. Current score : {score}.")
        score+=1
    else:
        game_should_continue=False
        print(f"You are wrong. Final score : {score}.")


