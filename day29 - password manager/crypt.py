import csv
import shutil
import tkinter.messagebox
from tempfile import NamedTemporaryFile
from itsdangerous import URLSafeSerializer, BadSignature

secret_key = 'pass'


# use to fix encrypted file on program quit
def serializer(type):
    filename = 'data.txt'
    tempfile = NamedTemporaryFile('w+t', delete=False)
    crypto = URLSafeSerializer(secret_key)

    with open(filename, mode='r', newline='\n') as csv_file, tempfile:
        reader = csv.reader(csv_file)
        writer = csv.writer(tempfile)

        for row in reader:
            line = str()
            if type == 'encrypt':
                line = [crypto.dumps(row)]
            elif type == 'decrypt':
                try:
                    line = crypto.loads(''.join(row))
                except BadSignature:
                    tkinter.messagebox.showerror(title='Failed', message='Wrong password!')
                    exit()
            writer.writerow(line)

    shutil.move(tempfile.name, filename)


# serializer('encrypt')
# serializer('decrypt')
