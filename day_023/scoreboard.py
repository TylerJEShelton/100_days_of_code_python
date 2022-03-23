from turtle import Turtle
FONT = ("Courier", 24, "normal")
LEVEL_ALIGNMENT = "left"
GAME_OVER_ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-270, 260)
        self.write(f"Level: {self.level}", align=LEVEL_ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=GAME_OVER_ALIGNMENT, font=FONT)
