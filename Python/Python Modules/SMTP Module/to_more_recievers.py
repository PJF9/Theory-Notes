import smtplib
import os
from email.message import EmailMessage

email = os.environ.get("EMAIL_NAME_TEST")
password = os.environ.get("EMAIL_PASSWORD_TEST")

# Make a contacts list
contacts = [
    "petros_floratos@gmail.com",
    "jacobfloratos@gmail.com"
]

message = EmailMessage()
message["Subject"] = "Email Subject"
message["From"] = email
# Adding more contacts
# The python documentation tell us to use this method
# But we can also replace that with contacts
message["To"] = ", ".join(contacts)
message.set_content("Email Body")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as conn:
    conn.login(email, password)
    conn.send_message(message)
