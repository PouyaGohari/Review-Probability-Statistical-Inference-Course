import numpy as np

C = np.zeros(shape=(1, 366), dtype=float)
for l in range(10):
  for i in range(1, 365):
      for j in range(10000):
          trials = np.random.randint(low=1, high=366, size=(1, i))
          trials = np.sort(trials)
          for k in range(i-2):
            if(trials[0][k] == trials[0][k+1] and trials[0][k+1] == trials[0][k+2]):
                C[0][i] += 1
                break
      C[0][i] = C[0][i] / 10000
      if(C[0][i] > 0.5):
        print(i, C[0][i])
        break