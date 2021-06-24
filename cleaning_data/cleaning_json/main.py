import json

# Special chars to letters
# classification
def cleanChars(r):
    if isinstance(r, str):
        if "\u0106" in r:
            r = r.replace("\u0106", "C")
        if "\u0107" in r:
            r = r.replace("\u0107", "c")
        if "\u010c" in r:
            r = r.replace("\u010c", "C")
        if "\u010d" in r:
            r = r.replace("\u010d", "c")
        if "\u0160" in r:
            r = r.replace("\u0160", "S")
        if "\u0161" in r:
            r = r.replace("\u0161", "s")
        if "\u017d" in r:
            r = r.replace("\u017d", "Z")
        if "\u017e" in r:
            r = r.replace("\u017e", "z")
        if "\u0189" in r:
            r = r.replace("\u0189", "Dj")
        if "\u0111" in r:
            r = r.replace("\u0111", "dj")
    return r

def cleanPrice(r):
    if '.' in r:
        r = r.replace(".", "")
    if ' ' in r:
        r = r.replace(" ", "")
    if not r.isdigit():
        return None
    return int(r)

def cleanTypeRealEstate(r):
    if r == "stanovi":
        return 0
    else:
        return 1

def cleanOfferType(r):
    if r == "Prodaja" or r == "prodaja":
        return 0
    else:
        return 1

def cleanLocation1(r):
    return cleanChars(r)

def cleanLocation2(r):
    return cleanChars(r)

def cleanSquareFootage(r):
    if r.isdigit():
        r = int(r)
        if r < 0:
            return r * (-1)
        if r > 9000:
            return None
    else:
        if 'ar' in r:
            return int(float(r.split(" ar")[0]) * 100)
        return None

def cleanYearBuilt(r):
    pass


def cleanArea(r):
    if isinstance(r, str):
        if '-' in r:
            return None
        if 'a plac' in r:
            return int(float(r.split("a plac")[0]) * 100)
        if ' ar' in r:
            return int(float(r.split(" ar")[0]) * 100)
        if ' m' in r:
            return int(round(float(r.split(" m")[0])))
    return None


def cleanFloor(r):
    pass


def cleanBooked(r):
    r = cleanChars(r)
    if r == "Da" or r == "uknjizeno":
        return 1
    else:
        return 0


def cleanHeating(r):
    pass


def cleanRoom(r):
    if r:
        if "-" in r:
            return None
        if " soba" in r:
            r = int(round(float(r.split(" soba")[0])))
        elif " sobe" in r:
            r = int(round(float(r.split(" sobe")[0])))
        if float(r) > 24:
            return 0
        else:
            return int(round(float(r)))
    return None

def cleanBathrooms(r):
    if r:
        if float(r) > 30:
            return 0
        else:
            return int(round(float(r)))
    return None


def cleanParking(r):
    if r:
        if r == "Ne":
            return 0
        else:
            return 1
    return None


def cleanElevator(r):
    if r:
        return 1
    else:
        return 0


def cleanTerrace(r):
    if r:
        if "Da" in r or "terasa|lodja" in r:
            return 1
    return 0


def cleanJSON(file):
    with open(file, 'r') as infile:
        result = json.load(infile)
        for r in result:
            r["Cena"] = cleanPrice(r["Cena"])
            r["Tip nekretnine"] = cleanTypeRealEstate(r["Tip nekretnine"])
            r["Tip ponude"] = cleanOfferType(r["Tip ponude"])
            r["Lokacija1"] = cleanLocation1(r["Lokacija1"])
            r["Lokacija2"] = cleanLocation2(r["Lokacija2"])
            r["Kvadratura"] = cleanSquareFootage(r["Kvadratura"])
            r["Godina izgradnje"] = cleanYearBuilt(r["Godina izgradnje"])
            r["Povrsina zemljista"] = cleanArea(r["Povrsina zemljista"])
            r["Spratnost"] = cleanFloor(r["Spratnost"])
            r["Uknji\u017eenost"] = cleanBooked(r["Uknji\u017eenost"])
            r["Tip grejanja"] = cleanHeating(r["Tip grejanja"])
            r["Broj soba"] = cleanRoom(r["Broj soba"])
            r["Broj kupatila"] = cleanBathrooms(r["Broj kupatila"])
            r["Parking"] = cleanParking(r["Parking"])
            r["Lift"] = cleanElevator(r["Lift"])
            r["Terasa"] = cleanTerrace(r["Terasa"])

    with open('cleaned.json', 'w') as output_file:
        output_file.write(
        '[' +
        ',\n'.join(json.dumps(i) for i in result) +
        ']\n')
cleanJSON("houses.json")