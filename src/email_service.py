"""
email_service.py

This module handles sending emails with attachments, such as the daily Twitter digest in PDF format.
It uses SMTP to send the email with the file attachment.
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email_with_attachment(to_address, subject, body, attachment_filename):
    """
    Sends an email with an attachment.

    Args:
        to_address (str): Recipient email address.
        subject (str): The subject of the email.
        body (str): The body content of the email.
        attachment_filename (str): The path to the file to be attached.

    Returns:
        None
    """
    from_address = os.getenv('EMAIL_USER')  # Your email address
    password = os.getenv('EMAIL_PASS')  # Your email password (or an app password)

    # Create email message
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body, 'plain'))

    # Open the file to be sent
    with open(attachment_filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(attachment_filename)}')

    # Attach the file to the email
    msg.attach(part)

    # Connect to the server and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        print(f"Email sent to {to_address} successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
