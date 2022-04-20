"""
Day 11 - Beginner - The Blackjack Capstone Project
"""

import random
from replit import clear
from Day_11__art import logo

# Create a deal_card() function that uses the List below to *return* a random card. 11 is the Ace.
def deal_card() :
    """return a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

# calculate_score() that takes a List of cards as input and returns the score. 
def calculate_score(card_list):
    # check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 
    # 0 will represent a blackjack in our game.
    if sum(card_list)==21 and len(card_list)==2:
        return 0

    # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
    if 11 in card_list and sum(card_list)>21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)

def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
    # Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    for i in range(2): 
        # append()-> add single item to existing list
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    # user playing
    playing=True
    while playing:    
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f"Your cards : {user_cards},current score : {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            playing=False
        else:
            # If the game has not ended, ask the user if they want to draw another card. 
            keep = input("Do you want to get another card ? Type 'y' or 'n' : ").lower() 
            if keep =='y':
                user_cards.append(deal_card())
            else:
                playing=False

    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    # computer playing
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"Your final hand : {user_cards},final score : {user_score}")
    print(f"Computer's final hand :{computer_cards},final score : {computer_score}")

    print(compare(user_score,computer_score))

# Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n' : '")=='y':
    print(logo)
    clear()
    play_game()