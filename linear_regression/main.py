import json
import numpy as np
from sklearn.utils import shuffle
import matplotlib.pyplot as plt

HYPERPARAMETERS = {
    'num_features': 7,
    'features': ('lokacija2', 'kvadratura', 'sprat', 'broj_soba', 'parking', 'lift', 'terasa'),
    'learning_rate': 0.01, # 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1
    'mini_batch_size': 32, # 32, 64, 128
    'random_seed': 1,
    'outer_cv_fold': 5,
    'inner_cv_fold': 5,
    'iterations': 20
}

def plotting(it, cost_list, J_avg_val_list):
    epochs = list(range(it))
    plt.plot(epochs, cost_list, '-b+', label='J train')
    plt.plot(epochs, J_avg_val_list, '-r', label='J val')
    plt.legend()
    plt.show()

def train_main():
    # ------------------------------------------PREPROCESSING DATA----------------------------------------------------------
    # I Create and import data and output
    with open("../data/data_flats_sale.json", 'r') as infile:
        json_data = json.load(infile)
    m = len(json_data)
    data = np.zeros([m, HYPERPARAMETERS['num_features']])
    output = np.zeros([m, 1])
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
    # IV Adding first column of ones for bias term
    data = np.hstack((np.ones((m, 1)), data))
    # -----------------------------------------Nested Cross Validation------------------------------------------------------
    # I Splitting data k-fold on train and test set
    k = HYPERPARAMETERS['outer_cv_fold']
    l = HYPERPARAMETERS['inner_cv_fold']
    for i in range(k):
        index = slice(int(i * m / k), int(i * m / k + m / k))
        test_data, test_output = data[index, :], output[index, :]
        trainval_data, trainval_output = np.delete(data, index, axis=0), np.delete(output, index, axis=0)
        # II Splitting data l-fold on train and validation set
        for j in range(l):
            index = slice(int(j * (m - m / k) / l), int(j * (m - m / k) / l + (m - m / k) / l))
            val_data, val_output = trainval_data[index, :], trainval_output[index, :]
            train_data, train_output = np.delete(trainval_data, index, axis=0), np.delete(trainval_output, index, axis=0)
            # III Creating model parameters initialized with zeros
            params = np.zeros([1, HYPERPARAMETERS['num_features']+1])
            # IV Splitting training data on mini-batches
            m_batch = HYPERPARAMETERS['mini_batch_size']
            J_train_list = []
            J_avg_train_list = []
            J_val_list = []
            J_avg_val_list = []
            for it in range(HYPERPARAMETERS['iterations']):
                for b in range(0, train_data.shape[0], m_batch):
                    X = train_data[b:b+m_batch] # 32x8
                    h = np.dot(X, params.transpose()) # 32x1
                    # V Loss funtion
                    L = h - train_output[b:b+m_batch] # 32x1
                    J_train = np.sum(L**2)/(2*X.shape[0])
                    J_train_list.append(J_train)
                    # VI Updating model parameters
                    dJ = np.dot(L.transpose(), X) # 1 x NUM_FEATURES + 1
                    params = params - (HYPERPARAMETERS['learning_rate'] / X.shape[0]) * dJ
                    # --------------------Validation--------------------------------------------
                    h_val = np.dot(val_data, params.transpose())
                    L_val = h_val - val_output
                    J_val = np.sqrt(np.sum(L_val**2)/(2*val_data.shape[0]))
                    J_val_list.append(J_val)
                    #---------------------------------------------------------------------------
                print(it)
                J_avg_train_list.append(np.mean(J_train_list))
                J_avg_val_list.append(np.mean(J_val_list))
            plotting(HYPERPARAMETERS['iterations'], J_avg_train_list, J_avg_val_list)

        break

train_main()
