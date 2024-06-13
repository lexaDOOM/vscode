import math
import random
import time
import matplotlib.pyplot as plt

op_count = 0
in_count = 0


def shaker_sort(lst):  # Сортировка перемешиванием
    global op_count
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
                op_count += 1
                swapped = True

        if not swapped:  # если без обменов, то
            break  # прерываем цикл

        swapped = False

        e_index -= 1

        #  СПРАВА НАЛЕВО
        for i in range(e_index - 1, b_index - 1, -1):
            if lst[i] > lst[i + 1]:  # Если lst[i] > lst[i + 1], то
                lst[i], lst[i + 1] = lst[i + 1], lst[i]  # Меняем их местами
                op_count += 1
                swapped = True

        b_index += 1

    return lst


def shell_sort(lst):  # Сортировка Шелла
    global op_count
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
                op_count += 1
                j -= step  # Переходим к следующему элементу с шагом назад
            lst[j] = temp  # Вставляем запомненный элемент на своё место
            op_count += 1

        step //= 2  # Уменьшаем шаг в два раза

    return lst  # Возвращаем отсортированный список


def heapify(lst, n, i):
    global op_count
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
        op_count += 1
        # Рекурсивно heapify поддерево
        heapify(lst, n, largest)


def heap_sort(lst):  # Пирамидальная сортировка
    global op_count
    global in_count
    n = len(lst)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]  # Меняем текущий корень с последним элементом
        op_count += 1
        in_count += 1
        heapify(lst, i, 0)  # Вызываем heapify на уменьшенной куче

    return lst


def introsort(arr):  # Интросорт
    # Определяем максимальную глубину рекурсии как удвоенный логарифм по основанию 2 от длины массива.
    max_depth = int(2 * math.log2(len(arr)))
    # Вызываем вспомогательную функцию _introsort для начала сортировки.
    _introsort(arr, 0, len(arr) - 1, max_depth)
    return arr


def _introsort(arr, start, end, max_depth):
    global in_count
    if start < end:
        if max_depth == 0:
            # Если достигли максимальной глубины рекурсии, переключаемся на пирамидальную сортировку.
            heap_sort(arr)
            in_count += 1
        else:
            # Выполняем быструю сортировку и получаем индекс разделения.
            p = partition(arr, start, end)
            in_count += 1
            # Рекурсивно сортируем левую и правую части массива, уменьшая допустимую глубину рекурсии.
            _introsort(arr, start, p - 1, max_depth - 1)
            _introsort(arr, p + 1, end, max_depth - 1)


def partition(arr, low, high):
    global in_count
    pivot = arr[high]  # Определяем опорный элемент как последний элемент текущего подмассива.
    i = low - 1  # Индекс меньшего элемента.
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1  # Увеличиваем индекс меньшего элемента.
            arr[i], arr[j] = arr[j], arr[i]  # Меняем местами элементы.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Ставим опорный элемент на правильное место.
    return i + 1  # Возвращаем индекс опорного элемента.

# Проверка устойчивости сортировки


def is_stable(sort_func):  # Функция проверки алгоритмов на устойчивость
    class Item:
        def __init__(self, value, original_index):
            self.value = value
            self.original_index = original_index

        def __lt__(self, other):
            return self.value < other.value

        def __le__(self, other):
            return self.value <= other.value

        def __eq__(self, other):
            return self.value == other.value and self.original_index == other.original_index

        def __repr__(self):
            return f"Item({self.value}, {self.original_index})"

    items = [Item(3, 1), Item(1, 2), Item(3, 2), Item(2, 3)]
    sorted_items = sort_func(items.copy())
    return sorted_items == sorted(items, key=lambda x: x.value)

# Основная функция для исследования


