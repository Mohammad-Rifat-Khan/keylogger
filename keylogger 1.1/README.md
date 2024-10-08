# Keystroke Logger with Email Sending Feature
This Python script captures keystrokes using pynput and sends the logged data via email when the ESC key is pressed. The logged keystrokes are saved in info.txt, which is attached to the email.

## Features
Keystroke Logging: Captures and logs every keypress in real time.    
Email Functionality: Sends the logged keystrokes via email once the ESC key is pressed.    
Attachment: Sends the log as a .txt file attachment.  
Prerequisites
Python 3.x installed on your machine.  
Basic understanding of Python.  
## Required Libraries:
### Install the pynput library:
pip install pynput  
The smtplib library is included with Python by default.
## Step 1: 
Clone the Repository
## Step 2: 
Configure Email Settings
### You will need a Gmail account to send the emails. Before running the script:
Enable 2-Step Verification on your Gmail account.   
Generate an App Password:   
Go to Google's App Passwords.   
Generate a password for this script (choose Mail as the app and Windows Computer as the device).   
Update the script with your Gmail credentials:   
Replace EMAIL_ADDRESS with your Gmail account.   
Replace EMAIL_PASSWORD with the app-specific password you just generated.   
Replace TO_EMAIL with the email address you want the log sent to.   
## Run the script:
python keylogger1.1.py    
The script will start logging all keystrokes into info.txt.
Press the "ESC" key to stop logging and send the email with the attached log file. 
