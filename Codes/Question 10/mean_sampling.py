import numpy as np
import matplotlib.pyplot as plt

uniform_mean = np.zeros(shape=(10000, ))
normal_mean = np.zeros(shape=(10000, ))
gamma_mean = np.zeros(shape=(10000, ))
exponential_mean = np.zeros(shape=(10000, )) 
binomial_mean = np.zeros(shape=(10000, ))
my_dict =["uniform", "normal", "gamma dist", "exponential dist", "binomial dist"]
means = [uniform_mean, normal_mean, gamma_mean, exponential_mean, binomial_mean]
for i in range(10000):
    x_1 = np.random.uniform(size= 1000)
    x_2 = np.random.normal(size= 1000)
    x_3 = np.random.gamma(2, 4, size= 1000)
    x_4 = np.random.exponential(size= 1000)
    x_5 = np.random.binomial(100, 0.2, size= 1000)
    x = [x_1, x_2, x_3, x_4, x_5]
    for j in range(len(x)):
        means[j][i] = x[j].mean()

for i,m in enumerate(means):
    plt.figure(i)
    plt.hist(m, bins=20, alpha=0.7, density=True)
    plt.xlabel(f'{my_dict[i]}')
    plt.ylabel(f'mean {my_dict[i]}')
    plt.grid(True)

plt.tight_layout()
plt.show()