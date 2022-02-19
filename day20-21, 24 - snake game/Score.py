from turtle import Turtle
from Config import Config


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # attributes
        self.score = 0
        self.high_score = self.load_high_score()
        self.color('white')
        # methods
        self.hideturtle()
        self.penup()
        self.goto(0, Config.SCREEN_HEIGHT/2-30)
        self.update_scoreboard()

    def initialize(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.clear()
        self.update_scoreboard()

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align='center', font=Config.SCOREBOARD_FONT)

    @staticmethod
    def load_high_score():
        with open('high_score.txt') as file:
            return int(file.read())

    def update_high_score(self):
        with open('high_score.txt', mode='w') as file:
            file.write(str(self.score))


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!', align='center', font=Config.SCOREBOARD_FONT)
        self.goto(0, -20)
        self.write(f'Do you want to play again? y/n', align='center', font=Config.SCOREBOARD_FONT)

