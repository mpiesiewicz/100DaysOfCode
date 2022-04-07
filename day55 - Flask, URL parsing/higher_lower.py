from flask import Flask
from random import randint

app = Flask(__name__)
correct_number = randint(0, 9)


@app.route('/')
def main_page():
    return "<h1>Guess a number between 0 and 9</h1>" \
           '<img src="https://media1.giphy.com/media/5zoxhCaYbdVHoJkmpf/giphy.gif?cid=ecf05e47114cmb5lp82p66wnb7g6916l114srxyt0c53lrfu&rid=giphy.gif&ct=g" width="480">'


@app.route("/<int:number>")
def answer(number):
    if number == correct_number:
        return f"<h1 style='color:green'>Correct!</h1>" \
               f"<img src='https://media1.giphy.com/media/wpoLqr5FT1sY0/giphy.gif?cid=ecf05e47hjc2igu5i4yuo909a5imilxtq2xuxyh1hfsduvgy&rid=giphy.gif&ct=g' width='480'>"

    elif number < correct_number:
        return f"<h1 style='color:red'>Too low!</h1>" \
               f"<img src='https://media3.giphy.com/media/ZeHqFM9JNauty/giphy.gif?cid=ecf05e47674qsbm0h60qtnz9dphq8mq2cue0okmg16vdhymh&rid=giphy.gif&ct=g' width='480'>"

    elif number > correct_number:
        return f"<h1 style='color:red'>Too high!</h1>" \
               f"<img src='https://media3.giphy.com/media/yvgaJzI8Q01Ow/giphy.gif?cid=ecf05e47528is829obc39b92bjevfi1sn8ganp3sr2zkrz52&rid=giphy.gif&ct=g' width='480'>"


if __name__ == '__main__':
    app.run(debug=True)
