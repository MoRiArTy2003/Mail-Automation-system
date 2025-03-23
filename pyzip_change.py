import os
import random
import string
import smtplib
import pyzipper
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# Function to generate a random password
def generate_password(length=8):
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to create a password-protected zip file using pyzipper
def create_password_protected_zip(file_path, zip_path, password):
    with pyzipper.AESZipFile(zip_path, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(password.encode())
        zf.write(file_path, os.path.basename(file_path))

# Function to send email
def send_email(sender_email, receiver_email, subject, body, attachment_path=None, smtp_server='smtp.gmail.com', smtp_port=587, login=None, password=None):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
            msg.attach(part)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Main function
def main():
    sender_email = "your_email@example.com"
    receiver_email = "receiver_email@example.com"
    email_password = "your_email_password" # Create App Password from Sender's Email

    # Generate a random password
    password = generate_password(12)  # Generating a 12-character long password

    # Create a dummy file to zip
    file_path = "dummy_file.txt"
    with open(file_path, "w") as f:
        f.write("This is a test file.")

    # Create a password-protected zip file
    zip_path = "protected.zip"
    create_password_protected_zip(file_path, zip_path, password)

    # Send email with the zip file
    subject = "Here is your password-protected file"
    body = "Please find the attached password-protected zip file."
    send_email(sender_email, receiver_email, subject, body, attachment_path=zip_path, login=sender_email, password=email_password)

    # Send email with the password
    password_subject = "Your password for the zip file"
    password_body = f"Here is the password for the zip file: {password}"
    send_email(sender_email, receiver_email, password_subject, password_body, login=sender_email, password=email_password)

    # Clean up
    os.remove(file_path)
    os.remove(zip_path)

if __name__ == "__main__":
    main()
