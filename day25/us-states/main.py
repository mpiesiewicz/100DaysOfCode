import turtle
from turtle import Turtle, Screen


class StatesGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.title('U.S. States Game')
        self.image = 'blank_states_img.gif'
        self.screen.addshape(self.image)

        self.turtle = Turtle()
        turtle.shape(self.image)

        # self.game_is_on = True

    def play(self):
        # self.screen.onscreenclick(self.get_mouse_click_coor)
        answer_state = self.screen.textinput(title='Guess the State', prompt="What's another state's name?")

        self.screen.mainloop()

    @staticmethod
    def get_mouse_click_coor(x, y):
        print(x, y)


if __name__ == '__main__':
    game = StatesGame()
    game.play()