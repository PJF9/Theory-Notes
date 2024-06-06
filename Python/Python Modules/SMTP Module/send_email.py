import smtplib
import os
# We can also import a class to help us to prevent put the message inside
#   f string
# We can also declaire the message outside the contex manager
from email.message import EmailMessage

email = os.environ.get("EMAIL_NAME_TEST")
password = os.environ.get("EMAIL_PASSWORD_TEST")

# Creating the message
message = EmailMessage()
# Subject of the mail
message["Subject"] = "Email Subject"
# Sender of the mail
message["From"] = email
# Reciever of the mail
message["To"] = "jacobfloratos@gmail.com"
# The body of the mail
message.set_content("Email body")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as conn:
    conn.login(email, password)
    # We dont need the send mail, insteed we need the send_message method
    conn.send_message(message)
