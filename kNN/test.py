import json
import numpy as np
from kNN import train_main

HYPERPARAMETERS = {
    'num_features': 7,
    'features': ('lokacija2', 'kvadratura', 'sprat', 'broj_soba', 'parking', 'lift', 'terasa'),
    'normalization': False,
}

with open("../data/data_flats_sale.json", 'r') as infile1:
    json_data1 = json.load(infile1)
m1 = len(json_data1)
data1 = np.zeros([m1, HYPERPARAMETERS['num_features']])
output1 = np.zeros([m1, 1])
i = 0
for r in json_data1:
    j = 0
    for feature in HYPERPARAMETERS['features']:
        data1[i, j] = r[feature]
        j += 1
    output1[i, 0] = r['cena'] // 50000
    output1[i, 0] = r['cena'] // 50000 if r['cena'] // 50000 < 5 else 4
    i += 1

euclidSum = 0
manhatttenSum = 0
for i in range(m1):
    print(i)
    r1, r2 = train_main(data1[i, :], True, 0)
    if r1 == output1[i, 0]:
        euclidSum += 1
    if r2 == output1[i, 0]:
        manhatttenSum += 1
print("Euklidovo rastojanje uspesnost: " + str(euclidSum/m1*100) + "%")
print("Menhetn rastojanje uspesnost: " + str(manhatttenSum/m1*100) + "%")