import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def cost_func(x, a, b, c):
    return a + b * x + c * (x ** 2)


def demand_func(p, a, b, c):
    return np.exp(a - b * p * 1.2 * 1.3) + c


def profit_func(demand, quantity, costs):
    return demand * quantity*1000 - costs*1000


def fit_demand():
    q = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).astype('float64')
    costs = np.array([18.0, 19.0, 19.3, 19.9, 20.3, 21.5, 23.0, 25.1, 26.2, 27.3]).astype('float64')
    quantities = np.linspace(1, 200)

    params_costs = curve_fit(cost_func, q, costs)
    print(params_costs[0])
    costs_fitted = cost_func(quantities, *params_costs[0])
    prices_initial = np.linspace(1, 50)

    prices_for_demand = np.array([15.29, 13.66, 15.71, 16.62, 14.31, 15.86, 16.25, 13.41, 13.56, 15.57]).astype(
        'float64')
    quantities_for_demand = np.array([6.89, 9.79, 6.57, 5.48, 8.74, 6.36, 5.99, 9.92, 9.85, 6.56]).astype('float64')

    params_demand = curve_fit(demand_func, prices_for_demand, quantities_for_demand)
    print(params_demand[0])
    demand_fitted = demand_func(prices_initial, *params_demand[0])
    profit_fitted = profit_func(demand_fitted, quantities, costs_fitted)

    f = plt.figure()
    plt.plot(prices_initial, profit_fitted, label="Fitted profit function")
    plt.plot(prices_initial, [0]*len(prices_initial), "r-")
    maximum_x = prices_initial[np.argmax(profit_fitted)]
    maximum_y = np.max(profit_fitted)
    plt.title(f"Profit function in relation to prices, \n"
              f"maximum at price={round(maximum_x, 2)} with profit={round(maximum_y, 2)}")
    plt.scatter(maximum_x, maximum_y)
    plt.ylabel("Profit")
    plt.xlabel("Price")
    plt.show()
    plt.savefig("Task6_graph.png")


if __name__ == '__main__':
    fit_demand()
