import colorgram
import turtle
from turtle import Turtle, Screen
import random

# rgb_colors = []
# colors = colorgram.extract('Flumequine.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

turtle.colormode(255)
color_list = [(243, 225, 74), (179, 78, 29), (49, 36, 26), (219, 151, 76), (146, 28, 41), (22, 25, 69), (44, 43, 120), (170, 21, 16), (48, 87, 158), (210, 85, 128), (156, 50, 86), (120, 160, 224), (27, 43, 28), (215, 79, 62), (139, 183, 140), (115, 106, 202), (75, 120, 57), (65, 30, 35), (157, 179, 231), (150, 211, 191), (204, 135, 43), (86, 87, 33), (87, 155, 109), (202, 121, 162), (61, 148, 170), (55, 100, 18)]

hirst = Turtle()
hirst.speed("fastest")
hirst.pu()
hirst.goto(-450, -400)
print(hirst.pos())
for row in range(10):
    hirst.pu()
    hirst.goto(-400, -400 + (row * 70))
    for _ in range(10):
        hirst.pd()
        hirst.dot(20, random.choice(color_list))
        hirst.pu()
        hirst.forward(70)

Screen().exitonclick()
