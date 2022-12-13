"""BlackJack game
"""
from art import logo
import os
import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the card"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compare both the user and computers score to publish the winner"""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose"

    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return"Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

        print(f" Your final hand: {user_cards}, final score: {user_score}")
        print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    play_game()

"""
This is a program that simulates the card game Blackjack. The program uses the deal_card() function to randomly 
choose a card from a deck of cards and add it to the player's hand or the computer's hand. The calculate_score() 
function takes a list of cards and calculates the score for that hand, taking into account the fact that an Ace can
be worth either 1 or 11 points. The compare() function compares the scores of the player and the computer, and returns
a string indicating who won the game.

The play_game() function is the main function that controls the flow of the game. It starts by dealing two cards each
to the player and the computer, and then it enters a loop where it asks the player if they want to hit (take another card)
or stand (keep their current hand). The loop continues until either the player or the computer has a score
of 21 (a Blackjack) or the player's score goes over 21 (busts).

After the player has finished their turn, the computer takes its turn, drawing additional cards until its score is 17
or higher. Once the computer has finished its turn, the final scores are displayed and the winner is announced.
The program then asks the player if they want to play again, and if so, the game starts over.
"""