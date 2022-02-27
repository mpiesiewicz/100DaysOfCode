import random
import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
from random import randint, choice
import time
import functools


BACKGROUND_COLOR = "#B1DDC6"
FONT_WORD = ('Ariel', 20, 'bold')
FONT_LANGUAGE = ('Ariel', 10, 'italic')


def cards_resize(img, width, height):
    image = Image.open(img)
    image = image.resize((width, height), Image.ANTIALIAS)
    photo_img = ImageTk.PhotoImage(image)
    return photo_img


def next_card():
    global flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(image, image=card_front)
    current_card = random.choice(to_learn)
    canvas.itemconfig(label_word, text=current_card['French'], fill='black')
    canvas.itemconfig(label_language, text='French', fill='black')
    flip_timer = window.after(3000, lambda: flip_card(current_card))


def flip_card(current_card):
    canvas.itemconfig(image, image=card_back)
    canvas.itemconfig(label_word, text=current_card['English'], fill='white')
    canvas.itemconfig(label_language, text='English', fill='white')

# Window settings
window = tk.Tk()
window.title('Flashy')
window.minsize(width=320, height=220)
window.config(pady=20, padx=20, background=BACKGROUND_COLOR)
window.resizable(width=False, height=False)

# Data loading
data = pd.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient='records')


# ------------------- UI SETTINGS -------------------

# images
card_front = cards_resize('images/card_front.png', 300, 150)
card_back = cards_resize('images/card_back.png', 300, 150)
tick_right = cards_resize('images/right.png', 25, 25)
tick_wrong = cards_resize('images/wrong.png', 25, 25)

# canvas
canvas = tk.Canvas(width=300, height=150, highlightthickness=0)
image = canvas.create_image(150, 75, image=card_front)
label_language = canvas.create_text(150, 40, font=FONT_LANGUAGE, text='sample')
label_word = canvas.create_text(150, 75, font=FONT_WORD, text='word')

btn_right = tk.Button(image=tick_right, highlightthickness=False, borderwidth=0, command=next_card)
btn_wrong = tk.Button(image=tick_wrong, highlightthickness=False, borderwidth=0, command=next_card)

canvas.grid(column=0, row=0, columnspan=2, rowspan=5)
btn_wrong.grid(column=0, row=5)
btn_right.grid(column=1, row=5)

flip_timer = window.after(0, next_card)

window.mainloop()
