print("XXXXXXXX NOVA VERZE MAIN.PY XXXXXXXX")

import json

from providers import get_offers
from filters import filter_offers
from mailer import send_email


def format_offer(offer):
    return f"""
Destinace: {offer.get('destination', '-')}

Hotel: {offer.get('hotel', '-')}

Kategorie: {offer.get('stars', '-')}*

Hodnocení: {offer.get('rating', '-')}/10

Strava: {offer.get('meal', '-')}

Počet nocí: {offer.get('nights', '-')}

Odletové letiště: {offer.get('airport', '-')}

Termín odletu: {offer.get('departure', '-')}

Cestovní kancelář: {offer.get('agency', '-')}

Cena za osobu:
{offer.get('price', '-')} Kč

Cena celkem:
{offer.get('total_price', '-')} Kč

Odkaz na zájezd:
{offer.get('url', '-')}

------------------------------------------------------------
"""


with open("config/settings.json", encoding="utf-8") as f:
    settings = json.load(f)

offers = get_offers()

filtered = filter_offers(
    offers,
    settings
)

email_body = []

email_body.append("PŘEHLED LAST MINUTE NABÍDEK")
email_body.append("=" * 60)
email_body.append("")

# VARIANTA A

email_body.append("VARIANTA A")
email_body.append("2 DOSPĚLÍ + 1 DÍTĚ (15 LET)")
email_body.append("=" * 60)
email_body.append("")

variant_a = [
    offer for offer in filtered
    if offer.get("search_variant") == "A"
]

if variant_a:
    for offer in variant_a:
        email_body.append(format_offer(offer))
else:
    email_body.append("Nebyla nalezena žádná nabídka.")
    email_body.append("")

# VARIANTA B

email_body.append("")
email_body.append("VARIANTA B")
email_body.append("3 DOSPĚLÍ + 1 DÍTĚ (15 LET)")
email_body.append("=" * 60)
email_body.append("")

variant_b = [
    offer for offer in filtered
    if offer.get("search_variant") == "B"
]

if variant_b:
    for offer in variant_b:
        email_body.append(format_offer(offer))
else:
    email_body.append("Nebyla nalezena žádná nabídka.")
    email_body.append("")

# NOVÉ NABÍDKY

email_body.append("")
email_body.append("NOVÉ NABÍDKY")
email_body.append("=" * 60)
email_body.append("")
email_body.append("Historie cen zatím není aktivní.")
email_body.append("")

# TOP SLEVA

email_body.append("")
email_body.append("TOP SLEVA DNE")
email_body.append("=" * 60)
email_body.append("")
email_body.append("Sledování zlevnění zatím není aktivní.")
email_body.append("")

# CENA/VÝKON

email_body.append("")
email_body.append("NEJLEPŠÍ POMĚR CENA / VÝKON")
email_body.append("=" * 60)
email_body.append("")
email_body.append("Skórování hotelů zatím není aktivní.")
email_body.append("")

send_email(
    subject="Denní přehled last minute dovolených",
    body="\n".join(email_body),
    recipient="jan.sabl@seznam.cz"
)
