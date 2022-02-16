from turtle import Turtle
from config import Config


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-Config.SCREEN_WIDTH/2+10, Config.SCREEN_HEIGHT/2 - 30)
        self.level = 0

    def update(self):
        self.clear()
        self.write(f'Level: {self.level}', font=Config.SCOREBOARD_FONT)


class Lines(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('pink')
        self.goto(-300, -274)

    def draw_lines(self):
        self.pendown()
        for i in range(int(Config.SCREEN_HEIGHT/30)):
            self.forward(Config.SCREEN_WIDTH)
            self.left(90)
            self.forward(30)
            self.left(90)
            self.forward(Config.SCREEN_WIDTH)
            self.right(90)
            self.forward(30)
            self.right(90)
