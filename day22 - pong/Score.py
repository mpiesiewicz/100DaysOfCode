from turtle import Turtle
from Config import Config
import time


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('pink')
        self.penup()
        self.goto(0, Config.SCREEN_HEIGHT/2-40)
        self.player1_score = 0
        self.player2_score = 0

    def update(self):
        self.write(f"{self.player1_score} | {self.player2_score}", align='center', font=Config.SCOREBOARD_FONT)

    def countdown(self):
        self.goto(0, 0)
        for c in range(3, 0, -1):
            self.write(f'{str(c)}', align='center', font=Config.SCOREBOARD_FONT)
            time.sleep(0.5)
            self.clear()

#
# class Counter(Scoreboard):
#     def __init__(self):
#         super().__init__()
#         self.goto()