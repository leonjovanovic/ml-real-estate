import json
from geopy.distance import geodesic
from geopy.distance import great_circle
from geopy.geocoders import GoogleV3


def createCoordsJSON(file):
    AUTH_KEY = "API_KEY"
    geolocator = GoogleV3(api_key=AUTH_KEY)
    dict_loc = {}
    count = 0
    with open(file, 'r') as infile:
        result = json.load(infile)
        for r in result:
            print(count)
            if r['lokacija'] is not None:
                adr = r['lokacija']
                adresa1 = r['lokacija'] + ", Belgrade, Serbia"
                adresa2 = r['lokacija'] + ", Beograd"
                print(adresa1)
                if 'Kula ' in adr or 'Scala' in adr or 'Sole' in adr or 'Libera' in adr or 'Aqua' in adr or 'Verde' in adr or 'Simfonija' in adr or 'Terra' in adr or 'Aria' in adr or 'Metropolitan' in adr or 'Aurora' in adr or 'Quartet' in adr or 'Terraces' in adr:
                    dict_loc[adr] = (44.806789, 20.449261)
                else:
                    coords = geolocator.geocode(adresa1)
                    if coords is not None:
                        dict_loc[adr] = (coords.latitude, coords.longitude)
                    else:
                        coords = geolocator.geocode(adresa2)
                        if coords is not None:
                            dict_loc[adr] = (coords.latitude, coords.longitude)
                        else:
                            dict_loc[adr] = (None, None)
            count += 1

    with open('location2_coords.json', 'w') as output_file:
        output_file.write(
            '[' +
            json.dumps(dict_loc, indent=4) +
            ']\n')

def calculateDistance():
    with open('location2_coords.json', 'r') as infile:
        results = json.load(infile)

    for r in results:
        li = list(r)
        for l in li:
            if r[l] is not None:
                distance = geodesic(r[l], (44.8125449, 20.4612299)).km


#createCoordsJSON("location2.json")
calculateDistance()
