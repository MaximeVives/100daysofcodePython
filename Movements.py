RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Movements:
    def __init__(self, snake):
        self.snake = snake

    def right(self):
        if self.snake.segments[0].heading() != LEFT:
            self.snake.segments[0].setheading(RIGHT)

    def left(self):
        if self.snake.segments[0].heading() != RIGHT:
            self.snake.segments[0].setheading(LEFT)

    def up(self):
        if self.snake.segments[0].heading() != DOWN:
            self.snake.segments[0].setheading(UP)

    def down(self):
        if self.snake.segments[0].heading() != UP:
            self.snake.segments[0].setheading(DOWN)

