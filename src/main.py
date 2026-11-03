import json
from providers import get_offers
from filters import filter_offers
from mailer import send_email
with open("config/settings.json",encoding="utf-8") as f: settings=json.load(f)
filtered=filter_offers(get_offers(),settings)
body="\n".join([f"{o['hotel']} - {o['price']} Kč/os." for o in filtered])
send_email(f"Nalezeno {len(filtered)} nabídek",body,settings["email"]["recipient"])
