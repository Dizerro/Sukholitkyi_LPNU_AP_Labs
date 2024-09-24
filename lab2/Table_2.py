import numpy as np
from math import factorial , prod 

m = 20
h = 0.05  
d = 0.001  
x_values = np.arange(0, 0.5 + h, h)  # точки на інтервалі [0, 0.5]

# Функція для обчислення ряду
def taylor_series(x, m, error_tol):
    sum_result = 1  
    term = 1  
    n = 1
    while abs(term) > error_tol:  
        term = (-1)**n * prod(range(m, m - n, -1)) / factorial(n) * x**n
        sum_result += term
        n += 1
    return sum_result

results = [(x, taylor_series(x, m, d)) for x in x_values]

for x, value in results:
    print(f"x = {x:.2f}, y = {value:.10f}")
