from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.setheading(90)
        self.start_position()

    def move(self):
        self.forward(20)

    def end_level(self):
        if self.ycor() >= 280:
            self.start_position()
            return True
        return False

    def start_position(self):
        self.goto(x=0, y=-280)
