import matplotlib.pyplot as plt
import random
import time

#  Списки для посторения зависимости времени от количества точек
time_elapsed, i_count = [], []

# Координаты точек
x_coordinate, y_coordinate = [], []

# Счётчик точек
k = 0

# Координаты искомых точек
x_matched, y_matched = [], []

# Задаём радиус поиска
try:
    r = int(input('Задайте радиус окрестности поиска >> '))

except ValueError:  # Защита от "дурака"
    print('Некорректные данные!')
    exit()

for n in range(0, 10000, 1000):

    i_count.append(1000 + n)  # Количество точек для итогового графика

    b_time = time.time()
    # Генерируем координаты точек
    for i in range(1000 + n):
        x_coordinate.append(random.randint(-1000 - n, 1000 + n))
        y_coordinate.append(random.randint(-1000 - n, 1000 + n))

        # Проверка точки на принадлежности к выбранной области
        if (r ** 2 >= ((x_coordinate[i] - x_coordinate[0]) ** 2) + ((y_coordinate[i] - y_coordinate[0]) ** 2)) and i > 0:
            x_matched.append(x_coordinate[i])
            y_matched.append(y_coordinate[i])
            k += 1

    time_elapsed.append(time.time() - b_time)  # Подсчёт затраченного времени

    print(x_coordinate[0], y_coordinate[0], k)

    """Реализация графика"""
    plt.grid()  # Сетка

    plt.gca().add_artist(plt.Circle((x_coordinate[0], y_coordinate[0]), r, facecolor='black'))  # Реализация эллипса

    plt.scatter(x_coordinate, y_coordinate, s=1, color='blue')  # Просто точки - обозначены синим
    plt.scatter(x_matched, y_matched, s=2, color='red')  # Искомые точки - обозначены красным
    plt.scatter(x_coordinate[0], y_coordinate[0], s=4,
                color='green')  # Центр области поиска (эллипса) - обозначена зелёным

    # Подписи осей
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()  # Вывод графика

    """Обнуление"""
    x_coordinate, y_coordinate, x_matched, y_matched = [], [], [], []

"""Итоговый график"""
plt.plot(i_count, time_elapsed, label='Зависимость времени поиска от количества точек', color='green')

# Подписи осей
plt.xlabel('Количество точек')
plt.ylabel('Затраченное время, с')

plt.grid()  # Сетка
plt.show()
