from turtle import Turtle
from config import Config
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.vehicles = []
        self.number_of_cars = 1

    def generate_a_car(self):
        new_car = Car()
        self.vehicles.append(new_car)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape('square')
        self.shapesize(stretch_wid=1.46, stretch_len=5)
        self.penup()
        self.setheading(180)
        self.setup()

    def setup(self):
        x = Config.SCREEN_WIDTH / 2 + 100
        # -195 - +205
        random_y = random.randrange(-Config.SCREEN_HEIGHT/2+102, Config.SCREEN_HEIGHT/2-100, 30)
        self.goto(x, random_y)

    def move(self):
        self.forward(1)
