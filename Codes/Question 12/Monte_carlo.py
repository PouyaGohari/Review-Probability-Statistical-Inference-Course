import numpy as np
import matplotlib.pyplot as plt
import math

def estimate_pi(trials_size, fig_iter):
    x_min = 0
    x_max = 1
    y_min = 0
    y_max = 1
    x = np.random.uniform(x_min, x_max, size=trials_size)
    y = np.random.uniform(y_min, y_max, size=trials_size)

    x_circle, y_cirlce = [], []

    for i in range(trials_size):
        if x[i]**2 + y[i]**2 <= 1:
            x_circle.append(x[i])
            y_cirlce.append(y[i])

    circle_probability = len(x_circle) / trials_size
    estimating_pi = 4 * circle_probability
    print(f'trials: {trials_size}, estimate pi: {estimating_pi}, real pi: {math.pi}')

    plt.figure(fig_iter)
    plt.scatter(x, y, color='b', label='square')
    plt.scatter(x_circle, y_cirlce, color='r', label='circle')
    plt.legend()
    plt.show()
iterate = 1000
fig_iter = 0

while (iterate <= 1000000):
    estimate_pi(iterate, fig_iter)
    iterate = 10 * iterate   
    fig_iter += 1