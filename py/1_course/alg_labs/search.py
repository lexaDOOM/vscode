import string, random, timeit
import matplotlib.pyplot as plt

# Стандартные константы для выполнения задачи
L3CACHE = 8
MINSIZE, STEP = L3CACHE * 2, L3CACHE * 2
MAXSIZE = L3CACHE * 20

# Счетчики операций для каждого алгоритма поиска
LINEAR_COUNT = 0
BINARY_COUNT = 0
NAIVE_COUNT = 0
KMP_COUNT = 0

# Массив для хранения результатов
results_array = []

# Функции для генерации входных данных

def generateIntArray(size):
    # Генерация массива случайных целых чисел заданного размера
    return [random.randint(0, 1000) for _ in range(size)]


def generateString(length):
    # Генерация строки случайных символов заданной длины
    return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

# Алгоритмы поиска в структурах данных


def linear_search(lys, element):  # Линейный поиск
    global LINEAR_COUNT
    for i in range(len(lys)):
        LINEAR_COUNT += 1
        if lys[i] == element:
            return i
    return -1


def binary_search(lys, val):  # Бинарный поиск
    global BINARY_COUNT
    first = 0
    last = len(lys) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        BINARY_COUNT += 1
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
        BINARY_COUNT += 1
    return index

# Алгоритмы поиска в строках
def naive_search(pattern, text):
    global NAIVE_COUNT
    # Получаем длины шаблона и текста
    m = len(pattern)
    n = len(text)

    # Цикл для смещения шаблона по тексту
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
            NAIVE_COUNT += 1
        NAIVE_COUNT += 1
        if j == m:
            return i


def KMP_search(pat, txt):
    global KMP_COUNT
    M = len(pat)
    N = len(txt)

    # Создание lps[] для хранения длины наибольшего префикса суффикса
    lps = [0] * M
    j = 0  # индекс для pat[]

    # Предварительная обработка шаблона (вычисление lps[] массива)
    computeLPSArray(pat, M, lps)

    i = 0  # индекс для txt[]
    while (N - i) >= (M - j):
        KMP_COUNT += 1
        if pat[j] == txt[i]:
            i += 1
            j += 1

        KMP_COUNT += 1
        if j == M:
            return i - j

        elif i < N and pat[j] != txt[i]:
            KMP_COUNT += 1
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def computeLPSArray(pat, M, lps):
    global KMP_COUNT
    len = 0  # длина предыдущего наибольшего префикса-суффикса

    lps[0] = 0  # lps[0] всегда 0
    i = 1

    # цикл для вычисления lps[i] для i = 1 до M-1
    while i < M:
        KMP_COUNT += 1
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            KMP_COUNT += 1
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


# Запуск тестов для различных размеров входных данных
for size in range(MINSIZE, MAXSIZE + 1, STEP):
    array = generateIntArray(size)
    text = generateString(size)

    search_value = random.randint(0, 1000)
    pattern = generateString(random.randint(1, 10))

    # Сброс счетчиков операций
    LINEAR_COUNT = 0
    BINARY_COUNT = 0
    NAIVE_COUNT = 0
    KMP_COUNT = 0

    # Измерение времени и подсчет операций для каждого алгоритма поиска
    print("Линейный    | ", "Размер массива:", size, "| Время:", timeit.timeit("linear_search(array, search_value)", setup="from __main__ import linear_search, array, search_value", number=1), "| Кол-во:", LINEAR_COUNT)
    print("Бинарный    | ", "Размер массива:", size, "| Время:", timeit.timeit("binary_search(array, search_value)", setup="from __main__ import binary_search, array, search_value", number=1), "| Кол-во:", BINARY_COUNT)
    print("Наивный     | ", "Размер массива:", size, "| Время:", timeit.timeit("naive_search(pattern, text)", setup="from __main__ import naive_search, text, pattern", number=1), "| Кол-во:", NAIVE_COUNT)
    print("КМП поиск       | ", "Размер массива:", size, "| Время:", timeit.timeit("KMP_search(pattern, text)", setup="from __main__ import KMP_search, text, pattern", number=1), "| Кол-во:", KMP_COUNT)

    # Сохранение результатов
    results_array.append((LINEAR_COUNT, BINARY_COUNT, NAIVE_COUNT, KMP_COUNT))

# Диапазон размеров данных для оси X
x = range(MINSIZE, MAXSIZE + 1, STEP)

# Построение графиков
plt.plot(x, [i[0] for i in results_array], label="Линейный")
plt.plot(x, [i[1] for i in results_array], label="Бинарный")
plt.plot(x, [i[2] for i in results_array], label="Наивный")
plt.plot(x, [i[3] for i in results_array], label="КМП поиск")
plt.ylabel("Количество операций")
plt.xlabel("Размер входных данных")
plt.ticklabel_format(axis="y", style="plain")
plt.legend()
plt.grid()
plt.show()
