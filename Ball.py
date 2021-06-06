from turtle import Turtle


class Ball(Turtle):
    orientation_x = 1
    orientation_y = 1
    ball_speed = 2

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()

    def move(self):
        new_x = self.xcor() + (self.ball_speed * self.orientation_x)
        new_y = self.ycor() + (self.ball_speed * self.orientation_y)
        self.goto(x=new_x, y=new_y)

    def bounce_wall(self):
        self.orientation_y = -self.orientation_y

    def bounce_paddle(self):
        self.orientation_x = -self.orientation_x
        self.increase_speed()

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_paddle()
        self.ball_speed = 2

    def increase_speed(self):
        self.ball_speed += 0.1
