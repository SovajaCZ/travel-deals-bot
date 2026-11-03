import os, smtplib
from email.mime.text import MIMEText

def send_email(subject, body, recipient):
    msg=MIMEText(body,"plain","utf-8")
    msg["Subject"]=subject
    msg["From"]=os.environ["SMTP_USER"]
    msg["To"]=recipient
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as s:
        s.login(os.environ["SMTP_USER"],os.environ["SMTP_PASSWORD"])
        s.send_message(msg)
