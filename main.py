import random


def welcome():
    print('''
Welcome to the Number Guessing Game !
I'm thinking of a number between 1 and 100. 
    ''')


def difficult_choice():
    difficulty = input("Choose a difficulty. Type 'easy or 'hard' : ")

    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5

    return attempts


def check_answer(guess, answer):
    if guess > answer:
        print("Too high.\n")
        return False

    elif guess < answer:
        print("Too low\n")
        return False

    else:
        return True


welcome()
play_again = "y"

while play_again == "y":
    attempts = difficult_choice()

    TO_GUESS = random.randint(1, 100)
    guess = 0


    # Start
    while guess != TO_GUESS or not win:
        print(f"You have {attempts} remaining to guess the number.")
        guess = int(input("Make a guess : "))
        attempts -= 1

        win = check_answer(guess=guess, answer=TO_GUESS)

        if win:
            break

        if attempts <= 0:
            break
        else:
            print("Guess again.")

    if win:
        print("WELL PLAYED ! You Win ! ")
    else:
        print(f"Nice Try but You Lose, the number was {TO_GUESS}")

    play_again = input("Play again ? 'y' to continue or 'e' to exit : ")
