from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_counter_clockwise():
    tim.left(5)


def turn_clockwise():
    tim.right(5)


def clear_and_reset():
    tim.clear()
    tim.reset()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_counter_clockwise)
screen.onkeypress(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_and_reset)

screen.exitonclick()
