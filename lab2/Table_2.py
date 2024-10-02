m = 20
h = 0.05  
d = 0.001  
x_values = [i * h for i in range(int(0.5 / h) + 1)]  # Точки на інтервалі [0, 0.5]

# Функція для обчислення факторіала
def my_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Функція для обчислення добутку діапазону
def my_prod(start, stop):
    result = 1
    for i in range(start, stop - 1, -1):
        result *= i
    return result

# Функція для обчислення ряду
def taylor_series(x, m, error_tol):
    sum_result = 1  
    term = 1  
    n = 1
    while abs(term) > error_tol:
        term = (-1)**n * my_prod(m, m - n + 1) / my_factorial(n) * x**n
        sum_result += term
        n += 1
    return sum_result

# Обчислення результатів для кожної точки
results = [(x, taylor_series(x, m, d)) for x in x_values]

# Виведення результатів
for x, value in results:
    x = round(x , 3)
    print(f"x = {x}, y = {value}")
