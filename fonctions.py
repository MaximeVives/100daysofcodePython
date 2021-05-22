from stocks import *


def order():
    coffee_choice = int(input("What would you like ? (1) Espresso / (2) Latte / (3) Cappuccino : "))

    while coffee_choice != 1 and coffee_choice != 2 and coffee_choice != 3:
        print("This selection doesn't exist or not in stock")
        coffee_choice = int(input("What would you like ? (1) Espresso / (2) Latte / (3) Cappuccino : "))

    return coffee_choice


def off_machine():
    code = input("Enter the code to turn off the Coffee Machine : ")
    while code != "off":
        choice = input("Incorrect value do you want to Back home ? 'y' for yes or 'n' for no : ")
        while choice != 'y' and choice != 'n':
            choice = input("Incorrect value do you want to Back home ? 'y' for yes or 'n' for no : ")

        if choice == 'y':
            return False
        code = input("Enter the code to turn off the Coffee Machine : ")
    return True


def report(drink):
    for ingredients in drink["ingredients"]:
        for key, value in ingredients.items():
            print(f"{key}: {value}")

    print(f"price : {drink['price']}")


def ressources_sufficient(drink):
    i = 0
    for ingredients in drink["ingredients"]:
        for key, value in ingredients.items():
            print(f"key: {key}, value: {value}")
            if stock[i][key] < value:
                print(f"Sorry there is not Enough {key}")
                return False

            else:
                stock[i][key] -= value
                print(stock[i][key])

        i += 1

    return True


def process_coins(drink):
    # Before, verify if ressources_sufficient == True
    price = drink["price"]
    money_customer = 0.0

    while money_customer < price:
        add_value = adding_money_bank()
        money_customer += add_value

        if money_customer >= price:
            print(f"change : {money_customer - price}$")

        elif money_customer == price:
            return True

        else:
            print(f"You have insert {money_customer}$. Need {price - money_customer}$ more")

    difference = 0

    if money_customer > price:
        difference = money_customer - price

    list_money = money_back(difference)

    quarters = list_money[0]
    dimes = list_money[1]
    nickles = list_money[2]
    pennies = list_money[3]

    sub_money_bank(quarters=quarters, dimes=dimes, nickles=nickles, pennies=pennies)


def money_back(difference):
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0

    while difference != 0:

        while difference - 0.25 * quarters > 0:
            quarters += 1
            if difference - 0.25 * quarters < 0:
                quarters -= 1
                break
        difference -= 0.25 * quarters

        while difference - 0.1 * dimes > 0:
            dimes += 1
            if difference - 0.1 * dimes < 0:
                dimes -= 1
                break
        difference -= 0.1 * dimes

        while difference - 0.05 * nickles > 0:
            nickles += 1
            if difference - 0.05 * nickles < 0:
                nickles -= 1
                break
        difference -= 0.05 * nickles

        while difference - 0.01 * pennies > 0:
            pennies += 1
            if difference - 0.01 * pennies < 0:
                pennies -= 1
                break
        difference -= 0.01 * pennies

    return [quarters, dimes, nickles, pennies]


def sub_money_bank(quarters, dimes, nickles, pennies):
    money["quarters"] -= quarters
    money["dimes"] -= dimes
    money["nickles"] -= nickles
    money["pennies"] -= pennies


def adding_money_bank():
    add_value = float(input("Please insert coins : (0.25), (0.10), (0.05) or (0.01)"))

    while add_value != 0.25 and add_value != 0.10 and add_value != 0.05 and add_value != 0.01:
        add_value = float(input("Please insert coins : (0.25), (0.10), (0.05) or (0.01)"))

    if add_value == 0.25:
        money["quarters"] += 1

    elif add_value == 0.1:
        money["dimes"] += 1

    elif add_value == 0.05:
        money["nickles"] += 1

    else:
        money["pennies"] += 1

    return add_value


def process_drink(drink):
    # Enough resources and paid

    print(f"Your {drink['name']} is ready. Enjoy !")


def check_stocks():
    print(f"Stock Product : \n{stock}")
    print(f"Money : \n{money}")

