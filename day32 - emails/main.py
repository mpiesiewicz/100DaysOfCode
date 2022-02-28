import smtplib

# smtp.mail.yahoo.com for yahoo
connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=)