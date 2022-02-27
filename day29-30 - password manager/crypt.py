import csv
import json
import shutil
import tkinter.messagebox
from tempfile import NamedTemporaryFile
from itsdangerous import URLSafeSerializer, BadSignature

secret_key = 'pass'


# use to fix encrypted file on program quit
# def serializer(type):
#     filename = 'data.json'
#     tempfile = NamedTemporaryFile('w+t', delete=False)
#     crypto = URLSafeSerializer(secret_key)
#
#     with open(filename, mode='r', newline='\n') as csv_file, tempfile:
#         reader = csv.reader(csv_file)
#         writer = csv.writer(tempfile)
#
#         for row in reader:
#             line = str()
#             if type == 'encrypt':
#                 line = [crypto.dumps(row)]
#             elif type == 'decrypt':
#                 try:
#                     line = crypto.loads(''.join(row))
#                 except BadSignature:
#                     tkinter.messagebox.showerror(title='Failed', message='Wrong password!')
#                     exit()
#             writer.writerow(line)
#
#     shutil.move(tempfile.name, filename)


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
        tkinter.messagebox.showerror(title='Failed', message='Wrong password!')
        exit()
    else:
        with open('data.json', 'w') as data_file:
            json.dump(decrypted_text, data_file, indent=4)


encrypt()
# decrypt()
