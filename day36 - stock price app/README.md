# day 36:
## _Stock price notification app_

Part 36 of the 100 days of code Bootcamp:
https://www.udemy.com/course/100-days-of-code/

The aim of the project:
- Create an application that will send a stock price notification

## Features

- Runs on pythonanywhere.com
- Scheduled at 7AM everyday
- Checks the stock price of a chosen entity (example - TSLA) for yesterday's closing, and a day before
- Calculates the % difference
- If the difference is greater or equal 4, will send 3 SMS messages, with most popular headlines and news description.
- Used APIs:
- Stock price: alphavantage.co
- News: newsapi.org
- SMS: twilio.com

## How to run

 - Run main.py file
 - Variables are needed to use the APIs. The full list of needed variables is located at the top of the 
main.py file. My variables were hidden in a credentials.py file which is not attached for obvious reasons.
## Library

- python 3.8.10
- requests
- twilio