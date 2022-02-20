import turtle
import pandas as pd
from turtle import Turtle, Screen
from turtles import Writer


class StatesGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.title('U.S. States Game')
        self.image = 'blank_states_img.gif'
        self.screen.addshape(self.image)
        self.right_guesses = list()
        self.game_is_on = True

        self.turtle = Turtle()
        turtle.shape(self.image)
        self.writer = Writer()

        # self.game_is_on = True

    def play(self):
        while self.game_is_on:
            # ask for a state
            title = f'{len(self.right_guesses)}/50 States Correct'
            answer_state = self.screen.textinput(title=title, prompt="What's another state's name? "
                                                                     "\nType 'exit' to give up.").title()
            # read data
            data = pd.read_csv('50_states.csv')
            # check if correct
            if answer_state in list(data.state) and answer_state not in self.right_guesses:
                self.right_guesses.append(answer_state)
                # print name to the map
                state_data = data[data.state == answer_state]
                self.writer.state_write(int(state_data.x), int(state_data.y), answer_state)

            # exit at win
            if len(self.right_guesses) == 50:
                self.writer.state_write(0, 0, 'ALL 50 STATES! CONGRATS!')
                self.game_is_on = False

            # exit when user gives up, fill missing states and print them to csv
            if answer_state == 'Exit':
                with open('states_to_learn.txt', mode='w') as file:
                    file.truncate()

                with open('states_to_learn.txt', mode='a') as file:
                    for state in data.state:
                        if state not in self.right_guesses:
                            state_data = data[data.state == state]
                            self.writer.state_write(int(state_data.x), int(state_data.y), state)
                            file.write(state + '\n')

                self.game_is_on = False

        self.screen.exitonclick()
        self.screen.mainloop()

    @staticmethod
    def load_data():
        data = pd.read_csv('50_states.csv')
        return data

    @staticmethod
    def get_mouse_click_coor(x, y):
        print(x, y)


if __name__ == '__main__':
    game = StatesGame()
    game.play()
