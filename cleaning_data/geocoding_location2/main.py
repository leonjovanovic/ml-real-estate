import json
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
from geopy.distance import great_circle


def createCoordsJSON(file):
    AUTH_KEY = "AIzaSyBmlo6HJUsLuxFT2ufSsScl7NKsANrlKoU"
    geolocator = GoogleV3(api_key=AUTH_KEY)

    dict_loc = {}
    count = 0
    with open(file, 'r') as infile:
        result = json.load(infile)
        for r in result:
            print(count)
            if r['lokacija'] is not None:
                adr = r['lokacija']
                adresa = r['lokacija'] + ", Belgrade, Serbia"
                print(adresa)
                coords = geolocator.geocode(adresa)
                print(coords)
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


createCoordsJSON("location2.json")
