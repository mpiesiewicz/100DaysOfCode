from turtle import Turtle


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def state_write(self, x_cor, y_cor, text):
        self.goto(x_cor, y_cor)
        self.write(text, align='center')
