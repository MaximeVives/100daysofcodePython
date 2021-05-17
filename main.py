# If the bill xas 150$, split between 5 people, with a 12% tip.
# Each person should pay (150 / 5) * 1.12

print("This is a bill and tip calculator, answer some questions and it will return an amount to pay for each person")

# 1. Get the amount of the bill
bill = float(input("What was the total bill ? "))

# 2. Get the percentage tip the user want to give
tip_percentage = int(input("What percentage tip would you like to give ? 10, 12, 15 ? "))

# 3. Transform the percentage to a float number
tip_float = 1 + (tip_percentage / 100)

# 4. Get the number of people with the user will split the bill
number_customer = int(input("How many people to split the bill ? "))

# 5. Show the result
result = round((bill / number_customer) * tip_float, 2)
print(f"Each person should pay: ${result}")
