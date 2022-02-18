from turtle import Turtle
from config import Config
import time


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-Config.SCREEN_WIDTH/2+10, Config.SCREEN_HEIGHT/2 - 30)
        self.level = 1

    def update(self):
        self.clear()
        self.write(f'Level: {self.level}', font=Config.SCOREBOARD_FONT)

    def warn_the_player(self):
        self.goto(0, 0)
        self.write('Click W to move up.')
        time.sleep(2)
        self.clear()
        self.write('But be careful!')
        time.sleep(2)
        self.clear()
        self.write('Cars are murderous, \nand much heavier than a turtle!', align='center')
        time.sleep(3)
        self.clear()

    def game_over(self):
        self.goto(0, Config.SCREEN_HEIGHT/2-50)
        self.write(f'SPLASH! \n Levels: {self.level}', align='center', font=Config.SCOREBOARD_FONT)

    def add_point(self):
        self.level += 1
        self.update()

    def countdown(self):
        for i in range(3, 0, -1):
            self.write(f'{str(i)}')
            time.sleep(1)
            self.clear()

#
# class Lines(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.hideturtle()
#         self.penup()
#         self.color('pink')
#         self.goto(-300, -274)

    # def draw_lines(self):
    #     self.pendown()
    #     for i in range(int(Config.SCREEN_HEIGHT/30)):
    #         self.forward(Config.SCREEN_WIDTH)
    #         self.left(90)
    #         self.forward(30)
    #         self.left(90)
    #         self.forward(Config.SCREEN_WIDTH)
    #         self.right(90)
    #         self.forward(30)
    #         self.right(90)
