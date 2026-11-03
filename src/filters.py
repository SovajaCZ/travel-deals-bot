def filter_offers(offers, settings):
    result=[]
    for offer in offers:
        if offer["price"]>settings["max_price_per_person"]: continue
        if offer["stars"]<settings["min_stars"]: continue
        if settings["meal"].lower() not in offer["meal"].lower(): continue
        result.append(offer)
    return sorted(result,key=lambda x:x["price"])
