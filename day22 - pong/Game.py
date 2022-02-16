from Screens import Window
from Paddles import Paddle
from Config import Config
from Balls import Ball
from Score import Scoreboard
import time
import random


class PongGame:

    def __init__(self):
        self.window = Window()
        self.game_is_on = True
        self.left_paddle = Paddle((-Config.SCREEN_WIDTH / 2 + 20, 0), 'w', 's')
        self.right_paddle = Paddle((Config.SCREEN_WIDTH / 2 - 20, 0), 'Up', 'Down')
        self.ball = Ball()
        self.scoreboard = Scoreboard()
        self.counter = Scoreboard()

    def play(self):
        self.window.setup()
        self.scoreboard.update()
        self.counter.countdown()
        while self.game_is_on:
            self.window.update()
            time.sleep(Config.GAME_SPEED)
            self.left_paddle.move()
            self.right_paddle.move()
            self.ball.move()
            self.check_paddle_bounce()
            if self.check_scored():
                self.next_round()
        self.window.exit()

    def check_paddle_bounce(self):
        if self.ball.xcor() >= Config.SCREEN_WIDTH/2-37:
            if self.right_paddle.ycor()-50 <= self.ball.ycor() <= self.right_paddle.ycor()+50:
                self.paddle_bounce()
        if self.ball.xcor() <= -Config.SCREEN_WIDTH/2+37:
            if self.left_paddle.ycor()-50 <= self.ball.ycor() <= self.left_paddle.ycor()+50:
                self.paddle_bounce()

    def paddle_bounce(self):
        self.ball.setheading(180 - self.ball.heading() + random.randint(-5, 5))
        print(self.ball.heading())

    def check_scored(self):
        if -Config.SCREEN_WIDTH/2 >= self.ball.xcor():
            print('Score for right side')
            self.scoreboard.player2_score += 1
            return True
        if Config.SCREEN_WIDTH/2 <= self.ball.xcor():
            print('Score for left side')
            self.scoreboard.player1_score += 1
            return True

    def next_round(self):
        self.scoreboard.clear()
        self.scoreboard.update()
        self.counter.countdown()
        self.ball.initialize()
        self.ball.time_speed += 0.1
        self.left_paddle.paddle_speed = self.right_paddle.paddle_speed = self.ball.time_speed/2
