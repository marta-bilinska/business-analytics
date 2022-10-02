import numpy as np
import matplotlib.pyplot as plt


def profit_func(Q):
    return -2.5 * (Q ** 4) + 22 * (Q ** 3) - 7.25 * (Q ** 2) + 90 * Q - 40


def maximize_profit():
    # Profit(Q)=-2,5×Q^4+22×Q^3-7,25×Q^2+90×Q-40
    quantities = np.linspace(1, 10)
    profits = profit_func(quantities)
    print(profits)
    f = plt.figure(figsize=(10, 10))
    plt.plot(quantities, profits)
    plt.plot(quantities, [0] * len(quantities), "r-")
    maximum_x = quantities[np.argmax(profits)]
    maximum_y = np.max(profits)
    plt.title(f"Profit function, maximum at quantity={round(maximum_x, 2)} with profit={round(maximum_y, 2)}")
    plt.xlabel("Quantity")
    plt.ylabel("Profit")
    plt.scatter(maximum_x, maximum_y)
    plt.show()
    plt.savefig("Task4_graph.png")


if __name__ == '__main__':
    maximize_profit()
