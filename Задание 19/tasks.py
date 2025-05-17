import time
from bisect import bisect_left

# Задача 1: Максимальная длина возрастающей подпоследовательности
def lis_length(arr):
    """
    Находит длину наибольшей возрастающей подпоследовательности.
    Сложность: O(n log n)
    """
    tails = []
    for x in arr:
        pos = bisect_left(tails, x)  # Бинарный поиск позиции для x
        if pos == len(tails):
            tails.append(x)  # Добавляем новый "хвост"
        else:
            tails[pos] = x  # Заменяем существующий "хвост"
    return len(tails)

# Задача 2: Поразрядная сортировка по битам
def radix_sort_bits(arr, k):
    """
    Сортирует массив чисел по битам.
    Сложность: O(nk)
    """
    for i in range(k):  # Для каждого бита
        zeros, ones = [], []
        for num in arr:
            if (num >> i) & 1 == 0:  # Проверяем i-й бит
                zeros.append(num)
            else:
                ones.append(num)
        arr = zeros + ones  # Объединяем элементы с битом 0 и 1
    return arr

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
    arr = [3, 1, 2, 1, 8, 5, 6]
    avg_time_task1 = measure_time(lis_length, arr)
    print(f"Длина LIS: {lis_length(arr)}")
    print(f"Среднее время работы задачи 1: {avg_time_task1:.6f} секунд")

    # Задача 2
    arr = [3, 6, 2, 8, 5, 1]
    k = 4  # Количество бит (например, для чисел от 0 до 15)
    avg_time_task2 = measure_time(radix_sort_bits, arr, k)
    print(f"Отсортированный массив: {radix_sort_bits(arr, k)}")
    print(f"Среднее время работы задачи 2: {avg_time_task2:.6f} секунд")