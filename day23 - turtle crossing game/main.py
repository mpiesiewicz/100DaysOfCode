import time
from turtle import Screen
from player import Player
from config import Config
from car_manager import CarManager, Car
from scoreboard import Scoreboard


class TurtleCrossing:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=Config.SCREEN_WIDTH, height=Config.SCREEN_HEIGHT)
        self.screen.title('DAMN STREET TURTLES!')
        self.screen.tracer(0)
        self.game_is_on = True
        self.turtle = Player('w')
        self.scoreboard = Scoreboard()
        self.writer = Scoreboard()
        self.manager = CarManager()
        self.game_speed = 200
        self.car_speed = 1

    def play(self):
        self.scoreboard.update()
        self.writer.warn_the_player()
        counter = 0
        while self.game_is_on:
            time.sleep(0.01)
            self.screen.update()
            self.turtle.move()

            if counter % self.game_speed == 0:
                self.manager.generate_a_car(self.car_speed)

            for car in self.manager.vehicles:
                car.move()

            if self.check_collision(counter):
                self.scoreboard.game_over()
                self.game_is_on = False

            if self.check_if_won():
                self.next_round()
            counter += 1

        self.screen.exitonclick()

    def check_collision(self, counter):
        for car in self.manager.vehicles:
            if counter % 100 == 0:
                car.clear()

            if car.ycor() == (self.turtle.ycor() + 5):
                car.beep()
                if car.xcor() - 60 <= self.turtle.xcor() <= car.xcor() + 50:
                    self.turtle.die()
                    car.hit()
                    return True

    def check_if_won(self):
        if self.turtle.ycor() >= Config.SCREEN_HEIGHT/2 - 10:
            return True

    def next_round(self):
        self.manager.clear_cars()
        self.turtle.setup()
        self.scoreboard.add_point()
        self.writer.countdown()
        self.game_speed = self.game_speed/2
        self.car_speed += 0.5


if __name__ == '__main__':
    game = TurtleCrossing()
    game.play()