def main():  # Основная
    global op_count
    global in_count
    lengths = [50, 500, 1000, 5000, 15000]

    # Списки для построения графиков
    pl_shaker_ops, pl_shell_ops, pl_heap_ops, pl_introsort_ops = [], [], [], []
    pl_shaker_size, pl_shell_size, pl_heap_size, pl_introsort_size = [], [], [], []

    for length in lengths:
        print(f"Длина списка: {length}")

        """Сортировка перемешиванием"""
        arr = [random.randint(0, 100) for _ in range(length)]
        start_time = time.time()  # Время начала сортировки
        shaker_sort(arr.copy())
        total_time = time.time() - start_time  # Итоговое время сортировки

        # Заполнение списков для построения графиков
        pl_shaker_ops.append(op_count)
        pl_shaker_size.append(length)

        print(f"Сортировка перемешиванием: Операций: {op_count}, Время работы: {total_time:.8f}")
        print(f"Устойчива - {'ДА' if is_stable(shaker_sort) else 'НЕТ'}")

        """Сортировка Шелла"""
        op_count = 0
        arr = [random.randint(0, 100) for _ in range(length)]
        start_time = time.time()  # Время начала сортировки
        shell_sort(arr.copy())
        total_time = time.time() - start_time  # Итоговое время сортировки

        # Заполнение списков для построения графиков
        pl_shell_ops.append(op_count)
        pl_shell_size.append(length)

        print(f"Сортировка Шелла: Операций: {op_count}, Время работы: {total_time:.8f}")
        print(f"Устойчива - {'ДА' if is_stable(shell_sort) else 'НЕТ'}")

        """Пирамидальная сортировка"""
        op_count = 0
        arr = [random.randint(0, 100) for _ in range(length)]
        start_time = time.time()  # Время начала сортировки
        heap_sort(arr.copy())
        total_time = time.time() - start_time  # Итоговое время сортировки

        # Заполнение списков для построения графиков
        pl_heap_ops.append(op_count)
        pl_heap_size.append(length)

        print(f"Пирамидальная сортировка: Операций: {op_count}, Время работы: {total_time:.8f}")
        print(f"Устойчива - {'ДА' if is_stable(heap_sort) else 'НЕТ'}")

        """Интросорт"""
        op_count = 0
        in_count = 0
        arr = [random.randint(0, 100) for _ in range(length)]
        start_time = time.time()  # Время начала сортировки
        introsort(arr.copy())
        total_time = time.time() - start_time  # Итоговое время сортировки

        # Заполнение списков для построения графиков
        pl_introsort_ops.append(in_count)
        pl_introsort_size.append(length)

        print(f"Интросорт: Операций: {in_count}, Время работы: {total_time:.8f}")
        print(f"Устойчива - {'ДА' if is_stable(introsort) else 'НЕТ'}")

        print("")

    """Графики зависимостей кол-ва операций от размеров списков"""
    # Перемешиванием
    plt.plot(pl_shaker_size, pl_shaker_ops, label='Перемешиванием', color='yellow')
    plt.title('Сортировка перемешиванием')
    plt.xlabel('Размер списка')
    plt.ylabel('Кол-во операций')
    plt.grid()
    plt.legend()
    plt.show()
    # Шелла
    plt.plot(pl_shell_size, pl_shell_ops, label='Шелла', color='green')
    plt.title('Сортировка Шелла')
    plt.xlabel('Размер списка')
    plt.ylabel('Кол-во операций')
    plt.grid()
    plt.legend()
    plt.show()
    # Пирамидальная
    plt.plot(pl_heap_size, pl_heap_ops, label='Пирамидальная', color='blue')
    plt.title('Пирамидальная сортировка')
    plt.xlabel('Размер списка')
    plt.ylabel('Кол-во операций')
    plt.grid()
    plt.legend()
    plt.show()
    # Интросорт
    plt.plot(pl_introsort_size, pl_introsort_ops, label='Интросорт', color='red')
    plt.title('Интроспективная сортировка')
    plt.xlabel('Размер списка')
    plt.ylabel('Кол-во операций')
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
