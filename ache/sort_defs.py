import math


def shaker_sort(lst):  # Сортировка перемешиванием
    length = len(lst)
    b_index = 0
    e_index = length - 1
    swapped = True

    while swapped:
        swapped = False

        #  СЛЕВА НАПРАВО
        for i in range(b_index, e_index):
            if lst[i] > lst[i + 1]:  # Если lst[i] > lst[i + 1], то
                lst[i], lst[i + 1] = lst[i + 1], lst[i]  # Меняет их местами
                swapped = True

        if not swapped:  # если без обменов, то
            break  # прерываем цисл

        swapped = False

        e_index -= 1

        #  СПРАВА НАЛЕВО
        for i in range(e_index - 1, b_index - 1, -1):
            if lst[i] > lst[i + 1]:  # Если lst[i] > lst[i + 1], то
                lst[i], lst[i + 1] = lst[i + 1], lst[i]  # Меняем их местами
                swapped = True

        b_index += 1

    return lst


def shell_sort(lst):
    last_index = len(lst)  # Определяем длину списка
    step = last_index // 2  # Начальный шаг сортировки
    # Основной цикл продолжается до тех пор, пока шаг больше 0
    while step > 0:
        # Проходим по элементам списка, начиная с индекса, равного шагу, до конца списка
        for i in range(step, last_index):
            temp = lst[i]  # Запоминаем текущий элемент
            j = i  # Индекс для внутреннего цикла
            # Внутренний цикл для перемещения элементов с текущим шагом
            while j >= step and lst[j - step] > temp:
                lst[j] = lst[j - step]  # Перемещаем элемент на шаг вперёд
                j -= step  # Переходим к следующему элементу с шагом назад
            lst[j] = temp  # Вставляем запомненный элемент на своё место
        step //= 2  # Уменьшаем шаг в два раза
    return lst  # Возвращаем отсортированный список


def heapify(lst, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    left = 2 * i + 1  # Левый дочерний элемент
    right = 2 * i + 2  # Правый дочерний элемент

    # Если левый дочерний элемент больше корня
    if left < n and lst[left] > lst[largest]:
        largest = left

    # Если правый дочерний элемент больше, чем самый большой элемент на данный момент
    if right < n and lst[right] > lst[largest]:
        largest = right

    # Если самый большой элемент не корень
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]  # Меняем местами

        # Рекурсивно heapify поддерево
        heapify(lst, n, largest)


def heap_sort(lst):
    n = len(lst)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]  # Меняем текущий корень с последним элементом
        heapify(lst, i, 0)  # Вызываем heapify на уменьшенной куче

    return lst


def introsort(arr):
    # Определяем максимальную глубину рекурсии как удвоенный логарифм по основанию 2 от длины массива.
    max_depth = int(2 * math.log2(len(arr)))
    # Вызываем вспомогательную функцию _introsort для начала сортировки.
    _introsort(arr, 0, len(arr) - 1, max_depth)
    return arr


def _introsort(arr, start, end, max_depth):

    if start < end:
        if max_depth == 0:
            # Если достигли максимальной глубины рекурсии, переключаемся на пирамидальную сортировку.
            heap_sort(arr)
        else:
            # Выполняем быструю сортировку и получаем индекс разделения.
            p = partition(arr, start, end)
            # Рекурсивно сортируем левую и правую части массива, уменьшая допустимую глубину рекурсии.
            _introsort(arr, start, p - 1, max_depth - 1)
            _introsort(arr, p + 1, end, max_depth - 1)


def partition(arr, low, high):
    
    pivot = arr[high]  # Определяем опорный элемент как последний элемент текущего подмассива.
    i = low - 1  # Индекс меньшего элемента.
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1  # Увеличиваем индекс меньшего элемента.
            arr[i], arr[j] = arr[j], arr[i]  # Меняем местами элементы.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Ставим опорный элемент на правильное место.
    return i + 1  # Возвращаем индекс опорного элемента.


