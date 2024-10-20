import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email_with_attachment(sender_email, receiver_email, subject, body, attachment_path, smtp_server, smtp_port, login, password):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file
    filename = os.path.basename(attachment_path)
    attachment = open(attachment_path, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {filename}")

    msg.attach(part)

    # Set up the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Enable security

    # Log in to the server
    server.login(login, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Quit the server
    server.quit()

    print(f"Email with attachment sent to {receiver_email}")
