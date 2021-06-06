from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.write(f"{self.l_score} - {self.r_score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self, position):
        if position == "right":
            self.r_score += 1
        else:
            self.l_score += 1

        self.clear()
        self.update_score()
