from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__(shape="square")
        self.hideturtle()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.penup()

        if pos == "right":
            self.goto(x=350, y=0)
        else:
            self.goto(x=-350, y=0)

        self.setheading(90)
        self.showturtle()

    def move_top(self):
        if not self.ycor() > 220.0:
            self.forward(20)

    def move_bottom(self):
        if not self.ycor() < -220.0:
            self.forward(-20)
