from math import log , log10 , cos , tan
print("Введіть значення X в проміжку [2;5]:")
x = float(input())
a = 2
b = 5
h = 0.2
while a <= x <= b:
    if x < 3:
        y=log10(abs(log(x)+1/(cos(x))))
        print("x=",x, "y=", y)
    elif 3<=x<4:
        y = 1/tan(x+log(x))
        print("x=",x, "y=", y)
    elif x > 4:
        y = 1/(16-x**2)
        print("x=",x, "y=", y)
    x += h