import colorgram
from turtle import Turtle, Screen, colormode
from random import choice


def list_colors_generator():
    rgb_colors = []
    colors = colorgram.extract("image.jpg", 30)

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b

        rgb_colors.append((r, g, b))

    return rgb_colors


def circle_color(cc):
    timmy.fillcolor(cc)
    timmy.circle(20)


def setup():
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)


def dot_map(l_color, nbr_dot):
    for dot_count in range(1, nbr_dot + 1):
        timmy.dot(20, choice(l_color))
        timmy.forward(50)

        if dot_count % 10 == 0:
            timmy.setheading(90)
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(500)
            timmy.setheading(0)


screen = Screen()

timmy = Turtle(shape="turtle")
timmy.penup()
timmy.hideturtle()

colormode(255)
timmy.speed("fastest")

list_colors = list_colors_generator()
setup()
dot_map(list_colors, 100)


screen.exitonclick()
