# day 35:
## _Rain Warning Application_

Part 35 of the 100 days of code Bootcamp:
https://www.udemy.com/course/100-days-of-code/

The aim of the project:
- Create an application that will send an SMS with a rain warning

## Features

- Runs on pythonanywhere.com
- Scheduled at 7AM everyday
- Will check the weather for the next 12 hours using API api.openweathermap.org
- If it rains, will send an SMS with the warning and information about the raining hours.

## How to run

 - Run main.py file
 - Variables are needed to use the APIs. The full list of needed variables is located at the top of the 
main.py file. My variables were hidden in a credentials.py file which is not attached for obvious reasons.
## Library

- python 3.8.10
- requests
- twilio