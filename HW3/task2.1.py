import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from task1 import func


def fit_demands():
    x_range = np.linspace(1, 3)
    params = [[3.7, 1.9, -0.2, 1.5],
              [3.8, 2.2, -0.25, 1.55],
              [3.6, 1.6, -0.15, 1.45]]
    colors = ["red", "green", "yellow"]
    f = plt.figure()
    for i in range(0, len(params)):
        p_s = params[i]
        plt.plot(x_range, func(x_range, *p_s), '-', color=colors[i],
                 label=f"Fitted function with a={p_s[0]}, b={p_s[1]}, c={p_s[2]}, d={p_s[3]}")
    plt.legend()
    plt.title("Fitted demand curves")
    plt.xlabel("Price")
    plt.ylabel("Demand")
    plt.savefig("Task2.1_graph.png")


if __name__ == '__main__':
    fit_demands()
