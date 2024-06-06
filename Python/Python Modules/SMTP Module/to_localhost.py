import smtplib
import os

email = os.environ.get("EMAIL_NAME_TEST")
password = os.environ.get("EMAIL_PASSWORD_TEST")

# With this method we can test email if we dont want to send to ourselfes
# To active the local debug server we need to open the cmd and type:
# python -m smtpd -c DebuggingServer -n localhost:1025
with smtplib.SMTP("localhost", 1025) as conn:
    subject = "Email Subject"
    body = "Email Body"
    message = f"Subject: {subject}\n\n{body}"

    # We have to type the next line but the mail doesn't be send to the email
    conn.sendmail(email, "jacobfloratos@gmail.com", message)
