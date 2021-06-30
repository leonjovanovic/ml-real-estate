import json

import numpy as np

HYPERPARAMETERS = {
    'num_features': 5,
    'features': ('lokacija2', 'kvadratura', 'uknjizenost', 'tip_grejanja', 'broj_soba'),
    'learning_rate': 0.01,
    'random_seed': 1,
    'data_size': 100828
}
#-------------------------------------------PREPROCESSING DATA----------------------------------------------------------
# 1) Napraviti matricu broj_podataka x broj_osobina ---------- NE SME DA BUDE NONE
data = np.zeros([HYPERPARAMETERS['data_size'], HYPERPARAMETERS['num_features']])
i = 0
with open("../data/data_real_estates.json", 'r') as infile:
    json_data = json.load(infile)
    for r in json_data:
        j = 0
        for feature in HYPERPARAMETERS['features']:
            data[i, j] = r[feature]
            j += 1
        i += 1
# 2) Srediti podatke - normalizovati i izmesati
# II Normalization
i = 0
for _ in HYPERPARAMETERS['features']:
    mean = np.mean(data[:, i])
    sigma = np.sqrt(np.mean(data[:, i]**2))
    data[:, i] = (data[:, i] - mean)/sigma
    i += 1
# III Shuffling data


# 3) Podeliti podatke u train, dev, test skupove (0.6, 0.2, 0.2)
# 4) Ugnjezdena unakrsna validacija struktura
# -- Gradijentni spust
# 5) Vektor sa parametrima 1 x broj_osobina + 1 (bias)
# 6) Cost fija (stochastic, mini-batch, batch)
# 7) Updejtovanje parametara
