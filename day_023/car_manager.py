from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
COLORS_LENGTH = len(COLORS)
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_Y_COR_MIN = -250
STARTING_Y_COR_MAX = 250


class CarManager():
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(COLORS[randint(0, COLORS_LENGTH - 1)])
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(300, randint(STARTING_Y_COR_MIN, STARTING_Y_COR_MAX))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.move_distance)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT
