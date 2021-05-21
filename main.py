from art import *
from game_data import *
import random


def print_guest(guest):
    return f"{guest['name']}, a {guest['description']} from {guest['country']}"


def print_compare(f_guest, s_guest):
    print_first = print_guest(f_guest)
    print_second = print_guest(s_guest)

    print("Compare : " + print_first)
    print(vs)
    print("Against : " + print_second)


print(logo)
print("""Welcome player, rules are easy. 
You have 2 personalities and you must find, who has the most followers on Instagram.""")

already_done = []

first_guest = random.choice(data)
already_done.append(first_guest)

correct = True
score = 0


while correct:
    if score == 49:
        print("You finished the Game ! GG ! 🏆")
        exit(0)

    print(f"Your score : {score}")
    second_guest = random.choice(data)

    while second_guest in already_done:
        second_guest = random.choice(data)

    already_done.append(second_guest)

    print_compare(first_guest, second_guest)

    choice = input(f"Who has the most followers on Instagram ? (1) {first_guest['name']} or (2) {second_guest['name']}")

    while choice != '1' and choice != '2':
        print("Enter a correct letter")
        choice = input(f"Who has the most followers on Instagram ? (1) {first_guest['name']} or (2) {second_guest['name']}")

    if choice == "1" and first_guest['follower_count'] > second_guest['follower_count']:
        print("Well played ! ")
        score += 1

    elif choice == "2" and first_guest['follower_count'] < second_guest['follower_count']:
        print("Well played ! ")
        first_guest = second_guest
        score += 1

    else:
        print("You lose")
        correct = False
