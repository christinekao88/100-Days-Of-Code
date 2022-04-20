
#------------------------------- rock-paper-scissors -------------------------------#
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

choose_list=[rock,paper,scissors]

 # remember input function always get string
user_choose = int(input('What do you choose? Type 0 for Rock ,Type 1 for Paper ,Type 2 for scissors \n'))

if user_choose >= 3 or user_choose < 0 :  
    print('You type wrong number')
else :
    print(choose_list[user_choose])

    print('Computer Choose')

    computer_choice = random.randint(0,len(choose_list)-1)
    print(choose_list[computer_choice])

    if computer_choice==user_choose:
        print('This is a draw game')
    elif user_choose>computer_choice:
        print('You win !!!')
    elif user_choose<computer_choice:
        print('You Loose')
    elif computer_choice==2 and user_choose==0:
        print('You win !!!')
    elif computer_choice==0 and user_choose==2:
        print('You Loose !!!')


#------------------------------- way 2 -------------------------------#
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose:{computer_choice}")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end