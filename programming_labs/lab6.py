from math import *


class Args:
    """Класс, описывающий уравнение"""

    x_s = 0  # x Начальное
    x_e = 0  # x Конечное

    a_s = 0  # a Начальное
    a_e = 0  # a Конечное

    def __init__(self, x_s, x_e, a_s, a_e, steps, fx):
        self.x_s = x_s
        self.x_e = x_e
        self.a_s = a_s
        self.a_e = a_e
        self.steps = steps
        self.fx = fx

    def get_fx(self):
        return self.fx


class Results:
    """Класс, хранящий результаты"""

    g_result = 0
    f_result = 0
    y_result = 0

    def __init__(self, g_result, f_result, y_result):
        self.g_result = g_result
        self.f_result = f_result
        self.y_result = y_result


lst_x = []
lst_a = []
lst_step = []
lst_g = []
lst_f = []
lst_y = []

x_st = float(input('Введите стартовое значение x >> '))  # Сбор данных
x_en = float(input('Введите конечное значение x >> '))
a_st = float(input('Введите начальное значение a >> '))
a_en = float(input('Введите конечное значение a >> '))
steps_count = int(input('Введите кол-во шагов >> '))
x_per_step = (x_en - x_st) / steps_count
a_per_step = (a_en - a_st) / steps_count

G = Args(x_st, x_en, a_st, a_en, steps_count, 'G')  # Объекты
F = Args(x_st, x_en, a_st, a_en, steps_count, "F")
Y = Args(x_st, x_en, a_st, a_en, steps_count, 'Y')

x = G.x_s
a = G.a_s
for i in range(G.steps):  # G
    x = G.x_s
    a = G.a_s
    num = 9 * (7 * a * a - 19 * a * x + 10 * x * x)  # Числитель
    den = 25 * a * a + 30 * a * x + 9 * x * x  # Знаменатель

    if den == 0:  # Если den == 0
        print('Ошибка! Знаменатель равен нулю.')
        exit()

    lst_step.append(i + 1)  # Добавить значения в списки
    lst_x.append(x)
    lst_a.append(a)
    lst_g.append(str(num / den))

    x += x_per_step
    a += a_per_step

for i in range(F.steps):  # F
    result = cos(9 * a * a - 13 * a * x - 10 * x * x)

    lst_step.append(i + 1)  # Добавить значения в списки
    lst_x.append(x)
    lst_a.append(a)
    lst_f.append(str(result))

    x += x_per_step
    a += a_per_step

for i in range(Y.steps):  # Y
    u_log = abs(-80 * a * a - 46 * a * x + 21 * x * x + 1)  # Подлогарифменное выражение

    result = log(u_log) / log(10)

    lst_step.append(i + 1)  # Добавить значения в списки
    lst_x.append(x)
    lst_a.append(a)
    lst_y.append(str(result))

    x += x_per_step
    a += a_per_step

Result = Results(lst_g[-1], lst_f[-1], lst_y[-1])

print(f'G = {Result.g_result}; F = {Result.f_result}; Y = {Result.y_result}')
