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
        if "\u0110" in r:
            r = r.replace("\u0110", "Dj")
        if "\u0111" in r:
            r = r.replace("\u0111", "dj")
        if "\u00d0" in r:
            r = r.replace("\u00d0", "Dj")
        if "\u2013" in r:
            r = r.replace("\u2013", "")
        if "\u0430" in r:
            r = r.replace("\u0430", "a")
        if "\u00e1" in r:
            r = r.replace("\u00e1", "a")
    return r

def cleanPrice(r):
    if '.' in r:
        r = r.replace(".", "")
    if ' ' in r:
        r = r.replace(" ", "")
    if not r.isdigit():
        return None
    if int(r) > 20000000:
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

def specialCaseLocation2(r):
    if r is None:
        return None
    if r.split(" ")[0] == "Borivoja":
        return "Borivoja Stanojevica"
    elif r.split(" ")[0] == "PALILULA":
        return "Palilula"
    elif r.split(" ")[0] == "HITNO!":
        return "Stara Pazova"
    elif r.split(" ")[0] == "***LUX***":
        return "Ruma"
    elif '\u0408' in r:
        return "Jevremova"
    else:
        return r.title()

def cleanLocation2(r):
    r = cleanChars(r)
    r = specialCaseLocation2(r)
    if r is not None and r == '-':
        return None
    if r is not None and r.isdigit():
        return None
    if r is not None and ',' in r:
        return r.split(",")[0]
    return r

def cleanSquareFootage(r):
    if r.isdigit():
        r = int(r)
        if r < 0:
            return r * (-1)
        if r > 9000:
            return None
        return r
    else:
        if 'ar' in r:
            return int(float(r.split(" ar")[0]) * 100)
        if '.' in r:
            return int(round(float(r)))
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

def cleanFloor2(floor):
    if 'suteren' in floor:
        return floor.replace("suteren", "-1")
    if 'podrum' in floor:
        return floor.replace("podrum", "-1")
    if 'nisko prizemlje' in floor:
        return floor.replace("nisko prizemlje", "0")
    if 'visoko prizemlje' in floor:
        return floor.replace("visoko prizemlje", "0")
    if 'prizemlje' in floor:
        return floor.replace("prizemlje", "0")
    if 'potkrovlje' in floor:
        return floor.replace("potkrovlje", "max")
    else:
        return floor

def cleanFloor(floor):
    if floor is not None:
        floor = cleanFloor2(floor.lower())
        curr = None
        total = None
        if ' / ' in floor:
            curr = floor.split(' / ')[0]
            total = floor.split(' / ')[1]
        elif '/' in floor:
            curr = floor.split('/')[0]
            total = floor.split('/')[1].split(' ')[0]
        elif '.' in floor:
            curr = floor.split('.')[0]
        else:
            curr = floor
        if curr.isdigit() or curr == '-1' or curr == '-2':
            curr = int(curr)
        if total is not None and total.isdigit():
            total = int(total)
        if curr == '1.5':
            curr = 2
        if curr == '-':
            curr = None
        if total == '-':
            total = None
        if total is None and curr == 'max':
            return None, None
        elif total is not None and curr == 'max':
            return total, total
        if curr is not None and curr > 45:
            return None, None
        if total is not None and curr is not None and curr > total:
            return None, None
        return curr, total
    return None, None

def cleanBooked(r):
    r = cleanChars(r)
    if r == "Da" or r == "uknjizeno":
        return 1
    elif r is None:
        return None
    else:
        return 0

def cleanHeating(r):
    if r is not None:
        r = cleanChars(r).lower()
        if '-' in r:
            return None
        if "centralno" in r:
            return 1
        else:
            return 0
    return None

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
            #r["Godina izgradnje"] = cleanYearBuilt(r["Godina izgradnje"])
            r["Povrsina zemljista"] = cleanArea(r["Povrsina zemljista"])
            r["Sprat"], r["Ukupna spratnost"] = cleanFloor(r["Spratnost"])
            r["Uknji\u017eenost"] = cleanBooked(r["Uknji\u017eenost"])
            r["Tip grejanja"] = cleanHeating(r["Tip grejanja"])
            r["Broj soba"] = cleanRoom(r["Broj soba"])
            r["Broj kupatila"] = cleanBathrooms(r["Broj kupatila"])
            r["Parking"] = cleanParking(r["Parking"])
            r["Lift"] = cleanElevator(r["Lift"])
            r["Terasa"] = cleanTerrace(r["Terasa"])
            del r["Spratnost"]
            r["Uknjizenost"] = r.pop("Uknji\u017eenost")
            if r["Lokacija2"] is not None and '\u0408\u0435\u0432\u0440\u0435\u043c\u043e\u0432\u0430' in r["Lokacija2"]:
                print(r["Lokacija2"])
    with open('cleaned.json', 'w') as output_file:
        output_file.write(
        '[' +
        ',\n'.join(json.dumps(i) for i in result) +
        ']\n')
cleanJSON("houses.json")