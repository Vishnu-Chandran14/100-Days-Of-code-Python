import random

from art import logo


#set difficulty levels

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def level(user_choice):
    if user_choice == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS

# Return the number of turns users have, make a number high or low based on guessing number,
# And return the final statement if guessing is correct

def attempts(computer_guess, user_guess, turns):
    if user_guess > computer_guess:
        print("Too high")
        return turns - 1
    elif user_guess < computer_guess:
        print("Too low")
        return turns - 1
    else:
        print(f"You got the number. The correct number was {turns}.")
        return


# Game function - To play the main game

def game():
    # print logo, welcome message, introduction
    print(logo)
    print("Welcome to the Number Guessing Game.")
    print("I'm thinking of a number between 1 and 100.")

    # Choose a difficulty level by user and print the attempt remaining till user types correctly.

    input_level = False
    while not input_level:
        difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard:").lower()
        if difficulty_level == "easy" or difficulty_level == "hard":
            input_level = True
        else:
            print("Incorrect input.")

    #print the number of turns that user have

    turns = level(difficulty_level)

    # Generate the number to find between 1 and 100

    random_number = random.randint(1, 100)

    # Give a choices till find the correct number therefore while loops operators

    correct_number = False
    while not correct_number:
        print(f"You have {turns} attempts remaining to guess the number")

        # Ask the user to guess a number

        guess_number = int(input("Make a guess: "))

        # call the function attempts by given inputs with guess_number, random_number, turns

        turns = attempts(random_number, guess_number, turns)

        # set the condition to run the loops

        if random_number == guess_number:
            correct_number = True
        elif turns == 0:
            print("You run out of attempts. Start the game again!")
            break
        elif random_number != guess_number:
            print("Guess again.")


game()




