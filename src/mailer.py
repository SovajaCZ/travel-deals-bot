import os
import smtplib
from email.message import EmailMessage


def send_email(subject, body, recipient):
    """
    Odeslání e-mailu přes SMTP Seznam.cz
    """

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = os.environ["SMTP_USER"]
    msg["To"] = recipient

    msg.set_content(body)

    try:
        print(f"Recipient: {recipient}")
        print(f"Subject: {subject}")
        print(f"Body length: {len(body)} znaků")
        print(f"Email size: {len(msg.as_string())} bajtů")

        with smtplib.SMTP_SSL("smtp.seznam.cz", 465) as server:
            server.login(
                os.environ["SMTP_USER"],
                os.environ["SMTP_PASSWORD"]
            )

            server.send_message(msg)

        print("E-mail byl úspěšně odeslán.")

    except smtplib.SMTPException as e:
        print(f"SMTP chyba: {e}")
        raise

    except Exception as e:
        print(f"Neočekávaná chyba: {e}")
        raise
