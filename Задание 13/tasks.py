import time

# Задача 1: Найти пропущенное число
def find_missing_number(arr, n):
    """
    Находит пропущенное число в массиве, содержащем числа от 0 до n.
    Сложность: O(n)
    """
    total_sum = n * (n + 1) // 2  # Сумма всех чисел от 0 до n
    actual_sum = sum(arr)  # Сумма элементов массива
    return total_sum - actual_sum

# Задача 2: Найти индекс точки "перелома"
def find_pivot_index(arr):
    """
    Находит индекс точки "перелома" в массиве, где убывание сменяется на возрастание.
    Сложность: O(log n)
    """
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            left = mid + 1  # Мы в убывающей части, идем вправо
        else:
            right = mid  # Мы в возрастающей части, идем влево
    return left

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
    arr = [0, 1, 2, 4, 5]  # Пример массива
    n = 5  # Диапазон чисел от 0 до n
    avg_time_task1 = measure_time(find_missing_number, arr, n)
    print(f"Пропущенное число: {find_missing_number(arr, n)}")
    print(f"Среднее время работы задачи 1: {avg_time_task1:.6f} секунд")

    # Задача 2
    arr = [9, 7, 5, 3, 4, 6, 8]  # Пример массива
    avg_time_task2 = measure_time(find_pivot_index, arr)
    print(f"Индекс точки 'перелома': {find_pivot_index(arr)}")
    print(f"Среднее время работы задачи 2: {avg_time_task2:.6f} секунд")