import tkinter
import tkinter.messagebox
from tkinter.simpledialog import askstring
from random import choice, randint, shuffle
import pandas as pd
import pyperclip
from itsdangerous import URLSafeSerializer
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

    random_letters = [choice(letters) for letter in range(nr_letters)]
    random_symbols = [choice(symbols) for symbol in range(nr_symbols)]
    random_numbers = [choice(numbers) for number in range(nr_numbers)]

    password_list = random_numbers + random_symbols + random_letters
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    return password


def pass_gen_btn():
    new_password = generate_password()
    pass_entry.delete(0, 'end')
    pass_entry.insert(0, new_password)


def encrypt_the_file():
    filename = 'data.txt'
    tempfile = NamedTemporaryFile('w+t', delete=False)
    encrypt = URLSafeSerializer(secret_key)

    with open(filename, mode='r', newline='\n') as csv_file, tempfile:
        reader = csv.reader(csv_file)
        writer = csv.writer(tempfile)

        for row in reader:
            line = [encrypt.dumps(row)]
            writer.writerow(line)

    shutil.move(tempfile.name, filename)


def decrypt_the_file():
    filename = 'data.txt'
    tempfile = NamedTemporaryFile('w+t', delete=False)
    encrypt = URLSafeSerializer(secret_key)

    with open(filename, 'r', newline='\n') as csv_file, tempfile:
        reader = csv.reader(csv_file, quotechar='"')
        writer = csv.writer(tempfile, quotechar='"')

        for row in reader:
            try:
                decrypted_row = encrypt.loads(''.join(row))
                writer.writerow(decrypted_row)
            except:
                print('zle haslo')
                exit_warning = tkinter.messagebox.showerror(title='Failed', message='Wrong password!')
                exit()

    shutil.move(tempfile.name, filename)


def on_closing():
    if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        encrypt_the_file()
        window.destroy()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = str(web_entry.get())
    login = str(email_entry.get())
    password = str(pass_entry.get())

    if site == "" or login == "" or password == "":
        empty_field_warning = tkinter.messagebox.showwarning(title='Ooops...', message="Please make sure you haven't "
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
        warning = tkinter.messagebox.askokcancel(title='Duplicate!', message='Password for this site and login'
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


# ---------------------------- UI SETUP ------------------------------- #
# general settings
FONT = ('Courier', 10, 'normal')
BACKGROUND = '#d9d9d9'

# screen settings
window = tkinter.Tk()
window.title('Passlock')
# window.minsize(width=300, height=300)
window.config(padx=20, pady=20)
window.resizable(width=False, height=False)

# background settings
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=False)
background_img = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=background_img)
canvas.grid(column=1, row=0)

# website
web_label = tkinter.Label(text='Website:', background=BACKGROUND, font=FONT)
web_label.grid(column=0, row=1)

web_entry = tkinter.Entry(background=BACKGROUND, font=FONT, width=36)
# web_entry.insert(tkinter.END, '.com')
web_entry.grid(column=1, row=1, columnspan=2, sticky='W')
web_entry.focus()

# email/username
email_label = tkinter.Label(text='Email/Username:', background=BACKGROUND, font=FONT)
email_label.grid(column=0, row=2)

email_entry = tkinter.Entry(background=BACKGROUND, font=FONT, width=36)
email_entry.insert(0, 'blueneasy@gmail.com')
email_entry.grid(column=1, row=2, columnspan=2, sticky='W')

# password
pass_label = tkinter.Label(text='Password:', background=BACKGROUND, font=FONT)
pass_label.grid(column=0, row=3)

pass_entry = tkinter.Entry(background=BACKGROUND, font=FONT, width=24)
pass_entry.grid(column=1, row=3, columnspan=1, sticky='W')

pass_generate_btn = tkinter.Button(text='Generate', background=BACKGROUND, font=FONT, width=9, command=pass_gen_btn)
pass_generate_btn.grid(column=2, row=3, sticky='W')

# add
add_btn = tkinter.Button(text='Add', background=BACKGROUND, font=FONT, width=34, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky='W')

secret_key = askstring('Password', 'Provide password: ')
if not secret_key or secret_key is None:
    exit()
decrypt_the_file()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
