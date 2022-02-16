from turtle import Turtle
from Config import Config


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('pink')
        self.penup()
        self.goto(0, Config.SCREEN_HEIGHT/2-40)
        self.player1_score = 0
        self.player2_score = 0
        self.update()

    def update(self):
        self.write(f"{self.player1_score} | {self.player2_score}", align='center', font=Config.SCOREBOARD_FONT)
