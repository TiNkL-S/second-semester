import time

# Задача 1: Количество общих элементов в двух отсортированных массивах
def count_common_elements(x, y):
    """
    Находит количество общих элементов в двух отсортированных массивах.
    Сложность: O(k + l)
    """
    i, j, count = 0, 0, 0
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            i += 1
        elif x[i] > y[j]:
            j += 1
        else:
            count += 1
            i += 1
            j += 1
    return count

# Задача 2: Найти общее число в трёх отсортированных массивах
def find_common_element(x, y, z):
    """
    Находит общее число в трёх отсортированных массивах.
    Сложность: O(p + q + r)
    """
    i, j, k = 0, 0, 0
    while i < len(x) and j < len(y) and k < len(z):
        if x[i] == y[j] == z[k]:
            return x[i]
        m = min(x[i], y[j], z[k])
        if x[i] == m:
            i += 1
        if y[j] == m:
            j += 1
        if z[k] == m:
            k += 1
    return None

# Задача 3: Максимальное число из перестановки массива
def max_number(arr):
    """
    Формирует максимальное число из перестановки массива.
    Сложность: O(n log n)
    """
    from functools import cmp_to_key

    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0

    str_arr = list(map(str, arr))
    str_arr.sort(key=cmp_to_key(compare))
    result = ''.join(str_arr)
    return result if result[0] != '0' else '0'

# Задача 4: Суммы квадратов m x m в таблице
def compute_prefix_sums(a, n):
    """
    Вычисляет префиксные суммы для матрицы.
    Сложность: O(n^2)
    """
    P = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            P[i][j] = a[i - 1][j - 1] + P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1]
    return P

def sum_squares(a, n, m):
    """
    Вычисляет суммы всех квадратов m x m в таблице.
    Сложность: O(n^2)
    """
    P = compute_prefix_sums(a, n)
    result = []
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            total = P[i + m][j + m] - P[i][j + m] - P[i + m][j] + P[i][j]
            result.append(total)
    return result

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
    x = [1, 2, 3, 4, 5]
    y = [3, 4, 5, 6, 7]
    avg_time_task1 = measure_time(count_common_elements, x, y)
    print(f"Количество общих элементов: {count_common_elements(x, y)}")
    print(f"Среднее время работы задачи 1: {avg_time_task1:.6f} секунд")

    # Задача 2
    x = [1, 2, 3, 4, 5]
    y = [3, 4, 5, 6, 7]
    z = [5, 6, 7, 8, 9]
    avg_time_task2 = measure_time(find_common_element, x, y, z)
    print(f"Общее число в трёх массивах: {find_common_element(x, y, z)}")
    print(f"Среднее время работы задачи 2: {avg_time_task2:.6f} секунд")

    # Задача 3
    arr = [3, 30, 34, 5, 9]
    avg_time_task3 = measure_time(max_number, arr)
    print(f"Максимальное число: {max_number(arr)}")
    print(f"Среднее время работы задачи 3: {avg_time_task3:.6f} секунд")

    # Задача 4
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    n = 3
    m = 2
    avg_time_task4 = measure_time(sum_squares, a, n, m)
    print(f"Суммы квадратов {m}x{m}: {sum_squares(a, n, m)}")
    print(f"Среднее время работы задачи 4: {avg_time_task4:.6f} секунд")