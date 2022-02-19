from turtle import Screen
from Config import Config


class Window:

    def __init__(self):
        self.screen = Screen()

    def screen_setup(self):
        self.screen.setup(width=Config.SCREEN_WIDTH,
                          height=Config.SCREEN_HEIGHT)
        self.screen.bgcolor('black')
        self.screen.title('snakes, snakes everywhere!')
        self.screen.tracer(0)

    def update(self):
        self.screen.update()

    def exit(self):
        self.screen.bye()
