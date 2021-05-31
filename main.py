from turtle import Screen, Turtle
from Snake import Snake
from Movements import Movements
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#333333")
screen.title("Snake Game")
screen.listen()

snake = Snake(Turtle)
movements = Movements(snake)

game_is_on = True

screen.onkey(fun=movements.right, key="Right")
screen.onkey(fun=movements.left, key="Left")
screen.onkey(fun=movements.up, key="Up")
screen.onkey(fun=movements.down, key="Down")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()







screen.exitonclick()
