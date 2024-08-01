import numpy as np

B = np.zeros(shape=(1, 366), dtype=float)
for k in range(10):
    for i in range(1, 366):
        for j in range(10000):
            trials = np.random.randint(low=1, high=366, size=(1, i))
            unique_value = np.unique(trials)
            if(unique_value.shape[0] != trials.shape[1]):
                B[0][i]  += 1
        B[0][i] = B[0][i] / 10000
        if(B[0][i] > 0.9):
            print(i, B[0][i])
            break