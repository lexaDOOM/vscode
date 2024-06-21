import random
import timeit
import matplotlib.pyplot as plt

# Несколько констант для удобства
L3CACHE = 8
MINSIZE = L3CACHE * 2
STEP = L3CACHE * 2
MAXSIZE = L3CACHE * 20

# Счётчики операций
bubbleCount = 0
insertionCount = 0
shellCount = 0
quickCount = 0

resultsArray = []


def bubbleSort(arr):  # Пузырьковая сортировка
    global bubbleCount
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                bubbleCount += 1


def insertionSort(arr):  # Сортировка вставками
    global insertionCount
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        insertionCount += 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            insertionCount += 1
        arr[j + 1] = key


def shellSort(arr):  # Сортировка Шелла
    global shellCount
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                shellCount += 1
                j -= gap
            arr[j] = temp
            shellCount += 1
        gap //= 2


def quickSort(array):  # Быстрая сортировка
    global quickCount
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[random.randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    quickCount += len(low) + len(high) + 1
    return quickSort(low) + same + quickSort(high)
    

for arraySize in range(MINSIZE, MAXSIZE+1, STEP):  # Основной цикл программы
    array = [random.randint(0, 1000) for _ in range(arraySize)]
    bubbleCount = 0
    insertionCount = 0
    shellCount = 0
    quickCount = 0
    bSortTime = timeit.timeit("bubbleSort(array)", setup="from __main__ import bubbleSort, array", number=1)
    iSortTime = timeit.timeit("insertionSort(array)", setup="from __main__ import insertionSort, array", number=1)
    sSortTime = timeit.timeit("shellSort(array)", setup="from __main__ import shellSort, array", number=1)
    qSortTime = timeit.timeit("quickSort(array)", setup="from __main__ import quickSort, array", number=1)
    print("Bubble sort    | ", "Array size:", arraySize, "| Time:", bSortTime, "| Count:", bubbleCount)
    print("Insertion sort | ", "Array size:", arraySize, "| Time:", iSortTime, "| Count:", insertionCount)
    print("Shell sort     | ", "Array size:", arraySize, "| Time:", sSortTime, "| Count:", shellCount)
    print("Quick sort     | ", "Array size:", arraySize, "| Time:", qSortTime, "| Count:", quickCount)
    resultsArray.append((bubbleCount, insertionCount, shellCount, quickCount))

x = range(MINSIZE, MAXSIZE+1, STEP)

# График
plt.plot(x, [i[0] for i in resultsArray], label="Bubble sort")
plt.plot(x, [i[1] for i in resultsArray], label="Insertion sort")
plt.plot(x, [i[2] for i in resultsArray], label="Shell sort")
plt.plot(x, [i[3] for i in resultsArray], label="Quick sort")
plt.title("Количество операций, выполняемых алгоримами сортировки")
plt.ylabel("Количество операций")
plt.xlabel("Размер массива")
plt.ticklabel_format(axis="y", style="plain")
plt.legend()
plt.grid()
plt.show()
