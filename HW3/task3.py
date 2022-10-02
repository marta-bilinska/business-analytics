import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def average_cost_func(x, a, b, c, d):
    return a - b * x - c * (x ** 2) + d * (x ** 3)


def total_cost_func(x, a, b, c, d, e):
    return a - b * x - c * (x ** 2) + d * (x ** 3) + e * (x ** 4)


def fit_costs():
    x_range = np.linspace(50, 1000)
    quantity = np.array([100, 200, 300, 400, 500, 600, 700, 800]).astype('float64')
    average_costs = np.array([2.9, 2.8, 2.6, 2.2, 1.9, 1.6, 1.35, 1.3]).astype('float64')
    total_costs = np.array([290, 560, 780, 880, 950, 960, 945, 1040]).astype('float64')
    params_average_costs = curve_fit(average_cost_func, quantity, average_costs)
    params_total_costs = curve_fit(total_cost_func, quantity, total_costs)

    f = plt.figure(figsize=(10, 10))
    p_s = params_average_costs[0]
    plt.plot(x_range, average_cost_func(x_range, *p_s), '-',
             label=f"Fitted average costs function with a={round(p_s[0], 2)}, b={round(p_s[1], 2)}, c={round(p_s[2], 2)}, d={round(p_s[3], 2)}")
    plt.scatter(quantity, average_costs)
    plt.legend()
    plt.xlabel("Quantity")
    plt.ylabel("Average costs")
    plt.title("Fitted average costs function")
    plt.savefig("Task3.1_graph.png")

    f2 = plt.figure(figsize=(10, 10))
    p_s = params_total_costs[0]
    plt.plot(x_range, total_cost_func(x_range, *p_s), '-',
             label=f"Fitted total costs function with a={round(p_s[0], 2)}, b={round(p_s[1], 2)}, c={round(p_s[2], 2)}, d={round(p_s[3], 2)}")
    plt.scatter(quantity, total_costs)
    plt.legend()
    plt.xlabel("Quantity")
    plt.ylabel("Total costs")
    plt.title("Fitted total costs function")
    plt.savefig("Task3.2_graph.png")


if __name__ == '__main__':
    fit_costs()
