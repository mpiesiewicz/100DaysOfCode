import turtle

from Myturtle import MyTurtle
from turtle import Turtle, Screen
import colorgram
import random


class TurtleArt:
    def __init__(self, turtle, colours, rows, columns):
        self.rows = rows
        self.columns = columns
        self.colours = colours
        self.turtle = turtle
        self.turtle.penup()
        self.direction_flag = 90

    # 90 is right, 270 is left
    def change_direction(self):
        if self.direction_flag == 90:
            self.direction_flag = 270
        else:
            self.direction_flag = 90

    def turn_to_next_row(self):
        for _ in range(2):
            self.turtle.left(self.direction_flag)
            self.turtle.forward(50)

    def draw_row(self):
        for _ in range(self.columns):
            random_colour = random.choice(self.colours)
            self.turtle.dot(20, random_colour)
            self.turtle.forward(50)

    def do_art(self):
        self.turtle.setposition(-250, -250)
        for c in range(self.rows):
            self.draw_row()
            self.turn_to_next_row()
            self.change_direction()


if __name__ == '__main__':

    # functions from MyTurtle class:
    tim = Turtle()
    tim.shape('turtle')
    tim.color('black', 'green')
    tim.speed(0)
    screen = Screen()
    screen.colormode(255)
    # MyTurtle.gon(tim, 5, 100)
    # MyTurtle.spirograph(tim)
    # MyTurtle.shape_in_shape(tim)
    # MyTurtle.random_walk(tim)

    number_of_colors = 10
    scan = colorgram.extract('dots.jpeg', number_of_colors)
    print(scan)
    COLORS = []
    for color in scan:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        COLORS.append((red, green, blue))
    print(COLORS[2:])

    painting = TurtleArt(tim, COLORS[2:], 100, 100)
    painting.do_art()

    screen.exitonclick()


