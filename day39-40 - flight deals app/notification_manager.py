import smtplib


class NotificationManager:
    def __init__(self, sender_smtp, sender_port, sender_address, password):
        self.sender_address = sender_address
        self.password = password
        self.sender_port = sender_port
        self.sender_smtp = sender_smtp

    def notify(self, recipients, content):
        if len(content) > 0:
            subject = "mp_dealfinder: new hot offers in your area"
            body = self.create_message(content)
            for recipient in recipients:
                self.send_email(recipient, subject, body)

    def create_message(self, content: list):
        head = "TODAY'S HOT DEALS\n"
        mid = str()
        for deal in content:
            mid += f"{deal['destination']}: {deal['todaysLowest']}EUR | LSF: {deal['lowestSoFar']}EUR | Link: {deal['link']}\n"
        footer = f"{'_' * 25}\n" f"automated by mp_dealfinder!\n" f""
        return head + mid + footer

    def send_email(self, recipient, subject, body):
        with smtplib.SMTP(self.sender_smtp, self.sender_port) as connection:
            connection.starttls()
            connection.login(user=self.sender_address, password=self.password)

            header = f"To:{recipient}\n" f"From:{self.sender_address}\n" f"Subject:{subject}\n"

            full_message = header + body
            connection.sendmail(from_addr=self.sender_address, to_addrs=recipient, msg=full_message)
