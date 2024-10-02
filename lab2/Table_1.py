from math import log , log10 , cos , tan

a = 2
b = 5
h = 0.2

x = a
arg1 = 3
arg2 = 4
while a <= x <= b:
    if x < arg1:
        y=log10(abs(log(x) + 1/(cos(x))))
        print(f"x=,{x}, y=, {y}")

    elif arg1<=x<arg2:
        y = 1/tan(x + log(x))
        print(f"x=,{x}, y=, {y}")
    
    elif x > arg2:
        y = 1/(16 - x**2)
        print(f"x=,{x}, y=, {y}")
    
    x += h
    x = round(x , 2)