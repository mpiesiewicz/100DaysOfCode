from tkinter import Tk, Menu, messagebox, PhotoImage, Canvas, Label, Entry, Button, Toplevel, Text, scrolledtext, END, \
    DISABLED
from tkinter.simpledialog import askstring
from random import choice, randint, shuffle
import pandas as pd
import pyperclip
from itsdangerous import URLSafeSerializer, BadSignature
import json


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


def search_btn():
    site = str(web_entry.get())
    with open('data.json', 'r') as data_file:
        data = json.load(data_file)
        try:
            finding = data[site]
        except KeyError:
            email_entry.delete(0, 'end')
            email_entry.insert(0, 'not found')
            pass_entry.delete(0, 'end')
            pass_entry.insert(0, 'not found')
        else:
            message = f"login: {finding['login']} \n" \
                      f"pass: {finding['password']}"
            messagebox.showinfo(title=site, message=message)

            email_entry.delete(0, 'end')
            email_entry.insert(0, finding['login'])
            pass_entry.delete(0, 'end')
            pass_entry.insert(0, finding['password'])


# ---------------------------- ENCRYPTING THE FILE ------------------------------- #
def encrypt():
    crypto = URLSafeSerializer(secret_key)

    with open('data.json', 'r') as data_file:
        reader = json.load(data_file)

        encrypted_text = crypto.dumps(reader)
    with open('data.json', 'w') as data_file:
        data_file.write(encrypted_text)


def decrypt():
    crypto = URLSafeSerializer(secret_key)

    with open('data.json', 'r') as data_file:
        reader = data_file.read()
    try:
        decrypted_text = crypto.loads(reader)
    except BadSignature:
        messagebox.showerror(title='Failed', message='Wrong password!')
        exit()
    else:
        with open('data.json', 'w') as data_file:
            json.dump(decrypted_text, data_file, indent=4)


def change_password(change_type=None):
    global secret_key
    secret_key = str()
    while len(secret_key) <= 0:
        secret_key = askstring('Password', 'New Password: ')
    return secret_key


def initialize():
    global secret_key

    try:
        with open('data.json', 'r') as data_file:
            if len(data_file.readlines()) == 0:
                raise FileNotFoundError

    except FileNotFoundError:
        # json file does not exist, do not attempt to decrypt
        answer = messagebox.askyesno('Set up password?', 'Do you want to change the default password?')
        if answer:
            change_password()
    else:
        secret_key = askstring('Password', 'Provide password: ')
        if not secret_key or secret_key is None:
            exit()
        else:
            decrypt()


def on_closing():
    global secret_key
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        encrypt()
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
    else:

        new_entry = {
            site: {
                'login': login,
                'password': password
            }
        }
        add_to_database(new_entry)
        restart_fields()


def add_to_database(new_entry):
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, ValueError) as error:
        with open('data.json', 'w') as data_file:
            json.dump(new_entry, data_file, indent=4)
    else:
        data.update(new_entry)
        with open('data.json', 'w') as data_file:
            json.dump(data, data_file, indent=4)


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
              'Credits: Dr. Angela\n' \
              '100 days of code challenge, day 29\n' \
              'https://www.udemy.com/course/100-days-of-code/\n'

    info_text = Text(info_window, height=500, width=500)
    info_text.insert(END, message)
    info_text.config(state=DISABLED)
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

    data = pd.read_json('data.json')
    data = data.T

    message = data.to_string()

    pass_text.insert(END, message)

    pass_text.config(state=DISABLED)
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

web_entry = Entry(background=BACKGROUND, font=FONT, width=24)
# web_entry.insert(tkinter.END, '.com')
web_entry.grid(column=1, row=1, columnspan=1, sticky='W')
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

# search
search_btn = Button(text='Search', background=BACKGROUND, font=FONT, width=9, command=search_btn)
search_btn.grid(column=2, row=1, sticky='W')

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
