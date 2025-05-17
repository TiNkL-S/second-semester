import time

# Задача 1: Поиск нижнего и верхнего индексов числа в отсортированном массиве
def find_indices(arr, x):
    """
    Находит нижний и верхний индексы числа x в отсортированном массиве arr.
    Если число отсутствует, возвращает 0.
    Сложность: O(log n)
    """
    def lower_bound(arr, x):
        left, right = 0, len(arr) - 1
        lower = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                if arr[mid] == x:
                    lower = mid
                right = mid - 1
        return lower

    def upper_bound(arr, x):
        left, right = 0, len(arr) - 1
        upper = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > x:
                right = mid - 1
            else:
                if arr[mid] == x:
                    upper = mid
                left = mid + 1
        return upper

    lower = lower_bound(arr, x)
    upper = upper_bound(arr, x)
    return (lower, upper) if lower != -1 and upper != -1 else 0

# Задача 2: Поиск суммы, наиболее близкой к числу q
def closest_sum(x, y, q):
    """
    Находит пару чисел из массивов x и y, сумма которых наиболее близка к числу q.
    Сложность: O(k + l)
    """
    i, j = 0, len(y) - 1
    min_diff = float('inf')
    closest_sum = 0
    best_i, best_j = -1, -1

    while i < len(x) and j >= 0:
        s = x[i] + y[j]
        diff = abs(s - q)
        if diff < min_diff:
            min_diff = diff
            closest_sum = s
            best_i, best_j = i, j
        if s < q:
            i += 1
        else:
            j -= 1

    return x[best_i], y[best_j], closest_sum

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
    arr = [1, 2, 2, 2, 3, 4, 5]
    x = 2
    avg_time_task1 = measure_time(find_indices, arr, x)
    print(f"Индексы числа {x} в массиве: {find_indices(arr, x)}")
    print(f"Среднее время работы задачи 1: {avg_time_task1:.6f} секунд")

    # Задача 2
    x = [1, 4, 6, 9]
    y = [2, 3, 7, 10]
    q = 8
    avg_time_task2 = measure_time(closest_sum, x, y, q)
    result = closest_sum(x, y, q)
    print(f"Пара чисел с суммой, наиболее близкой к {q}: {result[:2]}, сумма: {result[2]}")
    print(f"Среднее время работы задачи 2: {avg_time_task2:.6f} секунд")