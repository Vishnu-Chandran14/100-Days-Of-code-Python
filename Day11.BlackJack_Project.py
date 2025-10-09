import random

import art
from art import logo

def deal_card():
    """a function is used to return a random card """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #cards in a sequence
    deck_card = random.choices(cards)
    return deck_card


def calculated_score(cards):
    """This function helps to sums-up the cards"""
    if len(cards) == 2 and sum(cards) > 21:
        return 0  #checklist for blackjack(a hand with 2 cars i.e ace + 10 value card
                  # and return 0 instead of the actual score. 0 will represent a blackjack in our game.)
    if sum(cards) > 21 and 11 in cards: #change the ace card value if score over 21 with ace card
                                        #replace the value of ace card is 1 instead of 11
        cards.remove(11)
        cards.append(1)

    return sum(cards) #It gives sums-up the cards in the list of users and computers

def play_game():
    user_cards = []

    computer_cards = []

    """Add the two cards for users and computer"""
    for every_deck_card in range(2):
        new_user_card = deal_card()
        user_cards = user_cards + new_user_card

    for every_deck_card in range(2):
        new_computer_card = deal_card()
        computer_cards = computer_cards + new_computer_card

    is_game_over = False

    while not is_game_over:

        user_score = calculated_score(user_cards)
        computer_score = calculated_score(computer_cards)

        print(f"Your cards : {user_cards}. score : {user_score}")
        print(f"computer's first card: {computer_cards[0]}")

        if user_score > 21 or user_score == 0 or computer_score == 0:
            is_game_over = True

        else:
            should_continue = input("Type 'y' to get another card OR 'n' to pass: ").lower()
            if should_continue == 'y': #adding an another card to existing user cards list
                user_cards = user_cards + deal_card()
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        """The computer should keep drawing cards as long as it has a score less than 17"""
        computer_cards = computer_cards + deal_card() #adding an another card to existing computer cards list
        computer_score = calculated_score(computer_cards)

    def compare():
        if computer_score == user_score:
            return "It's a draw"
        elif computer_score == 0:
            return "You lose"
        elif user_score == 0:
            return "You win"
        elif user_score > 21:
            return "You lose"
        elif computer_score > 21:
            return "You win"
        elif user_score > computer_score:
            return "You win"
        else:
            return "you lose"

    print(f"Your final cards : {user_cards}. score : {user_score}")
    print(f"computer's final cards: {computer_cards}. final_score = {computer_score}")
    print(compare())

restart = False

while not restart:
    game = input("Type 'yes' to start a game OR 'no' to not to play game").lower()
    if game == 'yes':
        print("\n" * 20)
        print(art.logo)
        play_game()

    else:
        restart = True








