from turtle import Turtle
import random
COLORS = ["red", "yellow", "purple", "blue", "orange", "green"]


class CarManager:
    all_cars: list

    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(x=300, y=random.randint(-240, 280))
        new_car.setheading(180)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(30)

    def get_cars(self):
        return self.all_cars
