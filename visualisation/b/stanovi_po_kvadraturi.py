import json

dict_json = {'<36': 0, '36-50': 0, '51-65': 0, '66-80': 0, '81-95': 0, '96-110': 0, '>110': 0}


def updateDict(r):
    if r < 36:
        dict_json['<36'] += 1
    elif 36 <= r <= 50:
        dict_json['36-50'] += 1
    elif 51 <= r <= 65:
        dict_json['51-65'] += 1
    elif 66 <= r <= 80:
        dict_json['66-80'] += 1
    elif 81 <= r <= 95:
        dict_json['81-95'] += 1
    elif 96 <= r <= 110:
        dict_json['96-110'] += 1
    elif r > 110:
        dict_json['>110'] += 1
    else:
        print("Error")


def create_json(file):
    with open(file, 'r') as infile:
        result = json.load(infile)
        for r in result:
            if r['tip_nekretnine'] == 0 and r['tip_ponude'] == 0 and r['kvadratura'] is not None:
                updateDict(r['kvadratura'])

    print(dict_json)

    with open('stanovi_po_kvadraturi.json', 'w') as output_file:
        output_file.write(
            '[' +
            json.dumps(dict_json, indent=4) +
            ']\n')


create_json("../data_real_estates.json")
