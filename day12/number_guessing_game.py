from random import randint
from art import logo

HARD_LEVEL = 5
EASY_LEVEL = 10


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns -1
    elif guess < answer:
        print("Too Low")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}.")

def difficulty():
    """checks the difficulty we would play with"""
    level = input("choose your difficulty level. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    turns = difficulty()
    guess = 0

    #Repeat the guess if they get it wrong
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you've run out of guesses, you lose.")
            print(f"The correct answer is {answer}")

            return
        elif guess != answer:
            print("Guess again.")

play_game()