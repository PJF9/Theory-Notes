import smtplib
import os
from email.message import EmailMessage
import imghdr

email = os.environ.get("EMAIL_NAME_TEST")
password = os.environ.get("EMAIL_PASSWORD_TEST")

message = EmailMessage()
message["Subject"] = "Email Subject"
message["From"] = email
message["To"] = "jacobfloratos@gmail.com"
message.set_content("Images...")

pics = [
    "C:\\Users\\user\\OneDrive\\Εικόνες\\The Last Of Us\\pic.jpg",
    "C:\\Users\\user\\OneDrive\\Εικόνες\\The Last Of Us\\pic2.jpg",
    "C:\\Users\\user\\OneDrive\\Εικόνες\\The Last Of Us\\pic3.jpg"
]

# If we wanted to send a pdf file
# We have to remove the file_type, then insteed of main_type = "image"
#   we have to write main_type = application and the subtype will be
#   octet-stream

for pic in pics:
    with open(pic, "rb") as file_pic:
        file_data = file_pic.read()
        file_name = file_pic.name
        file_type = imghdr.what(file_name)

    message.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as conn:
    conn.login(email, password)
    conn.send_message(message)
