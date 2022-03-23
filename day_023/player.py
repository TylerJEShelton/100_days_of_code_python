from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def complete_level(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    def restart_level(self):
        self.goto(STARTING_POSITION)