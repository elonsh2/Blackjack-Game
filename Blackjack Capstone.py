from art import *
import random
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(list_of_cards):
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return sum(list_of_cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'Draw'
    elif computer_score == 0:
        return 'Lose'
    elif user_score == 0:
        return 'win'
    elif user_score > 21:
        return 'Lose'
    elif computer_score > 21:
        return 'win'
    elif user_score > computer_score:
        return 'win'
    elif computer_score > user_score:
        return 'Lose'


def blackjack():
    print(logo)
    is_game_over = False
    user_cards = []
    cpu_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        cpu_cards.append(deal_card())
    while not is_game_over:
        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}\n"
              f"Computer's first card: {cpu_cards[0]}")
        user_score = calculate_score(user_cards)
        cpu_score = calculate_score(cpu_cards)
        if user_score == 0 or cpu_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while cpu_score < 17 and cpu_score != 0:
        cpu_cards.append(deal_card())
        cpu_score = calculate_score(cpu_cards)
    outcome = compare(user_score, cpu_score)
    print(f"Your final hand is {user_cards} with a score of: {user_score}\n"
          f"The computer's final hand is {cpu_cards} with a score of {cpu_score}")
    print(outcome)


while input("Do you want to play a game of Blackjack? Type 'y' for yes: ") == 'y':
    cls()
    blackjack()
