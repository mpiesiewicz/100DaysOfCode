import random
from turtle import Turtle, Screen
from config import Config

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, up_key):
        super().__init__()
        self.starting_position = (0, -293)
        self.shape('turtle')
        self.color(Config.TURTLE_COLOR)
        self.move_distance = 30
        self.listening_screen = Screen()
        self.up_key = up_key
        self.turtlesize(stretch_len=1.2, stretch_wid=1.2)
        self.setup()

    def setup(self):
        self.penup()
        self.setheading(90)
        self.goto(self.starting_position)
        self.setheading(90)

    def move(self):
        self.listening_screen.listen()
        self.listening_screen.onkey(fun=self.up, key=self.up_key)

    def up(self):
        self.forward(self.move_distance)

    def die(self):
        self.goto(self.xcor()-10, self.ycor())
        self.color('black')
        last_words = random.choice(Config.TURTLE_LAST_WORDS)
        self.write(arg=last_words, align='right', font=('courier', 8, 'italic'))
