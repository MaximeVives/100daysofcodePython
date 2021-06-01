from turtle import Turtle


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.color("white")
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))



