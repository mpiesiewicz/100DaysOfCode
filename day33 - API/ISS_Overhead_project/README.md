# day 33:
## __

Part 33 of the 100 days of code Bootcamp:  
https://www.udemy.com/course/100-days-of-code/

The aim of the project:
- Play around smtplib, learn how to send emails
- Learn how to use APIs and combine the pulled data
- Create a small script "ISS Overhead" which will send email whenever the International Space Station is visible.


## Features
* checks APIs:
* sunrise-sunset.org - to check if it's dark under the current location
* ISS - to check if the ISS is overhead (approx -+ 5 long/lat)


## How to run

 - Run main.py file

Note: Requires credentials.py script with Login, Password, Port and smtp server variables, whcich is not published for
security reasons.

## Library

- python 3.8.10
- smtplib
- requests
