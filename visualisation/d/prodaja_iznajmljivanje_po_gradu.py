# Beograd, Novi Sad, Nis, Kragujevac, Jagodina

import json

dict_json = {'Beograd-prodaja': 0, 'Beograd-iznajmljivanje': 0,
             'Novi Sad-prodaja': 0, 'Novi Sad-iznajmljivanje': 0,
             'Nis-prodaja': 0, 'Nis-iznajmljivanje': 0,
             'Kragujevac-prodaja': 0, 'Kragujevac-iznajmljivanje': 0,
             'Jagodina-prodaja': 0, 'Jagodina-iznajmljivanje': 0}

dict_json_percentage = {'Beograd-prodaja': 0, 'Beograd-iznajmljivanje': 0,
                        'Novi Sad-prodaja': 0, 'Novi Sad-iznajmljivanje': 0,
                        'Nis-prodaja': 0, 'Nis-iznajmljivanje': 0,
                        'Kragujevac-prodaja': 0, 'Kragujevac-iznajmljivanje': 0,
                        'Jagodina-prodaja': 0, 'Jagodina-iznajmljivanje': 0}

def updateDict(r):
    if r['lokacija1'] == 'Beograd':
        if r['tip_ponude'] == 0:
            dict_json['Beograd-prodaja'] += 1
        else:
            dict_json['Beograd-iznajmljivanje'] += 1
    elif r['lokacija1'] == 'Novi Sad':
        if r['tip_ponude'] == 0:
            dict_json['Novi Sad-prodaja'] += 1
        else:
            dict_json['Novi Sad-iznajmljivanje'] += 1
    elif r['lokacija1'] == 'Nis':
        if r['tip_ponude'] == 0:
            dict_json['Nis-prodaja'] += 1
        else:
            dict_json['Nis-iznajmljivanje'] += 1
    elif r['lokacija1'] == 'Kragujevac':
        if r['tip_ponude'] == 0:
            dict_json['Kragujevac-prodaja'] += 1
        else:
            dict_json['Kragujevac-iznajmljivanje'] += 1
    elif r['lokacija1'] == 'Jagodina':
        if r['tip_ponude'] == 0:
            dict_json['Jagodina-prodaja'] += 1
        else:
            dict_json['Jagodina-iznajmljivanje'] += 1

def updateDictPercentage():
    dict_json_percentage['Beograd-prodaja'] = round(100.00 * float(dict_json['Beograd-prodaja'] / (dict_json['Beograd-prodaja'] + dict_json['Beograd-iznajmljivanje'])),2)
    dict_json_percentage['Beograd-iznajmljivanje'] = round(100.00 * float(dict_json['Beograd-iznajmljivanje'] / (dict_json['Beograd-prodaja'] + dict_json['Beograd-iznajmljivanje'])),2)
    dict_json_percentage['Novi Sad-prodaja'] = round(100.00 * float(dict_json['Novi Sad-prodaja'] / (dict_json['Novi Sad-prodaja'] + dict_json['Novi Sad-iznajmljivanje'])),2)
    dict_json_percentage['Novi Sad-iznajmljivanje'] = round(100.00 * float(dict_json['Novi Sad-iznajmljivanje'] / (dict_json['Novi Sad-prodaja'] + dict_json['Novi Sad-iznajmljivanje'])),2)
    dict_json_percentage['Nis-prodaja'] = round(100.00 * float(dict_json['Nis-prodaja'] / (dict_json['Nis-prodaja'] + dict_json['Nis-iznajmljivanje'])),2)
    dict_json_percentage['Nis-iznajmljivanje'] = round(100.00 * float(dict_json['Nis-iznajmljivanje'] / (dict_json['Nis-prodaja'] + dict_json['Nis-iznajmljivanje'])),2)
    dict_json_percentage['Kragujevac-prodaja'] = round(100.00 * float(dict_json['Kragujevac-prodaja'] / (dict_json['Kragujevac-prodaja'] + dict_json['Kragujevac-iznajmljivanje'])),2)
    dict_json_percentage['Kragujevac-iznajmljivanje'] = round(100.00 * float(dict_json['Kragujevac-iznajmljivanje'] / (dict_json['Kragujevac-prodaja'] + dict_json['Kragujevac-iznajmljivanje'])),2)
    dict_json_percentage['Jagodina-prodaja'] = round(100.00 * float(dict_json['Jagodina-prodaja'] / (dict_json['Jagodina-prodaja'] + dict_json['Jagodina-iznajmljivanje'])),2)
    dict_json_percentage['Jagodina-iznajmljivanje'] = round(100.00 * float(dict_json['Jagodina-iznajmljivanje'] / (dict_json['Jagodina-prodaja'] + dict_json['Jagodina-iznajmljivanje'])),2)

def create_json(file):
    with open(file, 'r') as infile:
        result = json.load(infile)
        for r in result:
            updateDict(r)

    updateDictPercentage()

    print(dict_json)
    print(dict_json_percentage)

    with open('prodaja_iznajmljivanje_po_gradu.json', 'w') as output_file:
        output_file.write(
            '[' +
            json.dumps(dict_json, indent=4) + '\n' + json.dumps(dict_json_percentage, indent=4) +
            ']\n')


create_json("../data_real_estates.json")
