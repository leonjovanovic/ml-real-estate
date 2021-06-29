# Broj nekretnina za prodaju koje imaju parking, u odnosu na ukupan broj nekretnina za prodaju (samo za Beograd).

import json
import matplotlib.pyplot as plt
import numpy as np

dict_json = {'Ima parking': 0, 'Ukupno nekretnina': 0}


def plotting():
    labels = ['Ima parking', 'Ukupno nekretnina']
    x = np.arange(len(labels))  # the label locations [0 1 2 3 4 5 6]
    width = 0.75  # the width of the bars
    values = [dict_json['Ima parking'], dict_json['Ukupno nekretnina']]
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, values, width)
    rects1[0].set_color('c')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Broj nekretnina')
    ax.set_title('Parking nekretnina za prodaju u Beogradu')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.bar_label(rects1, padding=1)
    fig.tight_layout()
    # fig.autofmt_xdate()
    plt.savefig('izgradjene_nekretnine.png')
    plt.show()


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

plotting()
