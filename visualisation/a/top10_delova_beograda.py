import json
import matplotlib.pyplot as plt
import numpy as np


def plotting(file):
    with open(file, 'r') as infile:
        dict_json = json.load(infile)
    labels = []
    values = []
    for dict1 in dict_json:
        labels.append(dict1['Uza lokacija'])
        values.append(dict1['Broj nekretnina'])
    x = np.arange(len(labels))  # the label locations [0 1 2 3 4 5 6]
    width = 0.75  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, values, width)
    i = 0
    for r in rects1:
        if i % 2 == 0:
            r.set_color('c')
        i += 1
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Broj nekretnina')
    ax.set_title('Top 10 delova Beograda po broju nekretnina')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.bar_label(rects1, padding=1)
    fig.tight_layout()
    fig.autofmt_xdate()
    plt.savefig('izgradjene_nekretnine.png')
    plt.show()

plotting("top10_delova_beograda.json")
