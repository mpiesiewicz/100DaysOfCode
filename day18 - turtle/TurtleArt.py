import random


class TurtleArt:
    def __init__(self, turtle, colours, rows, columns):
        self.rows = rows
        self.columns = columns
        self.colours = colours
        self.turtle = turtle
        self.turtle.penup()
        self.direction_flag = 90

    # 90 is right, 270 is left
    def change_direction(self):
        if self.direction_flag == 90:
            self.direction_flag = 270
        else:
            self.direction_flag = 90

    def turn_to_next_row(self):
        for _ in range(2):
            self.turtle.left(self.direction_flag)
            self.turtle.forward(50)

    def draw_row(self):
        for _ in range(self.columns):
            random_colour = random.choice(self.colours)
            self.turtle.dot(20, random_colour)
            self.turtle.forward(50)

    def do_art(self):
        self.turtle.setposition(-250, -250)
        for c in range(self.rows):
            self.draw_row()
            self.turn_to_next_row()
            self.change_direction()
