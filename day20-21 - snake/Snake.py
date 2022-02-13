from turtle import Turtle, Screen
import time


class Snake:

    def __init__(self, screen, speed=0.5):
        self.speed = speed
        self.snake_list = []
        self.new_piece = None
        self.screen = screen
        self.listening_screen = Screen()
        self.head = None

    def initialize(self):
        for i in range(3):
            self.new_piece = Turtle('turtle')
            self.new_piece.color('white')
            self.new_piece.penup()
            self.new_piece.setposition(i*(-20), 0)
            self.snake_list.append(self.new_piece)
        self.head = self.snake_list[0]

    def go_snake_go(self):
        self.screen.update()
        # self.change_direction()
        time.sleep(self.speed)

        for seg_num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[seg_num - 1].xcor()
            new_y = self.snake_list[seg_num - 1].ycor()
            self.snake_list[seg_num].goto(new_x, new_y)

        # self.snake_list[0].setheading(random.choice([0, 90, 180, 270]))
        self.head.forward(20)

    def change_direction(self):
        self.listening_screen.listen()
        self.listening_screen.onkey(fun=self.up, key='Up')
        self.listening_screen.onkey(fun=self.down, key='Down')
        self.listening_screen.onkey(fun=self.left, key='Left')
        self.listening_screen.onkey(fun=self.right, key='Right')

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
