from Game import SnakeGame


if __name__ == '__main__':

    # Screen setup
    # screen = Screen()
    # screen.setup(width=600, height=600)
    # screen.bgcolor('black')
    # screen.title('snakes snakes everywhere')

    # snake = []
    # for i in range(3):
    #     new_piece = Turtle('square')
    #     new_piece.color('white')
    #     new_piece.setposition(i*(-20), 0)
    #     snake.append(new_piece)

    game = SnakeGame()
    game.play()
