# day 29:
## _Passlock - password manager_

Part 29 of the 100 days of code Bootcamp:  
https://www.udemy.com/course/100-days-of-code/

The aim of the project:
- Create a password manager
- Learn how to use tkinter in more advanced projects
- Make it waaaaay better than what was shown in the tutorial

## Features

- Password manager with a nice and simple GUI
- Built in strong password generator
- Generated password is copied to clipboard, ready to paste whenever you want

Why is it better than the original one?
- Stores passwords in a signed form, using "itsdangerous" sign method
- Added quality - cannot store two passwords with the same login and site
- Explore all the stored passwords in a nice format (pandas)
- Set up an init password 
- Lets you change the password later on 
- Contains a nice menu bar and info section
- Always encrypts the passwords on exit

Passwords are stored in data.txt file, in a much safer format than just a plain text.
Passwords are not encrypted, the format is pseudo encrypted, still better than plain text.

Whenever somebody changes the stored form, the program will fail.

## How to run

 - Run main.py file

## Library

Written in pure python 3.8.10
- tkinter
- itsdangerous
- pandas
- pyperclip
- csv
- tempfile
- shutil