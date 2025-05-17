def find_median_sorted_arrays(A, B):
    """
    Находит медиану двух отсортированных массивов.
    Сложность: O(log(min(n, m)))
    """
    if len(A) > len(B):
        A, B = B, A  # Убедимся, что A — меньший массив

    n, m = len(A), len(B)
    low, high = 0, n
    total_left = (n + m + 1) // 2

    while low <= high:
        i = (low + high) // 2  # Разбиение в A
        j = total_left - i  # Соответствующее разбиение в B

        # Границы разбиения
        A_left = float('-inf') if i == 0 else A[i - 1]
        A_right = float('inf') if i == n else A[i]
        B_left = float('-inf') if j == 0 else B[j - 1]
        B_right = float('inf') if j == m else B[j]

        # Проверка корректности разбиения
        if A_left <= B_right and B_left <= A_right:
            # Найдено правильное разбиение
            if (n + m) % 2 == 1:
                return max(A_left, B_left)  # Нечётное количество элементов
            else:
                return (max(A_left, B_left) + min(A_right, B_right)) / 2  # Чётное количество элементов
        elif A_left > B_right:
            high = i - 1  # Слишком много элементов из A, идём влево
        else:
            low = i + 1  # Слишком мало элементов из A, идём вправо

# Замер времени выполнения функции
import time

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
    A = [1, 3, 8]
    B = [7, 9, 10, 11]
    avg_time = measure_time(find_median_sorted_arrays, A, B)
    print(f"Медиана массивов {A} и {B}: {find_median_sorted_arrays(A, B)}")
    print(f"Среднее время работы: {avg_time:.6f} секунд")