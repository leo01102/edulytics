# email_module.py

import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# load environment variables from a .env file
load_dotenv()

def send_email(to_email, subject, body):
    """Sends an email using SMTP credentials from environment variables."""
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    smtp_user = os.getenv("SMTP_SRU_USER")
    smtp_password = os.getenv("SMTP_SRU_APPPASSWORD") # uses a Google App Password

    # create the email message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = smtp_user
    msg['To'] = to_email

    try:
        # establish a secure connection with the SMTP server
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, to_email, msg.as_string())
        print(f"Email successfully sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")