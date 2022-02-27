import random
import tkinter as tk
import tkinter.messagebox

from PIL import Image, ImageTk
import pandas as pd
from random import randint, choice
import time
import functools


BACKGROUND_COLOR = "#B1DDC6"
FONT_WORD = ('Ariel', 20, 'bold')
FONT_LANGUAGE = ('Ariel', 10, 'italic')
SEEN_CARDS = list()
current_card = dict()
current_card_index = int()


def cards_resize(img, width, height):
    image = Image.open(img)
    image = image.resize((width, height), Image.ANTIALIAS)
    photo_img = ImageTk.PhotoImage(image)
    return photo_img


def data_initialize():
    try:
        data = pd.read_csv('data/words_to_learn.csv')
    except pd.errors.EmptyDataError:
        data = pd.read_csv('data/french_words.csv')
    to_learn = data.to_dict(orient='records')
    return to_learn


def not_known():
    global current_card, current_card_index
    next_card()


def known():
    global current_card_index
    to_learn.pop(current_card_index)
    if len(to_learn) == 0:
        tkinter.messagebox.showinfo(title='CONGRATS!', message='You know all the words.')
        on_closing()
    else:
        next_card()


def next_card():
    global flip_timer, current_card, current_card_index

    # prevent drawing the same index again
    old_index = current_card_index
    current_card_index = random.randint(0, len(to_learn) - 1)
    while old_index == current_card_index and len(to_learn) != 1:
        current_card_index = random.randint(0, len(to_learn) - 1)

    current_card = to_learn[current_card_index]

    window.after_cancel(flip_timer)
    canvas.itemconfig(image, image=card_front)
    canvas.itemconfig(label_word, text=current_card['French'], fill='black')
    canvas.itemconfig(label_language, text='French', fill='black')
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(image, image=card_back)
    canvas.itemconfig(label_word, text=current_card['English'], fill='white')
    canvas.itemconfig(label_language, text='English', fill='white')
    SEEN_CARDS.append(current_card)


def on_closing():
    saved_data = pd.DataFrame(to_learn)
    saved_data.to_csv('data/words_to_learn.csv', index=False)
    window.destroy()


# Window settings
window = tk.Tk()
window.title('Flashy')
window.minsize(width=320, height=220)
window.config(pady=20, padx=20, background=BACKGROUND_COLOR)
window.resizable(width=False, height=False)

# Data loading
to_learn = data_initialize()


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

btn_right = tk.Button(image=tick_right, highlightthickness=False, borderwidth=0, command=known)
btn_wrong = tk.Button(image=tick_wrong, highlightthickness=False, borderwidth=0, command=not_known)

canvas.grid(column=0, row=0, columnspan=2, rowspan=5)
btn_wrong.grid(column=0, row=5)
btn_right.grid(column=1, row=5)

flip_timer = window.after(0, not_known)

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
