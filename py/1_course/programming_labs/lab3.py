from math import *
x_s = float(input('Введите стартовое значение x >> ')) # Сбор данных
x = x_s
x_e = float(input('Введите конечное значение x >> '))
a = float(input('Введите a >> '))
steps = int(input('Введите кол-во шагов >> '))
fx = int(input('Выберете ф-кицю:\n1 - G\n2 - F\n3 - Y\n>>'))
x_per_step = (x_e - x_s) / steps

if steps <= 0:
    print('Ошибка! Ненатуральное число шагов')
    exit()

if fx == 1: # G
    for i in range(steps):
        num = 9 * (7 * a * a - 19 * a * x + 10 * x * x) # Числитель
        den = 25 * a * a + 30 * a * x + 9 * x * x # Знаменатель

        if den == 0: # Если den == 0
            print('Ошибка! Знаменатель равен нулю.')
            exit()

        print(f'Шаг: {i + 1}, x = {x}, G = {round(num / den, 5)}')
        x += x_per_step

elif fx == 2: # F
    for i in range(steps):
        result = cos(9 * a * a - 13 * a * x - 10 * x * x)

        print(f'Шаг: {i + 1}, x = {x}, F = {round(result, 5)}')
        x += x_per_step

elif fx == 3: # Y
    for i in range(steps):
        u_log = -80 * a * a - 46 * a * x + 21 * x * x + 1 # Подлогарифменное выражение

        if u_log <= 0: # Если u_log <= 0
            print('Ошибка! Подлогарифменное выражение <= 0')
            exit()

        result = log(u_log) / log(10)

        print(f'Шаг: {i + 1}, x = {x}, Y = {round(result, 5)}')
        x += x_per_step

else:
    print('Ошибка! Такой функции нет!')
    exit()
