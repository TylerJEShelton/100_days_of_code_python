from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        snake_length = 3
        for pos in range(0, snake_length):
            self.add_snake_body(pos)

    def add_snake_body(self, position):
        new_snake_body = Turtle(shape="square")
        new_snake_body.penup()
        new_snake_body.color("white")
        new_snake_body.goto(0 - (20 * position), 0)
        self.snake.append(new_snake_body)

    def extend_snake(self):
        self.add_snake_body(len(self.snake))

    def move(self):
        for body_num in range(len(self.snake) - 1, 0, -1):
            prev_body_position = self.snake[body_num - 1].position()
            self.snake[body_num].goto(prev_body_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)