from art import *


def welcome():
    print(logo)
    print('''Welcome everybody. Today we will participate to a blind auction.
    The prize is the 5G patent.
    Please all bidders register to the software and indicate your price.''')


def bidder_register():
    name_user = input("Enter your name : ")
    bid_user = float(input("Enter your price : "))

    return {
        "name": name_user,
        "bid": bid_user
    }


def bidder_winner(list_bidders):
    highest = {
        "name": "",
        "bid": -1
    }
    for bidder in list_bidders:
        if bidder["bid"] > highest["bid"]:
            highest = bidder

    return highest


# ============= START HERE =============
welcome()

end_of_bid = False
all_bidders = []


while not end_of_bid:
    all_bidders.append(bidder_register())

    choice = input("There is another bidder ? 'yes' or 'no' : ")

    if choice == "no":
        end_of_bid = True


print(f"The winner is {bidder_winner(all_bidders)["name"]}. Congratulation !")

