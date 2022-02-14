from turtle import Turtle
from Config import Config


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, Config.SCREEN_HEIGHT/2-30)
        self.hideturtle()
        self.update_scoreboard()

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align='center', font=Config.SCOREBOARD_FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!', align='center', font=Config.SCOREBOARD_FONT)
