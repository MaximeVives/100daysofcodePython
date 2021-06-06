# Pong Game

from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from GameOver import GameOver
from Score import Score

import time


screen = Screen()
screen.setup(width=800, height=605)
screen.bgcolor("#000")
screen.title("Pong")
screen.tracer(0)


paddle_right = Paddle(pos="right")
paddle_left = Paddle(pos="left")

ball = Ball()
score = Score()

screen.listen()
game_is_on = True

screen.onkey(fun=paddle_right.move_top, key="Up")
screen.onkey(fun=paddle_right.move_bottom, key="Down")

screen.onkey(fun=paddle_left.move_top, key="z")
screen.onkey(fun=paddle_left.move_bottom, key="s")

while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 260 or ball.ycor() < -260:
        # need to bounce
        ball.bounce_wall()

    if (ball.distance(paddle_left) < 50 and ball.xcor() < -320) or (ball.distance(paddle_right) < 50 and ball.xcor() > 320):
        ball.bounce_paddle()

    if ball.xcor() > paddle_right.xcor() + 20:
        ball.reset_position()
        score.increase_score("left")

    elif ball.xcor() < paddle_left.xcor() - 20:
        ball.reset_position()
        score.increase_score("right")

    if score.l_score >= 10 or score.r_score >= 10:
        game_is_on = False
        game_over = GameOver()



screen.exitonclick()