import json
import numpy as np
from sklearn.utils import shuffle

HYPERPARAMETERS = {
    'num_features': 3,
    'features': ('distance', 'squareFootage', 'numberOfRooms'),
    'learning_rate': 0.01, # 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1
    'mini_batch_size': 32, # 32, 64, 128
    'random_seed': 0,
    'outer_cv_fold': 10,
    'inner_cv_fold': 10,
    'iterations': 1000
}
# ------------------------------------------PREPROCESSING DATA----------------------------------------------------------
# I Create and import data and output
with open("../data/leon.json", 'r') as infile:
    json_data = json.load(infile)
m = len(json_data)
data = np.zeros([m, HYPERPARAMETERS['num_features']+1])
#output = np.zeros([m, 1])
i = 0
for r in json_data:
    j = 1
    for feature in HYPERPARAMETERS['features']:
        data[i, j] = r[feature]
        j += 1
    data[i, 0] = r['price']
    i += 1
# II Normalization (Standardization)
#data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)
for col in range(data.shape[1]):
    if col == 0:
        continue
    colMax = np.max(data[:, col])
    colMin = np.min(data[:, col])
    if colMin != colMax:
        data[:, col] = (data[:, col] - colMin) / (colMax - colMin)
    else:
        data[:, col] = (data[:, col] - colMin) / colMax
    print('column max and min are ')
    print(colMax)
    print(colMin)
# III Shuffling data
#data, output = shuffle(data, output, random_state=HYPERPARAMETERS['random_seed'])
np.random.shuffle(data)
#output = np.copy(data[:, 0]).reshape((m, 1))
# IV Adding first column of ones for bias term
#data = np.hstack((np.ones((m, 1)), data[:, 1:]))
# -----------------------------------------Nested Cross Validation------------------------------------------------------
# I Splitting data k-fold on train and test set

# III Creating model parameters initialized with zeros
params = np.zeros(np.shape(data)[1])
# IV Splitting training data on mini-batches
m_batch = HYPERPARAMETERS['mini_batch_size']
for _ in range(HYPERPARAMETERS['iterations']):
    for b in range(0, data.shape[0], m_batch):
        X = data[b:b+m_batch] # 32x8
        output = np.copy(X[:, 0])
        print(output)
        X[:, 0] = 1
        h = np.transpose(np.matmul(params, np.transpose(X))) # 32x1
        # V Loss funtion
        L = h - output # 32x1
        J = np.sum(np.square(L))/(2*X.shape[0])
        dJ = np.matmul(np.transpose(L), X) # 1 x NUM_FEATURES + 1
        #print(J)
        # VI Updating model parameters
        params = params - (HYPERPARAMETERS['learning_rate'] / X.shape[0]) * dJ
        #print(b/32)
        #print(np.sum(dJ))
        #print(dJ)
    print("sasrddfguiggohsdbsdhofhsdoighdfoighsdfoighiosduhgoisdzhfouisdhgoufhgiuo")
    #print(temp)
    #print(np.mean(J_list[100:]))
