"""
Day 7 - Beginner - Hangman
"""
from replit import clear
import random
from Day_7_hangman_words import word_list
from Day_7_hangman_art import logo, stages

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word=random.choice(word_list)

print(logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display. #For each letter in the chosen_word, add a "_" to 'display'.
display=[]
for i in range(0,len(chosen_word)):
    display.append('_')

# for letter in chosen_word:
#     display+='_'

# for _ in range(len(chosen_word)):
#     display+='_' 

# Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
lives=6
# Use a while loop to let the user guess again.
while '_' in display:
    guess=input("Guess a letter : ").lower()
    clear()
    if guess in display:
        print(f"You have already guess {guess}")
    # Loop through each position in the chosen_word;#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i]=guess
      #  If guess is not a letter in the chosen_word, Then reduce 'lives' by 1. 
    if guess not in chosen_word:
      lives-=1
      print(f"You guess {guess}, that's not in the word. You loose a life")        
      if lives==0:
          print("You Loose!")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    if '_' not in display:
        print("You win")
    print(stages[lives])