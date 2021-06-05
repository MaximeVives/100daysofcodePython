from turtle import Screen

from Snake import Snake
from Movements import Movements
from Food import Food
from ScoreBoard import ScoreBoard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#333333")
screen.title("Snake Game")
screen.listen()

snake = Snake()
movements = Movements(snake)
food = Food()
scoreboard = ScoreBoard()

game_is_on = True

screen.onkey(fun=movements.right, key="Right")
screen.onkey(fun=movements.left, key="Left")
screen.onkey(fun=movements.up, key="Up")
screen.onkey(fun=movements.down, key="Down")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Colision avec food
    if snake.segments[0].distance(food) <= 15.0:
        food.refresh()
        snake.add_segment()
        scoreboard.increase_score()

    # Detection collision wall
    if snake.segments[0].xcor() >= 280 or snake.segments[0].xcor() <= -280 or snake.segments[0].ycor() >= 280 or snake.segments[0].ycor() <= -280:
        game_is_on = False
        scoreboard.gameover()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()








screen.exitonclick()
