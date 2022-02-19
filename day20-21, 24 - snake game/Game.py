import time
from Config import Config
from Snake import Snake
from Window import Window
from Food import Food
from Score import Scoreboard, Writer
from turtle import Screen


class SnakeGame:

    def __init__(self):
        # objects
        self.screen = Window()
        self.listening_screen = Screen()
        self.snake = Snake(self.screen)
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.writer = Writer()
        # attributes
        self.game_is_on = True
        self.keyboard_input = False
        # methods
        self.screen.screen_setup()
        self.snake.initialize()

    def play(self):
        # main game loop
        while self.game_is_on:
            self.screen.update()
            time.sleep(Config.SNAKES_SPEED)
            self.snake.move()
            self.did_snake_eat()
            self.did_snake_hit_the_wall()
            self.did_snake_bite_the_tail()

            # handling game over
            if not self.game_is_on:
                self.keyboard_input = False
                # wait for keyboard input
                while not self.keyboard_input:
                    self.keys_activate()
                    self.screen.update()

        self.screen.exit()

    def did_snake_eat(self):
        if self.snake.head.distance(self.food) < 15:
            self.snake.eat()
            self.food.refresh()
            self.scoreboard.add_score()

    def did_snake_hit_the_wall(self):
        if self.snake.head.xcor() > Config.SCREEN_WIDTH/2-10 or \
                self.snake.head.xcor() < -Config.SCREEN_WIDTH/2-10 or \
                self.snake.head.ycor() > Config.SCREEN_HEIGHT/2-10 or \
                self.snake.head.ycor() < -Config.SCREEN_HEIGHT/2-10:
            self.writer.game_over()
            self.game_is_on = False

    def did_snake_bite_the_tail(self):
        if self.snake.tail_bite():
            self.writer.game_over()
            self.game_is_on = False

    def restart(self):
        self.keyboard_input = True
        self.game_is_on = True
        self.keys_deactivate()
        self.writer.clear()
        # if self.scoreboard.score > self.scoreboard.high_score:
        #     self.scoreboard.update_high_score()
        self.snake.remove()
        self.snake = Snake(self.screen)
        self.snake.initialize()
        self.scoreboard.initialize()

    def quit(self):
        self.game_is_on = False
        self.keyboard_input = True

    def keys_activate(self):
        self.listening_screen.onkey(fun=self.restart, key='y')
        self.listening_screen.onkey(fun=self.quit, key='n')
        self.listening_screen.listen()

    def keys_deactivate(self):
        self.listening_screen.onkey(fun=None, key='y')
        self.listening_screen.onkey(fun=None, key='n')
