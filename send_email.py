import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    # Add sender's email address
    username = ""

    # Add app password for email address
    password = os.getenv("")

    # Add receiver's email address
    receiver = ""
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
