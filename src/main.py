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
CK: {offer.get('agency', '-')}

Cena za osobu:
{offer.get('price', '-')} Kč

Cena celkem:
{offer.get('total_price', '-')} Kč

Odkaz:
{offer.get('url', '-')}

--------------------------------------------------
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

email_body.append("=" * 60)
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

email_body.append("")
email_body.append("=" *
