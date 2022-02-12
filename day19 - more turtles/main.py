from turtle import Turtle, Screen
from Sketching import Sketching
from TurtleRacing import TurtleRace

if __name__ == '__main__':

    # Turtles settings
    tim = Turtle(shape='turtle')
    danny = Turtle(shape='turtle')
    mick = Turtle(shape='turtle')
    luke = Turtle(shape='turtle')
    zozo = Turtle(shape='turtle')
    dodo = Turtle(shape='turtle')
    magda = Turtle(shape='turtle')

    tim.width = 10

    # Screen settings
    screen = Screen()

    # Two independent turtles game
    # game = Sketching(tim, screen, forward='w', backward='s', left='a', right='d')
    # game2 = Sketching(danny, screen, forward='Up', backward='Down', left='Left', right='Right')

    # Turtle Racing game
    participants = [tim, danny, mick, luke, zozo, dodo, magda]
    race = TurtleRace(screen, participants)
    race.race()

    screen.exitonclick()