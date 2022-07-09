import smtplib
import ssl
from email.message import EmailMessage

subject = input("Enter Your Subject: ")
body = input("Enter Your Body of the Mail ")
sender_email = input("Enter Your email address ")
receiver_email = input("Enter Receiver email adress ")
password = input("Enter Your email adress password ")
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
context = ssl.create_default_context()
print("Sending Email!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print("Success")
