# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('black', 'green')
#
# timmy.forward(100)
#
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokemon Name', ['Pikaczu', 'Squirtle', 'Charmander'])
table.add_column('Pokemon Type', ['electric', 'water', 'fire'])
table.align = 'l'

print(table)

#END