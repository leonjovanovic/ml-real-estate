import json
import numpy as np
from sklearn.utils import shuffle

HYPERPARAMETERS = {
    'num_features': 7,
    'features': ('lokacija2', 'kvadratura', 'sprat', 'broj_soba', 'parking', 'lift', 'terasa'),
    'learning_rate': 0.01,
    'random_seed': 0,
    'data_size': 100828
}
#-------------------------------------------PREPROCESSING DATA----------------------------------------------------------
# I Create and import data and output
with open("../data/data_flats_sale.json", 'r') as infile:
    json_data = json.load(infile)
data = np.zeros([len(json_data), HYPERPARAMETERS['num_features']])
output = np.zeros([len(json_data), 1])
i = 0
for r in json_data:
    j = 0
    for feature in HYPERPARAMETERS['features']:
        data[i, j] = r[feature]
        j += 1
    output[i, 0] = r['cena']
    i += 1
# II Normalization (Standardization)
data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)
# III Shuffling data
data, output = shuffle(data, output, random_state=HYPERPARAMETERS['random_seed'])
# 3) Podeliti podatke u train, dev, test skupove (0.6, 0.2, 0.2)
# 4) Ugnjezdena unakrsna validacija struktura
# -- Gradijentni spust
# 5) Vektor sa parametrima 1 x broj_osobina + 1 (bias)
# 6) Cost fija (stochastic, mini-batch, batch)
# 7) Updejtovanje parametara
