import turtle
from Myturtle import MyTurtle
from turtle import Turtle, Screen
from TurtleArt import TurtleArt
from Colours import Colours

if __name__ == '__main__':

    # Turtle settings:
    tim = Turtle()
    tim.shape('turtle')
    tim.color('black', 'green')
    tim.speed(0)

    # Screen settings:
    screen = Screen()
    screen.colormode(255)

    # functions from MyTurtle class:
    # MyTurtle.gon(tim, 5, 100)
    # MyTurtle.spirograph(tim)
    # MyTurtle.shape_in_shape(tim)
    # MyTurtle.random_walk(tim)

    # get colours except 2 most popular (eliminate white background)
    colors = Colours.colour_getter('dots.jpeg', 10)[2:]

    canvas = TurtleArt(tim, colors, 15, 15)
    canvas.do_art()

    screen.exitonclick()
