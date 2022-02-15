import turtle
from PIL import Image
from Config import Config
from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('red')
        turtle.register_shape('heart_transformed.gif')
        self.shape('heart_transformed.gif')
        self.initialize()
        self.time_speed = 4

    def bounce(self):
        if self.ycor() <= -Config.SCREEN_HEIGHT/2+12 or \
                self.ycor() >= Config.SCREEN_HEIGHT/2-12:
            self.setheading(360 - self.heading())

    def move(self):
        self.forward(self.time_speed)
        self.bounce()

    def initialize(self):
        self.goto(0, 0)
        # 315-359 - 1-45 / 135-225
        random_direction = random.choice([random.randint(135, 225), random.randint(135+180, 225+180)])
        self.setheading(random_direction)
        # self.setheading(12)


def resize():
    heart_ball = 'heart.gif'
    with Image.open(heart_ball) as im:
        im_resized = im.resize((15, 15))
        im_resized.save('heart_transformed.gif')

