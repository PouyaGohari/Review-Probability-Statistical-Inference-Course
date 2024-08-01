import numpy as np
import matplotlib.pyplot as plt

uniform_dist = np.random.uniform(size= 1000)
normal_dist = np.random.normal(size= 1000)
gamma_dist = np.random.gamma(2, 4, size= 1000)
exponential_dist = np.random.exponential(size= 1000)
binomial_dist = np.random.binomial(100, 0.2, size= 1000)
distributions = [uniform_dist, normal_dist, gamma_dist, exponential_dist, binomial_dist]
my_dict =["uniform", "normal", "gamma dist", "exponential dist", "binomial dist"]
for i in range(len(distributions)):
    plt.figure(i)
    plt.hist(distributions[i], bins=20, alpha=0.7, density=True)
    plt.title(f'Distribution of {my_dict[i]}')
    plt.xlabel(f'{my_dict[i]}')
    plt.ylabel(f'probability of {my_dict[i]}')
    plt.grid(True)

plt.tight_layout()
plt.show()