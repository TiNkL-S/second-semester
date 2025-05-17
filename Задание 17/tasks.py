import time

# Задача 1: Алгоритм Голландского флага
def dutch_national_flag(arr):
    """
    Переставляет элементы массива так, чтобы сначала шли 0, затем 1, затем 2.
    Сложность: O(n)
    """
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# Задача 2: Лексикографическая сортировка (MSD Radix Sort)
def msd_radix_sort(strings, d=0):
    """
    Лексикографическая сортировка строк переменной длины.
    Сложность: O(mk), где m — количество строк, k — длина самой длинной строки.
    """
    if len(strings) <= 1:
        return strings

    buckets = {}
    for s in strings:
        char = s[d] if d < len(s) else ""  # Используем пустую строку как специальный символ
        if char not in buckets:
            buckets[char] = []
        buckets[char].append(s)

    sorted_strings = []
    for char in sorted(buckets.keys()):
        sorted_strings.extend(msd_radix_sort(buckets[char], d + 1))
    return sorted_strings

# Задача 3: Подсчёт количества уникальных чисел
def count_distinct(arr):
    """
    Считает количество уникальных чисел в массиве.
    Сложность: O(n log n)
    """
    arr.sort()  # Сортируем массив
    distinct_count = 1  # Первый элемент всегда уникален
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            distinct_count += 1
    return distinct_count

# Замер времени выполнения функции
def measure_time(func, *args, iterations=10):
    times = []
    for _ in range(iterations):
        start = time.time()
        func(*args)
        end = time.time()
        times.append(end - start)
    return sum(times) / len(times)

# Пример использования
if __name__ == "__main__":
    # Задача 1
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    avg_time_task1 = measure_time(dutch_national_flag, arr.copy())
    print(f"Исходный массив: {arr}")
    print(f"Отсортированный массив: {dutch_national_flag(arr)}")
    print(f"Среднее время работы задачи 1: {avg_time_task1:.6f} секунд")

    # Задача 2
    strings = ["ba", "abc", "ab", "b"]
    avg_time_task2 = measure_time(msd_radix_sort, strings)
    print(f"\nИсходные строки: {strings}")
    print(f"Отсортированные строки: {msd_radix_sort(strings)}")
    print(f"Среднее время работы задачи 2: {avg_time_task2:.6f} секунд")

    # Задача 3
    arr = [4, 2, 2, 8, 3, 3, 1, 4, 6, 7, 7, 8]
    avg_time_task3 = measure_time(count_distinct, arr.copy())
    print(f"\nИсходный массив: {arr}")
    print(f"Количество уникальных чисел: {count_distinct(arr)}")
    print(f"Среднее время работы задачи 3: {avg_time_task3:.6f} секунд")