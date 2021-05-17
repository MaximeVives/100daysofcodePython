from art import *


def welcome():
    print(logo)
    print('''Hello, welcome to the Cesar Cypher.
You can enter a word and a shift. Then the software will cypher your word
You can choose to decode a word with the same technic
So now choose what you want to do : encrypte(1), decrypt(2), exit(3) ''')


def cesar_crypt(message, shift, shift_direction):
    encrypt_message = ""
    dir = 1

    if shift_direction != 1:
        dir = -1

    for letter in message:
        new_position = (alphabet.index(letter) + shift * dir) % 26
        encrypt_message += alphabet[new_position]

    return encrypt_message


def validate(message):
    for letter in message:
        if letter not in alphabet:
            return False
    return True


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

welcome()

choice = int(input('Your choice is : '))

while choice == 1 or choice == 2:
    message = input("Enter your message : ").lower()

    while not validate(message):
        message = input("Enter your message : ").lower()

    shift = int(input("Enter a number of shift : "))

    if choice == 1:
        print(f"Your encrypted message is : {cesar_crypt(message=message, shift=shift, shift_direction=choice)}")

    else:
        print(f"Your decrypted message is : {cesar_crypt(message=message, shift=shift, shift_direction=choice)}")

    choice = int(input('Your choice is (encrypte(1), decrypt(2), exit(3)) : '))

print("Good Bye")
