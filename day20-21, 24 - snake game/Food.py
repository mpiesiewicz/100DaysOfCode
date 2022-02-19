from turtle import Turtle
import random
from Config import Config


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(Config.FOOD_COLOUR)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-Config.SCREEN_WIDTH/2+20, Config.SCREEN_WIDTH/2-20)
        random_y = random.randint(-Config.SCREEN_HEIGHT/2+20, Config.SCREEN_HEIGHT/2-20)
        self.goto(random_x, random_y)
