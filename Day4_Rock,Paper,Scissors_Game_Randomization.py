#100-Days-Of-code-Python
#Documenatation of Python Course-Learning 100 days of code

#used the random method

import random



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

Game_Images = [rock, paper, scissors]

#user input

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#conditioning the user input within a limit 0 to 2

if user_choice >=0 and user_choice <=2:
   print(Game_Images[user_choice])


#print the computer choice by using the random

   computer_choice = random.randint(0,2)
   print("computer choice: ")
   print(Game_Images[computer_choice])

#conditioning the possibilities of user's win and loss by using logical operator like IF
    
   if user_choice == 0 and computer_choice == 1:
       print("You lose")
   elif user_choice == 0 and computer_choice == 2:
       print("You win!")
   elif user_choice == 2 and computer_choice == 0:
       print("You lose")
   elif user_choice > computer_choice:
       print("You win!")
   elif user_choice < computer_choice:
       print("You lose")
   elif user_choice == computer_choice:
       print("It's draw. Start the game again!")


#print the error / alert message if user give the number more than 2 as their input
else:
    print("Enter the valid number. Number should be between 0 and 1.")
