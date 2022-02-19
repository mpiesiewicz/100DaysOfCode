from turtle import Turtle, Screen
from Config import Config


class Snake:

    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

    def __init__(self, screen, speed=Config.SNAKES_SPEED):
        self.speed = speed
        self.snake_list = []
        self.new_piece = None
        self.screen = screen
        self.listening_screen = Screen()
        self.head = None

    def initialize(self):
        for position in self.STARTING_POSITIONS:
            self.extend_the_snake(position)
        self.head = self.snake_list[0]
        self.change_direction()

    def extend_the_snake(self, position):
        self.new_piece = Turtle('turtle')
        self.new_piece.color('white')
        self.new_piece.penup()
        if self.head is not None:
            last_piece_heading = self.snake_list[-1].heading()
            self.new_piece.setheading(last_piece_heading)
        self.new_piece.goto(position)
        self.snake_list.append(self.new_piece)

    def move(self):
        for seg_num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[seg_num - 1].xcor()
            new_y = self.snake_list[seg_num - 1].ycor()
            frontal_seg_heading = self.snake_list[seg_num - 1].heading()
            self.snake_list[seg_num].goto(new_x, new_y)
            self.snake_list[seg_num].setheading(frontal_seg_heading)

        self.change_direction()
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

    def eat(self):
        self.extend_the_snake(self.snake_list[-1].position())

    def tail_bite(self):
        for segment in self.snake_list[1:]:
            if self.head.distance(segment) < 10:
                return True

    def remove(self):
        # move snake away from the screen
        for element in self.snake_list:
            element.goto(Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT)

