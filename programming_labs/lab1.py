from math import *

def g(x, a):
    return round((9 * (7 * (a ** 2) - 19 * a * x) + 10 * (x ** 2)) / (25 * (a ** 2) + 30 * a * x + 9 * (x ** 2)), 5)

def f(x ,a):
    return round(cos(9 * (a ** 2) - 13 * a * x - 10 * (x ** 2)), 5)

def y(x, a):
    return round((log (-80 * (a ** 2 - 46 * a * x + 21 * (x ** 2) + 1)) / log(10)), 5)

x = int(input('x = '))
a = int(input('a = '))
print('G = ', g(x, a))

x = int(input('x = '))
a = int(input('a = '))
print('F = ', f(x, a))

x = int(input('x = '))
a = int(input('a = '))
print('Y = ', y(x, a))
