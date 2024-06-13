from math import *
x_s = float(input('Введите стартовое значение x >> '))  # Сбор данных
x = x_s
x_e = float(input('Введите конечное значение x >> '))
a_s = float(input('Введите начальное значение a >> '))
a = a_s
a_e = float(input('Введите конечное значение a >> '))
steps = int(input('Введите кол-во шагов >> '))
fx = int(input('Выберете ф-кицю:\n1 - G\n2 - F\n3 - Y\n>> '))
x_per_step = (x_e - x_s) / steps
a_per_step = (a_e - a_s) / steps
st = ''  # Строка

lst_x = []  # Списки
lst_a = []
lst_fx = []
lst_step = []

if steps <= 0:
    print('Ошибка! Кол-во шагов - натуральное число')
    exit()

if fx == 1:  # G
    f_x = 'G'
    for i in range(steps):
        num = 9 * (7 * a * a - 19 * a * x + 10 * x * x)  # Числитель
        den = 25 * a * a + 30 * a * x + 9 * x * x  # Знаменатель

        if den == 0:  # Если den == 0
            print('Ошибка! Знаменатель равен нулю.')
            exit()

        lst_step.append(i + 1)  # Добавить значения в списки
        lst_x.append(x)
        lst_a.append(a)
        lst_fx.append(str(num / den))

        x += x_per_step
        a += a_per_step

elif fx == 2:  # F
    f_x = 'F'
    for i in range(steps):
        result = cos(9 * a * a - 13 * a * x - 10 * x * x)

        lst_step.append(i + 1)  # Добавить значения в списки
        lst_x.append(x)
        lst_a.append(a)
        lst_fx.append(str(result))

        x += x_per_step
        a += a_per_step

elif fx == 3:  # Y
    f_x = 'Y'
    for i in range(steps):
        u_log = -80 * a * a - 46 * a * x + 21 * x * x + 1  # Подлогарифменное выражение

        if u_log <= 0:  # Если u_log <= 0
            print('Ошибка! Подлогарифменное выражение <= 0')
            exit()

        result = log(u_log) / log(10)

        lst_step.append(i + 1)  # Добавить значения в списки
        lst_x.append(x)
        lst_a.append(a)
        lst_fx.append(str(result))

        x += x_per_step
        a += a_per_step

else:
    print('Ошибка! Такой функции нет!')
    exit()

for i in range(steps):  # Заполение строки элементами списка
    st = st.join(lst_fx[i]).replace('.', '')

sample = input('Введите шаблон >> ')  # Поиск кол-ва совпадений по шаблону
print('Кол-во совпадений:', st.count(sample))
