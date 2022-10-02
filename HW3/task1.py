import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(x, a, b, c, d):
    return np.exp(a - b * x - c * (x ** 2)) + d


def fit_demand():
    x = np.array([1.65, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.4]).astype('float64')
    x_range = np.linspace(1, 3)
    y = np.array([430, 397, 361, 336, 313, 292, 273, 256]).astype('float64')
    params = curve_fit(func, x, y)

    f = plt.figure()
    plt.plot(x_range, func(x_range, *params[0]), 'r-', label="Fitted function")
    plt.scatter(x, y)
    plt.legend()
    plt.title("Fitted Demand curve")
    plt.xlabel("Price")
    plt.ylabel("Demand")
    plt.savefig("Task1_graph.png")
    return params[0]


if __name__ == '__main__':
    print(fit_demand())
