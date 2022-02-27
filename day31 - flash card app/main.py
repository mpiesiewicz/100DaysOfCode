import random
import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
from PIL import Image, ImageTk
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT_WORD = ('Ariel', 20, 'bold')
FONT_LANGUAGE = ('Ariel', 10, 'italic')
FONT_POPULARITY = ('Ariel', 10, 'italic')
SEEN_CARDS = list()
current_card = dict()
current_card_index = int()
words_to_learn = str()
data_file = str()

with open('settings.txt') as settings_file:
    LANGUAGE = settings_file.read()

if LANGUAGE == 'FR':
    language_flag = 'French'
else:
    language_flag = 'Spanish'


def cards_resize(img, width, height):
    image = Image.open(img)
    image = image.resize((width, height), Image.ANTIALIAS)
    photo_img = ImageTk.PhotoImage(image)
    return photo_img


def data_initialize():
    global language_flag, words_to_learn, data_file, to_learn

    if LANGUAGE == 'FR':
        language_flag = 'French'
    else:
        language_flag = 'Spanish'

    data_file = 'data/' + LANGUAGE + '_words.csv'
    words_to_learn = 'data/' + LANGUAGE + '_words_to_learn.csv'

    try:
        data = pd.read_csv(words_to_learn)
    except pd.errors.EmptyDataError:
        data = pd.read_csv(data_file)
    to_learn = data.to_dict(orient='records')
    return to_learn


def reset():
    global to_learn
    rows = 9000
    while rows >= 8001:
        rows = tkinter.simpledialog.askinteger('Resetting...', 'How many words do you want to know?\n'
                                                              'Max 8000')
    data = pd.read_csv(data_file, nrows=rows)
    data.to_csv(words_to_learn, index=False)
    to_learn = data.to_dict(orient='records')
    next_card()


def known():
    global current_card_index
    to_learn.pop(current_card_index)
    if len(to_learn) == 0:
        tkinter.messagebox.showinfo(title='CONGRATS!', message='You know all the words!\n'
                                                               'Impressive. Resetting...')
        reset()
    else:
        next_card()


def next_card():
    global flip_timer, current_card, current_card_index, LANGUAGE, language_flag

    # prevent drawing the same index again
    old_index = current_card_index
    current_card_index = random.randint(0, len(to_learn) - 1)
    while old_index == current_card_index and len(to_learn) != 1:
        current_card_index = random.randint(0, len(to_learn) - 1)

    current_card = to_learn[current_card_index]

    window.after_cancel(flip_timer)
    canvas.itemconfig(image, image=card_front)
    canvas.itemconfig(label_word, text=current_card[LANGUAGE], fill='black')
    canvas.itemconfig(label_language, text=language_flag, fill='black')
    canvas.itemconfig(label_popularity, text=current_card['Popularity'], fill='black')

    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(image, image=card_back)
    canvas.itemconfig(label_word, text=current_card['English'], fill='white')
    canvas.itemconfig(label_language, text='English', fill='white')
    canvas.itemconfig(label_popularity, text=current_card['Popularity'], fill='white')

    SEEN_CARDS.append(current_card)


def language_fr():
    on_closing(False)
    global LANGUAGE
    LANGUAGE = "FR"
    data_initialize()


def language_es():
    on_closing(False)
    global LANGUAGE
    LANGUAGE = "ES"
    data_initialize()


def on_closing(destroy=True):
    saved_data = pd.DataFrame(to_learn)
    saved_data.to_csv(words_to_learn, index=False)

    with open('settings.txt', 'w') as settings_file:
        settings_file.write(LANGUAGE)

    if destroy:
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
label_popularity = canvas.create_text(250, 130, font=FONT_POPULARITY, text='1')

btn_right = tk.Button(image=tick_right, highlightthickness=False, borderwidth=0, command=known)
btn_wrong = tk.Button(image=tick_wrong, highlightthickness=False, borderwidth=0, command=next_card)

canvas.grid(column=0, row=0, columnspan=2, rowspan=5)
btn_wrong.grid(column=0, row=5)
btn_right.grid(column=1, row=5)

# menubar
menubar = tk.Menu(window)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Reset', command=reset)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=on_closing)
menubar.add_cascade(label="File", menu=filemenu)

Languages_menu = tk.Menu(menubar, tearoff=0)
Languages_menu.add_command(label='FR', command=language_fr)
Languages_menu.add_command(label='ES', command=language_es)
menubar.add_cascade(label="Languages", menu=Languages_menu)

window.config(menu=menubar)

flip_timer = window.after(0, next_card)

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
