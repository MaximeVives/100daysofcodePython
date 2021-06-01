DISTANCE = 20
from turtle import Turtle


class Snake:
    segments = []
    colors = ["white", "white", "white"]

    def __init__(self):
        for ind in range(3):
            self.segments.append(Turtle(shape="square"))
            self.segments[ind].penup()
            self.segments[ind].forward(-(3 * DISTANCE) + (ind * DISTANCE))
            self.segments[ind].color(self.colors[ind])

    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()

            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(DISTANCE)

