from math import log , log10 , cos , tan

a = 2
b = 5
h = 0.2

x = a
while a <= x <= b:
    if x < 3:
        y=log10(abs(log(x) + 1/(cos(x))))
        print(f"x=,{x:.2f}, y=, {y}")

    elif 3<=x<4:
        y = 1/tan(x + log(x))
        print(f"x=,{x:.2f}, y=, {y}")
    
    elif x > 4:
        y = 1/(16 - x**2)
        print(f"x=,{x:.2f}, y=, {y}")

    x += h