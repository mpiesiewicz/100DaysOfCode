from Snake import Snake
from Window import Window


class SnakeGame:

    def __init__(self):
        self.screen = Window()
        self.snake = Snake(self.screen)
        self.game_is_on = True

    def play(self):
        self.screen.screen_setup()
        self.snake.initialize()
        self.snake.change_direction()
        while self.game_is_on:
            self.snake.go_snake_go()
        self.screen.exit()


