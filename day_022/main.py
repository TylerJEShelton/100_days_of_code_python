import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    ball.refresh()
    time.sleep(ball.move_speed)

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with right and left paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect Right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect Left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()


screen.exitonclick()
