import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

UP = "Up"

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
# create_car counter
create_car = 6
while game_is_on:
    screen.onkey(player.go_up, UP)
    # Add 1 to the create_car counter
    create_car += 1 * scoreboard.level
    # When the create_car counter reaches 6, put it to 0 and create a new car.
    if create_car >= 6:
        create_car = 0
        car_manager.create_car()
    car_manager.move()

    # Detect if player has completed the level.
    if player.complete_level():
        player.restart_level()
        car_manager.level_up()
        scoreboard.increase_level()

    # Detect collision with a car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
