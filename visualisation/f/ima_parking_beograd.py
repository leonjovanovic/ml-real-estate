# Broj nekretnina za prodaju koje imaju parking, u odnosu na ukupan broj nekretnina za prodaju (samo za Beograd).

import json

dict_json = {'Ima parking': 0, 'Ukupno nekretnina': 0}

def create_json(file):
    ima_p = 0
    ukupno = 0
    ukupno_bez_none = 0
    with open(file, 'r') as infile:
        result = json.load(infile)
        for r in result:
            if r['lokacija1'] == 'Beograd' and r['tip_ponude'] == 0:
                ukupno += 1
                if r['parking'] is not None:
                    ukupno_bez_none += 1
                    if r['parking'] == 1:
                        ima_p += 1

    dict_json['Ima parking'] = ima_p
    dict_json['Ukupno nekretnina'] = ukupno
    print(dict_json)

    with open('ima_parking_beograd.json', 'w') as output_file:
        output_file.write(
            '[' +
            json.dumps(dict_json) +
            ']\n')


create_json("../data_real_estates.json")

