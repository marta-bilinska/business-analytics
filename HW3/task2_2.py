import numpy as np
import pandas as pd
from task1 import func


def elasticity(a, b, c, d, price_point):
    return (-b - 2 * c * price_point) * price_point


if __name__ == '__main__':
    print(elasticity(3.7, 1.9, -0.2, 1.5, 1.6))
    print(elasticity(3.7, 1.9, -0.2, 1.5, 1.8))
