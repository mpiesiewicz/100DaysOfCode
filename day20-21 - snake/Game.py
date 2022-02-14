import time
from Config import Config
from Snake import Snake
from Window import Window
from Food import Food
from Score import Scoreboard


class SnakeGame:

    def __init__(self):
        self.screen = Window()
        self.snake = Snake(self.screen)
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.game_is_on = True

    def play(self):
        self.screen.screen_setup()
        self.snake.initialize()
        self.snake.change_direction()
        while self.game_is_on:
            # self.scoreboard.show_score()
            self.screen.update()
            time.sleep(Config.SNAKES_SPEED)
            self.snake.go_snake_go()
            self.did_snake_eat()
            # print(self.snake.head.distance(self.food))
            self.did_snake_hit_the_wall()

        self.screen.exit()

    def did_snake_eat(self):
        if self.snake.head.distance(self.food) < 15:
            self.snake.eat()
            self.food.refresh()
            self.scoreboard.add_score()

    def did_snake_hit_the_wall(self):
        if self.snake.head.xcor() > 500 or self.snake.head.xcor() < -500 or self.snake.head.ycor() > 500 or self.snake.head.ycor() < -500:
            self.scoreboard.game_over()
            self.game_is_on = False
