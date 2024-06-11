# Импорт алгоритмов
from sort_defs import shaker_sort, shell_sort, heap_sort, introsort

#  Неотсортированные списки
lst_sort_test = [[8, 3, 1, 9, 4, 2, 5, 7, 6, 0], [-8, -3, -1, -9, -4, -2, -5, -7, -6, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [8, 8, 8, 8, 8, 8, 8, 8, 8, 8], [8.3, 1.9, 4.2, 5.7, 6, 0.9, 6.8, 7.7, 5.6, 2.5]]

#  Отсортированный список для проверки
lst_sorted = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [8, 8, 8, 8, 8, 8, 8, 8, 8, 8], [0.9, 1.9, 2.5, 4.2, 5.6, 5.7, 6, 6.8, 7.7, 8.3]]

for i in range(len(lst_sort_test)):  # Проверка алгоритмов
    print(f'Исходный список | {lst_sort_test[i]}')
    shaker = shaker_sort(lst_sort_test[i])
    shell = shell_sort(lst_sort_test[i])
    heap = heap_sort(lst_sort_test[i])
    isort = introsort(lst_sort_test[i])
    print(f'Сорт. перемеш.  | {shaker} - {("ВЕРНО" if shaker == lst_sorted[i] else "НЕВЕРНО")}')
    print(f'Сорт. Шелла     | {shell} - {("ВЕРНО" if shaker == lst_sorted[i] else "НЕВЕРНО")}')
    print(f'Пирамид. сорт.  | {heap} - {("ВЕРНО" if shaker == lst_sorted[i] else "НЕВЕРНО")}')
    print(f'Интросорт       | {isort} - {("ВЕРНО" if shaker == lst_sorted[i] else "НЕВЕРНО")}')
    print('--------------------------------------------------')
