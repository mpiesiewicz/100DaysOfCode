import random


class TurtleRace:

    COLOURS = ['black', 'green', 'yellow', 'purple', 'orange', 'pink', 'blue']

    def __init__(self, screen, participants):
        self.screen = screen
        self.participants = participants
        self.width = 500
        self.height = 400
        self.screen.setup(width=self.width, height=self.height)
        self.user_bet = self.make_a_bet()
        self.is_race_on = False

    def make_a_bet(self):
        return self.screen.textinput(title='Make your bet',
                                     prompt=f'Which turtle will win the race? Enter a colour: \n'
                                            f'Available colours: {TurtleRace.COLOURS}')

    def goto_start(self):
        for counter, turtle in enumerate(self.participants):
            turtle.penup()
            turtle.color(TurtleRace.COLOURS[counter])
            x_position = -self.width/2+10

            top_margin = (self.height-(len(self.participants)-1)*30)/2

            y_position = (self.height/2)-top_margin-(30*counter)
            turtle.goto(x=x_position, y=y_position)

    def race(self):
        self.goto_start()
        self.is_race_on = True
        while self.is_race_on:
            for turtle in self.participants:
                if turtle.xcor() > self.width/2 - 30:
                    winning_turtle = turtle.pencolor()
                    print(f'Turtle {winning_turtle} won!')
                    if self.user_bet == winning_turtle:
                        print('You won! Good choice!')
                    else:
                        print('You lost! Looooser!!!')
                    self.is_race_on = False
                random_distance = random.randint(1, 10)
                turtle.forward(random_distance)


