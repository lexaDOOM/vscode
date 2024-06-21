import random
import timeit
from collections import Counter
import matplotlib.pyplot as plt


# Самописный Counter
def my_counter(lst, is_sorted=False):
    return [
        (i, lst.count(i))
        for i in set(
            is_sorted and sorted(lst)
            or lst
        )
    ]


# Функция для генерации списка
def generate_lst(n, min=1, max=10):
    return [random.randint(min, max) for _ in range(n)]


def main(change_alph_size):
    alph_size = change_alph_size and [10, 100, 1000, 10000, 25000, 50000] or [10]

    lst_size_options = sorted(
        list(range(50000, 100001, 5000)) + [52500, 57500, 62500, 72500, 80500, 90500, 97000, 98000, 52000])

    time_results = []

    for size_index in range(0, len(alph_size)):
        for i in lst_size_options:
            print(f"\nРазмер алфавита входных данных: [1; {alph_size[size_index]}]")
            print(f"Размер списка: {i}")
            array = generate_lst(i, max=alph_size[size_index])
            sorted_array = sorted(array)

            counter_time_start = timeit.default_timer()
            _ = Counter(array)
            counter_time_end = timeit.default_timer()
            counter_time = counter_time_end - counter_time_start
            print(f"Counter                     | Время выполнения: {counter_time}")

            count_unique_time_start = timeit.default_timer()
            _ = my_counter(array)
            count_unique_time_end = timeit.default_timer()
            count_unique_time = count_unique_time_end - count_unique_time_start
            print(f"my_counter                | Время выполнения: {count_unique_time}")

            count_unique_time_sorted_start = timeit.default_timer()
            _ = my_counter(sorted_array)
            count_unique_time_sorted_end = timeit.default_timer()
            count_unique_time_sorted = count_unique_time_sorted_end - count_unique_time_sorted_start
            print(f"my_counter (сортированный)       | Время выполнения: {count_unique_time_sorted}")

            count_unique_time_sorted_st_start = timeit.default_timer()
            _ = my_counter(array, is_sorted=True)
            count_unique_time_sorted_st_end = timeit.default_timer()
            count_unique_time_sorted_st = count_unique_time_sorted_st_end - count_unique_time_sorted_st_start
            print(f"count_unique (sorted + st)  | Время выполнения: {count_unique_time_sorted_st}")

            time_results.append(
                (counter_time, count_unique_time, count_unique_time_sorted, count_unique_time_sorted_st))

        plt.plot(lst_size_options, [i[0] for i in time_results], label="Counter")
        plt.plot(lst_size_options, [i[1] for i in time_results], label="my_counter")
        plt.plot(lst_size_options, [i[2] for i in time_results], label="my_counter (сортированыый)")
        plt.plot(lst_size_options, [i[3] for i in time_results], label="my_counter (сортированный + сорт время)")
        plt.ylabel("Время выполнения")
        plt.xlabel("Размер списка")
        plt.title(f"Время выполнения с размером входных данных [1; {alph_size[size_index]}]")
        plt.grid()
        plt.legend()
        plt.show()
        time_results.clear()


if __name__ == "__main__":
    main(bool(int(input("Изменять размер алфавита входных данных (1 - да; 0 - нет)? >> "))))
    exit()
