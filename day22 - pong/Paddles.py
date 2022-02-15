from turtle import Turtle, Screen
from Config import Config


class Paddle(Turtle):
    def __init__(self, position, up_key, down_key):
        super().__init__()
        self.shape('square')
        self.turtlesize(1, 5)
        self.color('pink')
        self.penup()
        self.setheading(90)
        self.goto(position)
        self.listening_screen = Screen()
        self.up_key = up_key
        self.down_key = down_key
        self.paddle_speed = 2

    def move(self):
        self.listening_screen.listen()
        self.listening_screen.onkey(fun=self.up, key=self.up_key)
        self.listening_screen.onkey(fun=self.down, key=self.down_key)

        if (Config.SCREEN_HEIGHT / 2 <= self.ycor() and self.heading() == 90) or \
                -Config.SCREEN_HEIGHT / 2 >= self.ycor() and self.heading() == 270:
            self.forward(0)
        else:
            self.forward(self.paddle_speed)

    def up(self):
        self.setheading(90)

    def down(self):
        self.setheading(270)
