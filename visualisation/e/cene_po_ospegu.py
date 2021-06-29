# Broj (i procentualni odnos) svih nekretnina za prodaju, koje po ceni pripadaju jednom od sledećih opsega:
# ▪ manje od 49 999 €,
# ▪ između 50 000 i 99 999 €,
# ▪ između 100 000 i 149 999 €,
# ▪ između 150 000 € i 199 999 €,
# ▪ 200 000 € ili više.

import json
import matplotlib.pyplot as plt
import numpy as np

dict_json = {'<50 000': 0, '50 000-99 999': 0, '100 000-149 999': 0, '150 000-199 999': 0, '>199 999': 0}
dict_json_percentage = {'<50 000': 0, '50 000-99 999': 0, '100 000-149 999': 0, '150 000-199 999': 0, '>199 999': 0}


def updateDict(r):
    if r < 50000:
        dict_json['<50 000'] += 1
    elif 50000 <= r <= 99999:
        dict_json['50 000-99 999'] += 1
    elif 100000 <= r <= 149999:
        dict_json['100 000-149 999'] += 1
    elif 150000 <= r <= 199999:
        dict_json['150 000-199 999'] += 1
    elif r >= 200000:
        dict_json['>199 999'] += 1
    else:
        print("Error")

def updateDictPercentage():
    sum = dict_json['<50 000'] + dict_json['50 000-99 999'] + dict_json['100 000-149 999'] + dict_json['150 000-199 999'] + dict_json['>199 999']
    dict_json_percentage['<50 000'] = round(100.00 * float(dict_json['<50 000'] / sum),2)
    dict_json_percentage['50 000-99 999'] = round(100.00 * float(dict_json['50 000-99 999'] / sum),2)
    dict_json_percentage['100 000-149 999'] = round(100.00 * float(dict_json['100 000-149 999'] / sum),2)
    dict_json_percentage['150 000-199 999'] = round(100.00 * float(dict_json['150 000-199 999'] / sum),2)
    dict_json_percentage['>199 999'] = round(100.00 * float(dict_json['>199 999'] / sum),2)

def plotting():
    labels = ['<50 000', '50 000-99 999', '100 000-149 999', '150 000-199 999', '>199 999']
    values = [dict_json['<50 000'], dict_json['50 000-99 999'], dict_json['100 000-149 999'], dict_json['150 000-199 999'], dict_json['>199 999']]
    fig, ax = plt.subplots(figsize=(8, 6.5))
    suma = sum(values)
    ax.pie(values, labels=labels, explode=(0.01, 0.01, 0.01, 0.01, 0.01), autopct=lambda p: '{:.1f}%({:.0f})'.format(p, (p/100)*suma),
            shadow=False, startangle=90, colors=['royalblue', 'deepskyblue', 'darkturquoise', 'cyan', 'tab:blue'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Nekretnine po cenama')
    plt.savefig('cene_po_opsegu.png')
    plt.show()


def create_json(file):
    with open(file, 'r') as infile:
        result = json.load(infile)
        for r in result:
            if r['tip_ponude'] == 0 and r['cena'] is not None:
                updateDict(r['cena'])

    updateDictPercentage()

    print(dict_json)
    print(dict_json_percentage)

    with open('cena_po_opsegu.json', 'w') as output_file:
        output_file.write(
            '[' +
            json.dumps(dict_json, indent=4) +
            ']\n')


create_json("../data_real_estates.json")
plotting()