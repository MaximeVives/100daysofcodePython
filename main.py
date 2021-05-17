import random
import os
from hangman_art import *
from hangman_words import *


# 0. Print the Hangman ASCII logo
print(logo)

# 1. Picking a Random Word and checking answer
chosen_word = random.choice(word_list)

# 1.2 Implement "lives" to 6
lives = 6

# INTERMEDIAIRE
# print(f"DEBUG : {chosen_word}")

# 2. Create a list with "blank" as the same size as the chosen_word.
display = []

for _ in chosen_word:
    display += "_"

print(display)

# 3. Use a loop to let the user guess again
while "_" in display and lives > 0:

    # 4. Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter : ").lower()

    if guess in display:
        print(f"You already try '{guess}'. Try another one !")

    while len(guess) > 1 or len(guess) < 1:
        guess = input("Write only 1 letter please : ").lower()

    # 5. Check if the letter the user guessed is one of the letters
    # in the chosen_word and replace a blank by the letter on the list
    for pos, letter in enumerate(chosen_word, start=0):
        if letter == guess:
            display[pos] = letter

    if guess not in chosen_word:
        print(f"There is no '{guess}' in the word.")
        lives -= 1

    print(f"You have {lives} lives")
    print(display)
    print(stages[lives])

print(f"Game over")

if lives == 0:
    print("You lose")
else:
    print("You win !")
