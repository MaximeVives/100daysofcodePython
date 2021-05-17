from art import *


# Functions Calculator
# ADD
def add(a, b):
    return a + b


# SUBSTRACT
def substract(a, b):
    return a - b


# MULTIPLY
def multiply(a, b):
    return a * b


# DIVIDE
def divide(a, b):
    if b == 0:
        return "Error"
    return a / b


def calculator():
    num1 = float(input("What's the first number : "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation  : ")
        num2 = float(input("What's the next number : "))
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        next_step = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation :")

        if next_step == "y":
            num1 = answer

        elif next_step == "n":
            should_continue = False
            calculator()

        else:
            should_continue = False


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

print(logo)
calculator()

