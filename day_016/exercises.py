# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("black", "green")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Eevee", "Charmander", "Squirtle", "Bulbasaur"])
table.add_column("Type", ["Normal", "Fire", "Water", "Grass"])
table.align = "l"

print(table)
