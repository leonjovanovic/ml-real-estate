#Broj izgrađenih nekretnina po dekadama (1951-1960, 1961-1970, 1971-1980, 1981-1990, 1991-2000, 2001-2010, 2011-2020)1,
# a obuhvatiti i sekcije za prodaju i za iznajmljivanje.

import json

dict_json = {'1951-1960': 0, '1961-1970': 0, '1971-1980': 0, '1981-1990': 0, '1991-2000': 0, '2001-2010': 0, '2011-2020': 0}


def updateDict(r):
    if 1951 <= r <= 1960:
        dict_json['1951-1960'] += 1
    elif 1961 <= r <= 1970:
        dict_json['1961-1970'] += 1
    elif 1971 <= r <= 1980:
        dict_json['1971-1980'] += 1
    elif 1981 <= r <= 1990:
        dict_json['1981-1990'] += 1
    elif 1991 <= r <= 2000:
        dict_json['1991-2000'] += 1
    elif 2001 <= r <= 2010:
        dict_json['2001-2010'] += 1
    elif 2011 <= r <= 2020:
        dict_json['2011-2020'] += 1


def create_json(file):
    with open(file, 'r') as infile:
        result = json.load(infile)
        for r in result:
            if r['godina_izgradnje'] is not None:
                updateDict(r['godina_izgradnje'])

    print(dict_json)

    with open('izgradjene_nekretnine.json', 'w') as output_file:
        output_file.write(
            '[' +
            json.dumps(dict_json, indent=4) +
            ']\n')


create_json("../data_real_estates.json")
