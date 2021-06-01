from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
    
