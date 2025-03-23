# Mail Automation System

This project offers a collection of Python scripts designed to automate email sending tasks. It streamlines processes such as sending emails with attachments, compressing files, and modifying files before sending.

## Features

- **Automated Email Sending**: Leverages Python’s `smtplib` for sending emails automatically.
- **File Compression**: Compress files into ZIP format before sending.
- **Attachment Handling**: Easily attach files to emails.
- **File Modification**: Modify or reformat files prior to compression and sending.

## Repository Contents

- **demomail.py**: The main script for sending emails with attachments.
- **mail_zip.py**: A script to compress files into a ZIP archive and send them via email.
- **pyzip_change.py**: A script to modify files before compressing and sending.

## Prerequisites

- Python 3.x installed on your system.
- An email account (e.g., Gmail) with valid credentials.
- Required Python libraries (e.g., `smtplib`, `zipfile`). If additional packages are needed, consider including them in a `requirements.txt`.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/MoRiArTy2003/Mail-Automation-system.git

Usage
Configure Email Settings:

Open demomail.py (or the appropriate script) and update the following placeholders with your email credentials and recipient details:

sender_email = "your_email@example.com"
receiver_email = "recipient@example.com"
password = "your_password"

Specify the File(s) to Send:
Update the script with the file(s) you wish to attach or compress before sending.

Run the Script:
Execute the script from the command line. For example, to run the main script:

python demomail.py
You can also run mail_zip.py or pyzip_change.py depending on your specific requirements.

Contributing
Contributions are welcome! If you would like to contribute:

Fork the repository.

Create a feature branch.

Commit your changes.

Open a pull request with a clear description of your modifications.

License
This project is open source and available under the MIT License.
