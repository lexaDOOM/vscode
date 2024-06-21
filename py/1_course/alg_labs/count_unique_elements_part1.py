import random
import timeit
from collections import Counter
from multiprocessing.dummy import Pool as ThreadPool
import matplotlib.pyplot as plt

THREADS_POOL = 100


# Самописная функция Counter
def my_counter(array):
    count_lst = []
    dct_lst = []
    result = []
    for i in array:
        if i not in dct_lst:
            dct_lst.append(i)
            count_lst.append(array.count(i))
    for i in range(len(dct_lst)):
        result.append(f'{dct_lst[i]}:{count_lst[i]}')
    return result


# Функция для генерации списка
def generate_lst(n, min=1, max=10):
    return [random.randint(min, max) for _ in range(n)]


"""Задание 1"""
def task1():
    choice = int(input("Выберите задачу (1 или 2): "))
    if choice == 1:
        # Задача 1.1
        lst = [int(input("Введите число: ")) for _ in range(10)]
        print("Результат: ", sorted(Counter(lst).items(), key=lambda x: x[0]))
    elif choice == 2:
        # Задача 1.2
        array_len = int(input("Введите длину массива: "))
        lst = generate_lst(array_len, 1, 999)
        print(f"Сгенерированный массив из {array_len} элементов: ", lst)
        print("Результат: ", my_counter(lst))
    else:
        print("Неправильная команда")
    exit()


"""Задание 2"""
def task2():
    print("\nВнимание! Данное задание выполняется в многопоточном режиме\n")

    choice = int(input(
        "1) n = 10**3; 10**4; 10**5 и 10**6 \
        \n2) n от 10**5 до 10**6 с шагом 25000 \
        \nВыберите вариант подсчетов: "
    ))

    if choice not in [1, 2]:
        print("Неправильная команда")
        exit()

    # Константы для обозначения границ размеров массива тестовых значений
    MIN_SIZE = choice == 1 and 3 or 10 ** 5
    MAX_SIZE = choice == 1 and 6 or 10 ** 6
    STEP = choice == 1 and 1 or 25000

    """обозначения:"""
    # cu = my_counter - Самописная функция
    # cc = collections.Counter - Встроенная функция

    # Списки для хранения времени выполнения функций
    # для последующего вывода в графике
    timelst_cu = []
    timelst_cc = []

    for i in range(MIN_SIZE, MAX_SIZE + 1, STEP):
        print(f"\nРазмер списка: {choice == 1 and 10 ** i or i}")
        lst = generate_lst(choice == 1 and 10 ** i or i)

        # Использование многопоточности
        pool = ThreadPool(THREADS_POOL)

        # Расчет времени выполнения самописной функции
        start_cu = timeit.default_timer()
        cu_result = pool.map(my_counter, [lst])
        end_cu = timeit.default_timer()
        timelst_cu.append(end_cu - start_cu)

        # Расчет времени выполнения стандартной функции
        start_cc = timeit.default_timer()
        cc_result = pool.map(Counter, [lst])
        end_cc = timeit.default_timer()
        timelst_cc.append(end_cc - start_cc)

        print(f"Время выполнения самописной функции (my_counter): {end_cu - start_cu}; Результат: {cu_result[0]}")
        print(
            f"Время выполнения стандартной функции (collections.Counter): {end_cc - start_cc}; Результат: {list(cc_result[0].items())}")

        # Очистка массивов результата выполнения функции,
        # Закрытие и переоткрытие пула для процессов на многопоточности
        cu_result.clear()
        cc_result.clear()
        pool.close()
        pool.join()

    # Создание списка координат оси Ох
    x = [
        choice == 1 and 10 ** i or i
        for i in range(MIN_SIZE, MAX_SIZE + 1, STEP)
    ]

    """график"""
    # Объявление координат двух прямых на графике
    plt.plot(x, timelst_cu, label="my_counter")
    plt.plot(x, timelst_cc, label="Counter")

    # Названия для координатных осей
    plt.xlabel("Размер массива")
    plt.ylabel("Время выполнения функции")

    # Легенда
    plt.legend()

    # Переключение отображения позиций на оси Ox
    # 0.2 * 1e6 -> 200000
    plt.ticklabel_format(axis="x", style="plain")

    # Отображение графика и выход из программы
    plt.show()
    exit()


"""Основная функция программы"""
if __name__ == "__main__":
    taskChoice = int(input("Выберите задание (1 или 2): "))
    if taskChoice == 1:
        task1()
    elif taskChoice == 2:
        task2()
    else:
        print("Неправильная команда")
        exit()
