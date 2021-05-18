import random
from art import *


def welcome():
    print(logo)
    print('''Welcome. You want to play a game of Blackjack so the cashier will get only one card until you finished
    to play. Then, it will be his turn.\n\n''')


def get_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def show_cards(j1, j2):
    print(f"Your cards : {j1}")
    print(f"Cashier cards : {j2}")
    print("\n")


def action():
    return int(input("What do you want to do ? take a card (1) end here (2)\n"))


def total(cards):
    total_score = 0
    for card in cards:
        total_score += card

    return total_score


def verification(j1, j2):
    if j2 > j1:
        if j2 > 21:
            print("You win !")
        else:
            print("You lose !")
        if j2 == 21:
            print("Cashier wins with a Blackjack !")
    elif j2 < j1:
        if j1 > 21:
            print("You lose !")
        else:
            print("You win !")
        if j1 == 21:
            print("You win with a Blackjack !")
    else:
        print("It's a draw")


def play():
    j1_cards = [get_a_card()]
    j2_cards = [get_a_card()]

    lose_j1 = False

    show_cards(j1=j1_cards, j2=j2_cards)

    # ================ J1 ======================
    choice = action()

    while choice != 2:
        j1_cards.append(get_a_card())
        show_cards(j1=j1_cards, j2=j2_cards)

        total_j1 = total(j1_cards)

        if total_j1 > 21:
            if 11 in j1_cards:
                position = j1_cards.index(11)
                j1_cards[position] = 1
                total_j1 = total(j1_cards)
                show_cards(j1=j1_cards, j2=j2_cards)
            else:
                lose_j1 = True
                choice = 2

        if not lose_j1:
            choice = action()

    # ================J2========================
    total_j2 = total(j2_cards)
    show_cards(j1=j1_cards, j2=j2_cards)

    while total_j2 < 17 and not lose_j1:
        j2_cards.append(get_a_card())
        total_j2 = total(j2_cards)

        show_cards(j1=j1_cards, j2=j2_cards)

        if total_j2 > 21:
            if 11 in j2_cards:
                position = j2_cards.index(11)
                j2_cards[position] = 1
                total_j2 = total(j2_cards)
                show_cards(j1=j1_cards, j2=j2_cards)

    verification(j1=total_j1, j2=total_j2)