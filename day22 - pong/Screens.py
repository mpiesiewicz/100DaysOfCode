from turtle import Screen
from Config import Config


class Window:
    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)

    def setup(self):
        self.screen.setup(width=Config.SCREEN_WIDTH,
                          height=Config.SCREEN_HEIGHT)
        self.screen.bgcolor('white')
        self.screen.title('Ping Pong dla Madzi <3')

    def update(self):
        self.screen.update()

    def exit(self):
        self.screen.exitonclick()
