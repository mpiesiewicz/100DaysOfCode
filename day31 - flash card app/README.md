# day 31:
## __

Part 31 of the 100 days of code Bootcamp:  
https://www.udemy.com/course/100-days-of-code/

The aim of the project:
- Create Flashy - a language learning app 
Helps to learn new words. Draw a card. If the word on the card is known, press ✔
to add it to known words and remove from the deck. If not, 
see the english side and add the word back to the deck.


## Features

- Nice and simple GUI
- Saves the progress in data/words_to_learn csv file
- Contains the most used words in the selected language, 
based on opensubtitles.org database (credits: https://github.com/hermitdave/FrequencyWords/tree/master/content/2018)

Why is it better than the original one?
- 2 Languages support instead of one - French and Spanish
- 8000 words to learn per language 
- Reset words or choose how many to fetch using reset button
- Built in menu bar with options to change language, reset or quit the app
- The popularity rank of the word is shown on the bottom right corner of the card.

## How to run

 - Run main.py file

## Library

- python 3.8.10
- tkinter
- pandas
- PIL
