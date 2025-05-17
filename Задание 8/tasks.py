import time
import math
import matplotlib.pyplot as plt

# 1. Округление вниз до ближайшего целого значения квадратного корня числа x
def floor_sqrt(x):
    """
    Вычисление квадратного корня числа x, округленного вниз, за O(log x).
    """
    if x < 0:
        raise ValueError("x должно быть неотрицательным")
    if x == 0 or x == 1:
        return x

    low, high = 0, x
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            low = mid + 1
            result = mid
        else:
            high = mid - 1
    return result

# 2. Подсчет количества испорченных плиток
def damaged_tiles(n, m):
    """
    Подсчет количества испорченных плиток на полу размером N x M.
    Сложность O(log max(N, M)).
    """
    return n + m - math.gcd(n, m)

# 3. НОД с помощью алгоритма Евклида
def gcd(a, b):
    """
    Нахождение НОД двух чисел с использованием алгоритма Евклида.
    """
    while b != 0:
        a, b = b, a % b
    return a

# Замер времени выполнения функции
def measure_time(func, *args, iterations=10):
    times = []
    for _ in range(iterations):
        start = time.time()
        func(*args)
        end = time.time()
        times.append(end - start)
    return min(times), max(times), sum(times) / len(times)

# Построение графиков
def plot_results(results, title, xlabel, ylabel):
    x = [r[0] for r in results]
    y_min = [r[1] for r in results]
    y_max = [r[2] for r in results]
    y_avg = [r[3] for r in results]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y_min, label="Min Time", marker="o")
    plt.plot(x, y_max, label="Max Time", marker="o")
    plt.plot(x, y_avg, label="Average Time", marker="o")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

# Генерация данных и выполнение замеров
def main():
    # Тестирование функции floor_sqrt
    results_sqrt = []
    for x in range(1, 1_000_001, 100_000):
        results_sqrt.append((x, *measure_time(floor_sqrt, x)))
    plot_results(results_sqrt, "Floor Square Root", "Input (x)", "Time (s)")

    # Тестирование функции damaged_tiles
    results_tiles = []
    for n in range(1, 1_001, 100):
        m = n * 2  # Пример: m в 2 раза больше n
        results_tiles.append((n, *measure_time(damaged_tiles, n, m)))
    plot_results(results_tiles, "Damaged Tiles", "Input (N)", "Time (s)")

    # Тестирование функции gcd
    results_gcd = []
    for a in range(1, 1_000_001, 100_000):
        b = a // 2  # Пример: b в 2 раза меньше a
        results_gcd.append((a, *measure_time(gcd, a, b)))
    plot_results(results_gcd, "GCD (Euclid's Algorithm)", "Input (a)", "Time (s)")

if __name__ == "__main__":
    main()