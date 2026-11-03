import os
import smtplib
from email.mime.text import MIMEText


def send_email(subject, body, recipient):
    """
    Odeslání e-mailu přes SMTP Seznam.cz
    """

    msg = MIMEText(body, "plain", "utf-8")

    msg["Subject"] = subject
    msg["From"] = os.environ["SMTP_USER"]
    msg["To"] = recipient

    with smtplib.SMTP_SSL("smtp.seznam.cz", 465) as server:
        server.login(
            os.environ["SMTP_USER"],
            os.environ["SMTP_PASSWORD"]
        )

        server.send_message(msg)

    print("E-mail byl úspěšně odeslán.")
