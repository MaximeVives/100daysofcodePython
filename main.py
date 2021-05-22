from fonctions import *
from art import *


def valid_choice():
    choice_user = int(input("Good Morning, please select an action: (0) Off the machine, (1) Order a coffee, (2) Check Stocks : "))

    while choice_user != 0 and choice_user != 1 and choice_user != 2:
        print("Please Select a good option !")
        choice_user = int(input("Good Morning, please select an action: (0) Off the machine, (1) Order a coffee, (2) Check Stocks : "))

    return choice_user


print(logo)
print(title)

choice = valid_choice()

while choice == 0 or choice == 1 or choice == 2:

    if choice == 0:
        if off_machine():
            exit(0)
        else:
            choice = valid_choice()

    elif choice == 1:
        coffee_choice = order()
        drink = drinks[coffee_choice - 1]

        report(drink=drink)

        if not ressources_sufficient(drink=drink):
            print("Sorry, we can't make this coffee")

        else:
            process_coins(drink=drink)
            process_drink(drink=drink)

        choice = valid_choice()

    else:
        check_stocks()
        choice = valid_choice()




