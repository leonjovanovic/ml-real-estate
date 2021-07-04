import json
from numpy import zeros as np_zeroes
from numpy import mean as np_mean
from numpy import std as np_std
from numpy import sqrt as np_sqrt
from numpy import sum as np_sum
from numpy import argmax as np_argmax
from numpy import argpartition as np_argpartition
from numpy import array as np_array
from numpy import absolute as np_absolute

HYPERPARAMETERS = {
    'num_features': 7,
    'features': ('lokacija2', 'kvadratura', 'sprat', 'broj_soba', 'parking', 'lift', 'terasa'),
    'normalization': False,
}

def train_main(new_data, k_auto, k):
    # ------------------------------------------PREPROCESSING DATA----------------------------------------------------------
    # I Create and import data and output
    with open("../data/data_flats_sale.json", 'r') as infile:
        json_data = json.load(infile)
    m = len(json_data)
    results = [0] * 5
    data = np_zeroes([m, HYPERPARAMETERS['num_features']])
    output = np_zeroes([m, 1])
    i = 0
    for r in json_data:
        j = 0
        for feature in HYPERPARAMETERS['features']:
            data[i, j] = r[feature]
            j += 1
        output[i, 0] = r['cena'] // 50000
        output[i, 0] = r['cena'] // 50000 if r['cena'] // 50000 < 5 else 4
        i += 1
    # II Normalization (Standardization)
    if HYPERPARAMETERS['normalization']:
        mean = np_mean(data, axis=0)
        data = data - mean
        new_data = new_data - mean
        std = np_std(data, axis=0)
        data = data / std
        new_data = new_data / std
    # III Calculate K
    if k_auto:
        k = int(np_sqrt(m))
    if k % 2 == 0:
        k += 1
    # IV Euclidean distance
    distance = np_sqrt(np_sum((data - new_data) ** 2, axis=1))
    k_indexes = np_argpartition(distance, k)[:k]
    for index in k_indexes:
        results[int(output[index])] += 1
    final_class_1 = np_argmax(np_array(results))
    # V Manhatten distance
    distance = np_sum(np_absolute(data - new_data), axis=1)
    k_indexes = np_argpartition(distance, k)[:k]
    for index in k_indexes:
        results[int(output[index])] += 1
    final_class_2 = np_argmax(np_array(results))
    return final_class_1, final_class_2

