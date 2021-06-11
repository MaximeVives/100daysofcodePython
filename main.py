from turtle import Screen
import time
from Player import Player
from CarManager import CarManager
from Dashboard import Dashboard

sc = Screen()
sc.setup(width=600, height=600)
sc.tracer(0)

turtle = Player()
car = CarManager()
score = Dashboard()

game_is_on = True

sc.listen()
sc.onkey(turtle.move, "Up")

wait = 0

while game_is_on:
    if wait % 3 == 0:
        car.create_cars()
    if wait % 2 == 0:
        car.move_cars()

    for car_list in car.get_cars():
        if turtle.distance(car_list) <= 20:
            game_is_on = False
            score.game_over()

    if turtle.end_level():
        score.update_score()

    wait += 1
    time.sleep(0.1)
    sc.update()

sc.exitonclick()
