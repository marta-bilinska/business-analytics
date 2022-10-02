import numpy as np
import matplotlib.pyplot as plt


def demand_func(p, a, b):
    return np.exp(-a * p - b)


def costs_func(q, a, b, c):
    return a + b * q + c * (q ** 2)


def profits_func(prices, demands, costs):
    return prices * demands - costs


def maximize_profit():
    # Profit(Q)=-2,5×Q^4+22×Q^3-7,25×Q^2+90×Q-40
    prices = np.linspace(1, 100)
    demands = demand_func(prices, 0.1, -3)
    total_costs = costs_func(demands, 2, 9, 0.1)
    profits = profits_func(prices, demands, total_costs)

    f = plt.figure()
    plt.plot(prices, profits)
    plt.plot(prices, [0] * len(prices), "r-")
    maximum_x = prices[np.argmax(profits)]
    maximum_y = np.max(profits)
    plt.title(f"Profit function, maximum at price={round(maximum_x, 2)} with profit={round(maximum_y, 2)}")

    plt.scatter(maximum_x, maximum_y)
    plt.xlabel("Price")
    plt.ylabel("Profit")
    plt.show()
    plt.savefig("Task5.1&2.png")

def marketing_spend_analysis():
    prices = np.linspace(1, 100)
    demands = demand_func(prices, 0.1, -3.4)
    total_costs = costs_func(demands, 2, 9, 0.1) + 10
    profits = profits_func(prices, demands, total_costs)
    f = plt.figure()
    plt.plot(prices, profits)
    plt.plot(prices, [0] * len(prices), "r-")
    maximum_x = prices[np.argmax(profits)]
    maximum_y = np.max(profits)
    plt.title(f"Profit function after marketing campaign, \n"
              f"maximum at price={round(maximum_x,2)} with profit={round(maximum_y, 2)}")
    plt.xlabel("Price")
    plt.ylabel("Profit")
    plt.scatter(maximum_x, maximum_y)
    plt.show()
    plt.savefig("Task5.3.png")

if __name__ == '__main__':
    # maximize_profit()
    marketing_spend_analysis()
