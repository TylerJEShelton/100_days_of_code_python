import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you think will win the race. Enter the color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(-230, -100 + 30 * index)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for each_turtle in turtles:
        if each_turtle.xcor() > 230:
            is_race_on = False
            winning_color = each_turtle.pencolor()
            if winning_color == user_bet:
                screen.title("You've Won!")
                print(f"You've won! The {winning_color} turtle won the race!")
            else:
                screen.title("You've lost!")
                print(f"You lost! The {winning_color} turtle actually won the race!")

        rand_distance = random.randint(0, 15)
        each_turtle.forward(rand_distance)


screen.exitonclick()