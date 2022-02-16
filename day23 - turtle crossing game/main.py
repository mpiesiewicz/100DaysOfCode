import time
from turtle import Screen
from player import Player
from config import Config
from car_manager import CarManager, Car
from scoreboard import Scoreboard, Lines


class TurtleCrossing:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=Config.SCREEN_WIDTH, height=Config.SCREEN_HEIGHT)
        self.screen.tracer(0)
        self.game_is_on = True
        self.turtle = Player('w')
        self.scoreboard = Scoreboard()
        self.manager = CarManager()
        self.line_drawer = Lines()
        # self.line_drawer.draw_lines()

    def play(self):
        self.scoreboard.update()
        counter = 0
        while self.game_is_on:
            time.sleep(0.01)
            self.screen.update()
            self.turtle.move()
            for car in self.manager.vehicles:
                car.move()
            if counter % 200 == 0:
                self.manager.generate_a_car()
            self.check_collision()
            print('T:', self.turtle.ycor() + 5)
            counter += 1

        self.screen.exitonclick()

    def check_collision(self):
        for car in self.manager.vehicles:
            print(car.ycor())
            if car.ycor != (self.turtle.ycor() + 5):
                continue
            print('Ys bang')


if __name__ == '__main__':
    game = TurtleCrossing()
    game.play()
