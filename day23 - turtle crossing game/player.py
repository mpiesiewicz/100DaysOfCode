from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, up_key):
        super().__init__()
        self.starting_position = (0, -293)
        self.penup()
        self.setheading(90)
        self.shape('turtle')
        self.color('green')
        self.goto(self.starting_position)
        self.move_distance = 30
        self.listening_screen = Screen()
        self.up_key = up_key
        # self.turtlesize(stretch_len=0.80)
        self.turtlesize(stretch_len=1.2, stretch_wid=1.2)

    def move(self):
        self.listening_screen.listen()
        self.listening_screen.onkey(fun=self.up, key=self.up_key)

    def up(self):
        self.forward(self.move_distance)

