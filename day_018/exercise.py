import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
#
# for _ in range(1, 6):
#     timmy.forward(20)
#     timmy.pu()
#     timmy.forward(20)
#     timmy.pd()
#
#
#
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# draw_shape(6)
# draw_shape(5)
# draw_shape(4)
# draw_shape(3)

turtle.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
#
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "SeaGreen", "SlateGrey"]
# directions = [0, 90, 180, 270]
# timmy.pensize(15)
# timmy.speed("fastest")
#
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)


draw_spirograph(2)


Screen().exitonclick()