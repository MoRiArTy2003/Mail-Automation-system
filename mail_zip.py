import os
import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from zipfile import ZipFile, ZIP_DEFLATED
import shutil

# Function to generate a random password
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to create a password-protected zip file
def create_password_protected_zip(file_path, zip_path, password):
    shutil.make_archive(zip_path, 'zip', os.path.dirname(file_path), os.path.basename(file_path))
    shutil.move(f"{zip_path}.zip", zip_path)
    with ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(os.path.dirname(zip_path), pwd=bytes(password, 'utf-8'))

# Function to send email
def send_email(sender_email, receiver_email, subject, body, attachment_path=None, smtp_server='smtp.gmail.com', smtp_port=587, login=None, password=None):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    if attachment_path:
        attachment = open(attachment_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(attachment_path))
        msg.attach(part)
        attachment.close()

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

# Main function
def main():
    sender_email = "Moriarty2003.A.3043@gmail.com"
    receiver_email = "capyslaypullup2120@gmail.com"
    email_password = "CSGOisscience3043"

    # Generate a random password
    password = generate_password()

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
