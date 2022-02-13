from turtle import Screen


class Window:

    def __init__(self):
        self.screen = Screen()

    def screen_setup(self):
        self.screen.setup(width=1000, height=1000)
        self.screen.bgcolor('black')
        self.screen.title('snakes, snakes everywhere!')
        self.screen.tracer(0)

    def update(self):
        self.screen.update()

    def exit(self):
        self.screen.exitonclick()