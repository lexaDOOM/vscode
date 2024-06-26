from math import *
	
def g(x, a):
    num = 9 * (7 * a ** 2 - 19 * a * x + 10 * x ** 2)
    den = 25 * a ** 2 + 30 * a * x + 9 * x ** 2
    if den == 0:
        print('Ошибка. Знаменатель равен нулю!')
        exit()
    return round(num / den, 5)

def f(x ,a):
    return round(cos(9 * (a ** 2) - 13 * a * x - 10 * (x ** 2)), 5)

def y(x, a):
    u_log = -80 * (a ** 2 - 46 * a * x + 21 * (x ** 2) + 1)
    if u_log < 0 or u_log == 1:
        print('Ошибка. Подлогарифменное выражение ∉ (0; 1) v (1; +∞)')
        exit()
    return round((log(u_log) / log(10)), 5)

x = int(input('x = '))

a = int(input('a = '))

fx = input('Выберите функцию:\n1 - G\n2 - F\n3 - Y')

if fx == '1':
    print('G = ', g(x, a))
elif fx == '2':
    print('F = ', f(x, a))
elif fx == '3':
    print ('Y = ', y(x, a))
else:
    print('Ошибка. Выбран неверный вариант!')
    exit()
