"""
Built the hangman game
"""
import random
from os import system
import hangman_words as hmw
import hangman_art as hma

END_OF_GAME = False
chosen_word = random.choice(hmw.word_list)
word_length = len(chosen_word)
LIVES = 6

print(hma.logo)

display = []
for letter in range(word_length):
    display += "_"
while not END_OF_GAME:
    guess = input("Guess a letter: ").lower()
    system('clear')
    if guess in display:
        print(f"you've already guessed {guess}")
    #check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter ==  guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"you guessed {guess}, that's not in the word. You lose a life")
        LIVES -= 1
        if LIVES == 0:
            END_OF_GAME = True
            print("you lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        END_OF_GAME = True
        print("You win")
    print(hma.stages[LIVES])
    