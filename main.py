from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


def start_turtles():
    for index, color in enumerate(colors):
        turtles.append(Turtle(shape="turtle"))

        turtles[index].speed("fastest")
        turtles[index].penup()
        turtles[index].color(color)

        ypos = -90 + (index * 30)

        turtles[index].goto(x=-225, y=ypos)


def run_turtle():
    winner = False
    while not winner:
        for turtle in turtles:
            if turtle.xcor() >= 225:
                winner = True
                return turtle
            else:
                turtle.forward(randint(2, 8))


sc = Screen()
sc.setup(width=500, height=400)

user_bet = sc.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

start_turtles()

winner_turtle = run_turtle()

if winner_turtle.color()[1] == user_bet:
    print("You win")

else:
    print(f"You lose. It's the {winner_turtle.color()[1]} turtle winner.")

sc.exitonclick()
