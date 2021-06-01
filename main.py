# Pong Game

from turtle import Screen
from Paddle import Paddle
from Ball import Ball


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#000")
screen.title("Pong")


paddle_right = Paddle(pos="right")
paddle_left = Paddle(pos="left")

ball = Ball()

screen.listen()
game_is_on = True

screen.onkey(fun=paddle_right.move_top, key="Up")
screen.onkey(fun=paddle_right.move_bottom, key="Down")

screen.onkey(fun=paddle_left.move_top, key="z")
screen.onkey(fun=paddle_left.move_bottom, key="s")





screen.exitonclick()