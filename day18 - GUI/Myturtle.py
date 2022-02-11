import math
import random


class MyTurtle:

    COLOURS = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue']

    @staticmethod
    def dashed_forward(moving_object, length, dash_length=5):
        rounded_length = math.floor(length/dash_length)*dash_length
        rest = length - rounded_length
        loops = rounded_length/dash_length/2 # /2 because in each step we move forward twice
        for _ in range(int(loops)):
            moving_object.forward(dash_length)
            moving_object.penup()
            moving_object.forward(dash_length)
            moving_object.pendown()
        moving_object.forward(rest) # move the rest


    # draw heptagon or any gon you want.
    @staticmethod
    def gon(moving_object, number_of_walls, length):
        angle = 360 - (360 / number_of_walls)
        for _ in range(number_of_walls):
            moving_object.forward(length)
            moving_object.right(angle)

    @staticmethod
    def shape_in_shape(moving_object):
        for shape_side_n in range(3, 11):
            colour = MyTurtle.COLOURS[random.randint(0, len(MyTurtle.COLOURS) - 1)]
            moving_object.pencolor(colour)
            MyTurtle.gon(moving_object, shape_side_n, 100)

    @staticmethod
    def random_walk(moving_object):
        moving_object.speed(0)
        moving_object.width(1)
        while True:
            colour_number = random.randint(0, len(MyTurtle.COLOURS) - 1)
            moving_object.color(MyTurtle.COLOURS[colour_number])
            random_angle = random.choice([90, 180, 270, 360])
            moving_object.forward(5)
            moving_object.right(random_angle)

    @staticmethod
    def random_colour():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b

    @staticmethod
    def spirograph(moving_object):
        moving_object.speed(6)
        moving_object.width(5)
        number_of_circles = 10
        for _ in range(number_of_circles):
            moving_object.pencolor(MyTurtle.random_colour())
            moving_object.circle(80)
            moving_object.left(360/number_of_circles)
