from itsdangerous import URLSafeSerializer
import csv
from tempfile import NamedTemporaryFile
import shutil


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
            decrypted_row = encrypt.loads(''.join(row))
            writer.writerow(decrypted_row)
    shutil.move(tempfile.name, filename)


secret_key = 'pass'
# encrypt_the_file()
decrypt_the_file()

