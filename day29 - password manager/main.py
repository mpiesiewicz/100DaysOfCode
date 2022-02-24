import tkinter
from tkinter import Tk, Menu, messagebox, PhotoImage, Canvas, Label, Entry, Button, Toplevel, Text, scrolledtext
from tkinter.simpledialog import askstring
from random import choice, randint, shuffle
import pandas as pd
import pyperclip
from itsdangerous import URLSafeSerializer, BadSignature
import csv
from tempfile import NamedTemporaryFile
import shutil


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    random_letters = [choice(letters) for _ in range(nr_letters)]
    random_symbols = [choice(symbols) for _ in range(nr_symbols)]
    random_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = random_numbers + random_symbols + random_letters
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    return password


def pass_gen_btn():
    new_password = generate_password()
    pass_entry.delete(0, 'end')
    pass_entry.insert(0, new_password)

# ---------------------------- ENCRYPTING THE FILE ------------------------------- #


def serializer(action, password):
    filename = 'data.txt'
    tempfile = NamedTemporaryFile('w+t', delete=False)
    crypto = URLSafeSerializer(password)

    with open(filename, mode='r', newline='\n') as csv_file, tempfile:
        reader = csv.reader(csv_file)
        writer = csv.writer(tempfile)

        for row in reader:
            line = str()
            if action == 'encrypt':
                line = [crypto.dumps(row)]
            elif action == 'decrypt':
                try:
                    line = crypto.loads(''.join(row))
                except BadSignature:
                    messagebox.showerror(title='Failed', message='Wrong password!')
                    exit()
            writer.writerow(line)

    shutil.move(tempfile.name, filename)


def change_password(change_type=None):
    global secret_key
    secret_key = str()
    while len(secret_key) <= 0:
        secret_key = askstring('Password', 'New Password: ')

    if change_type == 'init':
        serializer('decrypt', 'pass')

    return secret_key


def initialize():
    global secret_key
    with open('data.txt', mode='r', newline='\n') as csv_file:
        reader = csv.reader(csv_file)
        number_of_rows = sum(1 for _ in reader) - 1  # minus header

        if number_of_rows == 0:
            secret_key = change_password('init')
        else:
            secret_key = askstring('Password', 'Provide password: ')
            if not secret_key or secret_key is None:
                exit()
            serializer('decrypt', secret_key)


def on_closing():
    global secret_key
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        serializer('encrypt', secret_key)
        window.destroy()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = str(web_entry.get())
    login = str(email_entry.get())
    password = str(pass_entry.get())

    if site == "" or login == "" or password == "":
        messagebox.showwarning(title='Ooops...', message="Please make sure you haven't "
                                                         "left any fields empty.")
        return None

    data = pd.read_csv('data.txt', sep=';')

    new_entry = {
        'site': site,
        'login': login,
        'password': password
    }

    # check if site/login already in the database
    if ((data['site'] == site) & (data['login'] == login)).any():
        warning = messagebox.askokcancel(title='Duplicate!', message='Password for this site and login'
                                                                             'already exists. Overwrite?.')
        if warning:
            update_database(data, new_entry)
    else:
        add_to_database(data, new_entry)

    restart_fields()


def add_to_database(data, new_entry):
    data.loc[-1] = new_entry
    data.index = data.index + 1
    data = data.sort_index()
    data.to_csv('data.txt', sep=';', index=None)
    print(data)


def update_database(data, new_entry):
    rows_to_delete = data[(data['site'] == new_entry['site']) & (data['login'] == new_entry['login'])].index
    data.drop(rows_to_delete, inplace=True)
    add_to_database(data, new_entry)


def restart_fields():
    web_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    email_entry.insert(0, 'blueneasy@gmail.com')
    pass_entry.delete(0, 'end')


# ---------------------------- Menu settings ------------------------------- #
def show_info():
    # window settings
    info_window = Toplevel()
    info_window.title('Credits')
    info_window.maxsize(width=400, height=150)
    info_window.config(padx=5, pady=5)
    info_window.resizable(width=False, height=False)

    # label settings
    title_label = Label(info_window, text='Credits:', font=FONT)
    title_label.grid(column=0, row=0)

    # text box settings
    message = 'Created by mpiesiewicz \n' \
              'https://github.com/mpiesiewicz\n' \
              'Credits: Dr. Angela\n'\
              '100 days of code challenge, day 29\n' \
              'https://www.udemy.com/course/100-days-of-code/\n'

    info_text = Text(info_window, height=500, width=500)
    info_text.insert(tkinter.END, message)
    info_text.config(state=tkinter.DISABLED)
    info_text.grid(column=0, row=1)
    info_window.grab_set()


def show_passwords():
    # window settings
    pass_window = Toplevel()
    pass_window.title('Saved passwords')
    pass_window.config(padx=5, pady=5)
    pass_window.resizable(width=False, height=False)

    # scroll text box settings
    pass_text = scrolledtext.ScrolledText(pass_window, font=FONT, undo=True)

    message = pd.read_csv('data.txt', sep=';')
    pass_text.insert(tkinter.END, message)

    pass_text.config(state=tkinter.DISABLED)
    pass_text.grid(column=0, row=0)
    pass_window.grab_set()


# ---------------------------- UI SETUP ------------------------------- #
# general settings
FONT = ('Courier', 10, 'normal')
BACKGROUND = '#d9d9d9'
secret_key = 'pass'

# screen settings
window = Tk()
window.title('Passlock')
# window.minsize(width=300, height=300)
window.config(padx=20, pady=20)
window.resizable(width=False, height=False)

# background settings
canvas = Canvas(width=200, height=200, highlightthickness=False)
background_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=background_img)
canvas.grid(column=1, row=0)

# website
web_label = Label(text='Website:', background=BACKGROUND, font=FONT)
web_label.grid(column=0, row=1)

web_entry = Entry(background=BACKGROUND, font=FONT, width=36)
# web_entry.insert(tkinter.END, '.com')
web_entry.grid(column=1, row=1, columnspan=2, sticky='W')
web_entry.focus()

# email/username
email_label = Label(text='Email/Username:', background=BACKGROUND, font=FONT)
email_label.grid(column=0, row=2)

email_entry = Entry(background=BACKGROUND, font=FONT, width=36)
email_entry.insert(0, 'blueneasy@gmail.com')
email_entry.grid(column=1, row=2, columnspan=2, sticky='W')

# password
pass_label = Label(text='Password:', background=BACKGROUND, font=FONT)
pass_label.grid(column=0, row=3)

pass_entry = Entry(background=BACKGROUND, font=FONT, width=24)
pass_entry.grid(column=1, row=3, columnspan=1, sticky='W')

pass_generate_btn = Button(text='Generate', background=BACKGROUND, font=FONT, width=9, command=pass_gen_btn)
pass_generate_btn.grid(column=2, row=3, sticky='W')

# add
add_btn = Button(text='Add', background=BACKGROUND, font=FONT, width=34, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky='W')

# menu
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Show passwords', command=show_passwords)
filemenu.add_command(label='Change password', command=change_password)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=on_closing)
menubar.add_cascade(label="File", menu=filemenu)

infomenu = Menu(menubar, tearoff=0)
infomenu.add_command(label='Info', command=show_info)
menubar.add_cascade(label='Info', menu=infomenu)

window.config(menu=menubar)

initialize()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
