import turtle


class Sketching:

    def __init__(self, turtle, screen, forward, backward, left, right):
        # self.right = right
        # self.left = left
        # self.backward = backward
        # self.forward = forward
        self.turtle = turtle
        self.screen = screen
        self.screen.listen()
        self.screen.onkey(key=forward, fun=self.move_forwards)
        self.screen.onkey(key=backward, fun=self.move_backwards)
        self.screen.onkey(key=left, fun=self.turn_left)
        self.screen.onkey(key=right, fun=self.turn_right)
        self.screen.onkey(key='c', fun=self.clear)

    def move_forwards(self):
        self.turtle.forward(10)

    def move_backwards(self):
        self.turtle.back(10)

    def turn_right(self):
        self.turtle.right(90)

    def turn_left(self):
        self.turtle.left(90)

    def clear(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.home()
        self.turtle.pendown()


