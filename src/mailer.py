import os
import smtplib
from email.message import EmailMessage


def send_email(subject, body, recipient):

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = os.environ["SMTP_USER"]
    msg["To"] = recipient

    msg.set_content(body)

    with smtplib.SMTP_SSL(
        "smtp.seznam.cz",
        465,
        timeout=60
    ) as server:

        server.set_debuglevel(1)

        server.login(
            os.environ["SMTP_USER"],
            os.environ["SMTP_PASSWORD"]
        )

        server.sendmail(
            os.environ["SMTP_USER"],
            [recipient],
            msg.as_string()
        )

    print("Email odeslán.")
