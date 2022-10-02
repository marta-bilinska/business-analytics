from task1 import func
from task2_2 import elasticity


def demand_change(a, b, c, d, price_initial, price_new):
    demand_initial = func(price_initial, a, b, c, d)
    demand_new = func(price_new, a, b, c, d)
    delta_demand = demand_new - demand_initial
    delta_revenue = demand_new*price_new - demand_initial*price_initial
    print(f"delta_demand = {delta_demand}, delta_revenue = {delta_revenue}, delta_demand/demand_initial = {delta_demand/demand_initial}")
    return delta_demand, delta_revenue, delta_demand/demand_initial


def price_change(a, b, c, d, price_initial, price_new):
    delta_price_per_price_initial = (price_new - price_initial)/price_initial
    price_elasticity = elasticity(a, b, c, d, price_initial)
    delta_demand_per_demand_initial = price_elasticity*delta_price_per_price_initial
    print(f"delta_price/price_initial = {delta_price_per_price_initial}")
    print(f"delta_demand/demand_initial = {delta_demand_per_demand_initial}")
    return delta_demand_per_demand_initial


if __name__ == '__main__':
    demand_change(3.7, 1.9, -0.2, 1.5, 1.8, 1.6)
    price_change(3.7, 1.9, -0.2, 1.5, 1.8, 1.6)
