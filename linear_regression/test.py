import json
import numpy as np
from sklearn.utils import shuffle
import matplotlib.pyplot as plt

HYPERPARAMETERS = {
    'num_features': 7,
    'features': ('lokacija2', 'kvadratura', 'sprat', 'broj_soba', 'parking', 'lift', 'terasa'),
    'learning_rate': [0.001, 0.003, 0.01, 0.03],  # 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1
    'mini_batch_size': [16, 32, 64, 128],
    'random_seed': 1,
    'outer_cv_fold': 10,
    'inner_cv_fold': 10,
    'iterations': 50
}


def plotting(it, J_train, J_val):
    epochs = list(range(it))
    plt.plot(epochs, J_train, '-b+', label='J train')
    plt.plot(epochs, J_val, '-r', label='J val')
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
    # -------------------------------------------------------------------------------------------------------------------
    # --------------------------Nested Cross Validation For Finding BEST HYPERPARAMETERS--------------------------------
    # -------------------------------------------------------------------------------------------------------------------
    # I Splitting data k-fold on train and test set
    k = HYPERPARAMETERS['outer_cv_fold']
    l = HYPERPARAMETERS['inner_cv_fold']
    J_total = np.array([], dtype=np.int64).reshape(0, len(HYPERPARAMETERS['learning_rate']) * len(
        HYPERPARAMETERS['mini_batch_size']))
    for i in range(k):
        index = slice(int(i * m / k), int(i * m / k + m / k))
        test_data, test_output = data[index, :], output[index, :]
        trainval_data, trainval_output = np.delete(data, index, axis=0), np.delete(output, index, axis=0)
        J_avg_val_list = np.array([], dtype=np.int64).reshape(0, len(HYPERPARAMETERS['learning_rate']) * len(
            HYPERPARAMETERS['mini_batch_size']))
        # II Splitting data l-fold on train and validation set
        for j in range(l):
            index = slice(int(j * (m - m / k) / l), int(j * (m - m / k) / l + (m - m / k) / l))
            val_data, val_output = trainval_data[index, :], trainval_output[index, :]
            train_data, train_output = np.delete(trainval_data, index, axis=0), np.delete(trainval_output, index,
                                                                                          axis=0)
            # III Creating model parameters initialized with zeros
            params = np.zeros([1, HYPERPARAMETERS['num_features'] + 1])
            # IV Splitting training data on mini-batches
            J_val_list = []
            for lr in HYPERPARAMETERS['learning_rate']:
                for m_batch in HYPERPARAMETERS['mini_batch_size']:
                    J_val = 0
                    # -----------------------------------One trained model----------------------------------------------
                    for it in range(HYPERPARAMETERS['iterations']):
                        for b in range(0, train_data.shape[0], m_batch):
                            X = train_data[b:b + m_batch]  # 32x8
                            h = np.dot(X, params.transpose())  # 32x1
                            # V Loss funtion
                            L = h - train_output[b:b + m_batch]  # 32x1
                            J_train = np.sum(L ** 2) / (2 * X.shape[0])
                            # VI Updating model parameters
                            dJ = np.dot(L.transpose(), X)  # 1 x NUM_FEATURES + 1
                            params = params - (lr / X.shape[0]) * dJ
                            # --------------------Validation------------------------------------------------------------
                            h_val = np.dot(val_data, params.transpose())
                            L_val = h_val - val_output
                            J_val = np.sum(L_val ** 2) / (2 * val_data.shape[0])
                            # ------------------------------------------------------------------------------------------
                    J_val_list.append(J_val)
            J_avg_val_list = np.vstack([J_avg_val_list, J_val_list])
            # print(str(J_avg_val_list.shape[0]) + "/10")
        temp = list(np.mean(J_avg_val_list, axis=0))
        J_total = np.vstack([J_total, temp])
        print("Hyperparameter index for iteration " + str(J_total.shape[0]) + "/10 is " + str(temp.index(min(temp))))
    temp = list(np.mean(J_total, axis=0))
    print(temp)
    print("Hyperparameter index is " + str(temp.index(min(temp))))
    best_hparam_index = temp.index(min(temp))
    # best_hparam_index = 14
    best_hyperparams = [HYPERPARAMETERS['learning_rate'][best_hparam_index // len(HYPERPARAMETERS['learning_rate'])],
                        HYPERPARAMETERS['mini_batch_size'][best_hparam_index % len(HYPERPARAMETERS['mini_batch_size'])]]
    # -------------------------------------------------------------------------------------------------------------------
    # ---------------------Cross Validation On Evaluation For Finding MEAN PERFORMANCE----------------------------------
    # -------------------------------------------------------------------------------------------------------------------
    RMSE = []
    MAE = []
    for i in range(k):
        index = slice(int(i * m / k), int(i * m / k + m / k))
        test_data, test_output = data[index, :], output[index, :]
        trainval_data, trainval_output = np.delete(data, index, axis=0), np.delete(output, index, axis=0)
        params = np.zeros([1, HYPERPARAMETERS['num_features'] + 1])
        lr, m_batch = best_hyperparams[0], best_hyperparams[1]
        # -----------------------------------One trained model----------------------------------------------
        for it in range(HYPERPARAMETERS['iterations']):
            for b in range(0, trainval_data.shape[0], int(m_batch)):
                X = trainval_data[b:b + m_batch]  # 32x8
                h = np.dot(X, params.transpose())  # 32x1
                # V Loss funtion
                L = h - trainval_output[b:b + m_batch]  # 32x1
                J_train = np.sum(L ** 2) / (2 * X.shape[0])
                # VI Updating model parameters
                dJ = np.dot(L.transpose(), X)  # 1 x NUM_FEATURES + 1
                params = params - (lr / X.shape[0]) * dJ
        # --------------------Evaluation------------------------------------------------------------
        h_test = np.dot(test_data, params.transpose())
        L_test = h_test - test_output
        RMSE.append(np.sqrt(np.sum(L_test ** 2) / test_data.shape[0]))
        MAE.append(np.sum(np.absolute(L_test)) / test_data.shape[0])
        # ------------------------------------------------------------------------------------------
    print("Average root mean squared error: " + str(np.mean(RMSE)))
    print("Average mean absolute error: " + str(np.mean(MAE)))
    # -------------------------------------------------------------------------------------------------------------------
    # ----------------------------Training on whole data set for BEST PARAMETERS----------------------------------------
    # -------------------------------------------------------------------------------------------------------------------
    params = np.zeros([1, HYPERPARAMETERS['num_features'] + 1])
    lr, m_batch = best_hyperparams[0], best_hyperparams[1]
    # -----------------------------------One trained model----------------------------------------------
    for it in range(HYPERPARAMETERS['iterations']):
        for b in range(0, data.shape[0], int(m_batch)):
            X = data[b:b + m_batch]  # 32x8
            h = np.dot(X, params.transpose())  # 32x1
            # V Loss funtion
            L = h - output[b:b + m_batch]  # 32x1
            J_train = np.sum(L ** 2) / (2 * X.shape[0])
            # VI Updating model parameters
            dJ = np.dot(L.transpose(), X)  # 1 x NUM_FEATURES + 1
            params = params - (lr / X.shape[0]) * dJ
    with open('model_parameters.json', 'w') as output_file:
        output_file.write(json.dumps({"parameters": params.tolist()}, indent=4))


train_main()
