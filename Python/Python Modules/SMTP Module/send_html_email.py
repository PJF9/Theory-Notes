import smtplib
import os
from email.message import EmailMessage

email = os.environ.get("EMAIL_NAME_TEST")
password = os.environ.get("EMAIL_PASSWORD_TEST")

message = EmailMessage()
message["Subject"] = "Email Subject"
message["From"] = email
message["To"] = "jacobfloratos@gmail.com"
# Set a message if the html failed
message.set_content("Email Body")

# Add the html previlage to the email
message.add_alternative('''
<!DOCTYPE HTML>
<html>
    <body>
        <h1> Email Body </h1>
    </body>
</html>
''', subtype="html")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as conn:
    conn.login(email, password)
    conn.send_message(message)
