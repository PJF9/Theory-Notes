import smtplib
import os
from email.message import EmailMessage
# We also need a module to declare the pic type
import imghdr

email = os.environ.get("EMAIL_NAME_TEST")
password = os.environ.get("EMAIL_PASSWORD_TEST")

# We need to open the pic files
# rb is read bytes mode
with open("C:\\Users\\user\\OneDrive\\Εικόνες\\The Last Of Us\\pic.jpg", "rb") as file_pic:
    # Get the data from the file
    file_data = file_pic.read()
    # Get the file name
    file_name = file_pic.name
    # Get the pic type
    file_type = imghdr.what(file_name)


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as conn:
    conn.login(email, password)

    message = EmailMessage()
    message["Subject"] = "Email Subject"
    message["From"] = email
    message["To"] = "jacobfloratos@gmail.com"

    # Add the image to the message
    # First is the data od the file then the main type following by the
    #   .whateverand finally the file name
    message.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

    conn.send_message(message)
