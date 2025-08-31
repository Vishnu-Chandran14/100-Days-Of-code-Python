



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
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >=0 and user_choice <=2:
   print(Game_Images[user_choice])

   computer_choice = random.randint(0,2)
   print("computer choice: ")
   print(Game_Images[computer_choice])

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



else:
    print("Enter the valid number. Number should be between 0 and 1.")
