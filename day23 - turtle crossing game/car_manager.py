from turtle import Turtle
from config import Config
import random


class CarManager:
    def __init__(self):
        self.vehicles = []

    def generate_a_car(self, car_speed=1):
        new_car = Car(car_speed)
        self.vehicles.append(new_car)

    def clear_cars(self):
        for car in self.vehicles:
            car.hideturtle()
            car.goto(Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT)
        self.vehicles.clear()


class Car(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed
        self.color(random.choice(Config.CAR_COLORS))
        self.shape('square')
        self.shapesize(stretch_wid=1.46, stretch_len=5)
        self.penup()
        self.setheading(180)
        self.setup()
        self.car_speed = speed
        self.beeps = 0

    def setup(self):
        x = Config.SCREEN_WIDTH / 2 + 100
        random_y = random.randrange(-Config.SCREEN_HEIGHT/2+102, Config.SCREEN_HEIGHT/2-100, 30)
        self.goto(x, random_y)

    def move(self):
        self.forward(self.car_speed)

    def hit(self):
        self.color('black')
        self.goto(self.xcor(), self.ycor()+15)
        self.write(random.choice(Config.DRIVERS_LAST_WORDS), align='center', font=('Comic Sans MS', 10, 'normal'))

    def beep(self):
        # randomize beep:
        self.beeps += random.randint(0, 1)

        # do not beep when turtle is passed
        if self.xcor() < 15:
            self.beeps += 1

        # beep
        if self.beeps < 1:
            self.goto(self.xcor(), self.ycor())
            self.write(random.choice(Config.BEEPS))
            self.beeps += 1

        # when car passed the turtle
        if self.xcor() < 0 and random.randint(0, 1) and self.beeps == 1:
            self.write(random.choice(Config.DRIVERS_WARNINGS))

