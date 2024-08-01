import numpy as np
B_validate = np.zeros(shape=(1, 365), dtype=float)
for k in range(10):
    for i in range(1, 365):
        for j in range(30):
            trials = np.random.randint(low=1, high=366, size=(1, i))
            unique_value = np.unique(trials)
            if(unique_value.shape[0] != trials.shape[1]):
                B_validate[0][i]  += 1
        B_validate[0][i] = B_validate[0][i] / 30
        if(B_validate[0][i] > 0.9):
            print(i, B_validate[0][i])
            break