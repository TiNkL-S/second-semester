import time
import matplotlib.pyplot as plt

# 1. Подсчет количества вхождений числа a среди чисел (b * c) mod p
def count_occurrences(b, p, a, d):
    """
    Определяет, сколько раз число a встречается среди чисел (b * c) mod p
    для всех c в интервале 0 < c <= d. Сложность O(p).
    """
    count = 0
    for c in range(1, d + 1):
        if (b * c) % p == a:
            count += 1
    return count

# 2. Генерация кодов Грея длины N
def gray_code(n):
    """
    Генерация кодов Грея для векторов длины N.
    """
    if n == 0:
        return ["0"]
    if n == 1:
        return ["0", "1"]

    # Рекурсивное построение
    prev_gray = gray_code(n - 1)
    result = []

    # Добавляем 0 к началу предыдущих кодов
    for code in prev_gray:
        result.append("0" + code)

    # Добавляем 1 к началу предыдущих кодов в обратном порядке
    for code in reversed(prev_gray):
        result.append("1" + code)

    return result

# 3. Округление вниз до ближайшего целого значения квадратного корня числа x
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
    # Тестирование функции count_occurrences
    results_occurrences = []
    b, p, a = 3, 7, 2
    for d in range(1, 1_001, 100):
        results_occurrences.append((d, *measure_time(count_occurrences, b, p, a, d)))
    plot_results(results_occurrences, "Count Occurrences", "Input (d)", "Time (s)")

    # Тестирование функции gray_code
    results_gray = []
    for n in range(1, 13):  # Ограничиваем длину векторов для тестирования
        results_gray.append((n, *measure_time(gray_code, n)))
    plot_results(results_gray, "Gray Code Generation", "Input (n)", "Time (s)")

    # Тестирование функции floor_sqrt
    results_sqrt = []
    for x in range(1, 1_000_001, 100_000):
        results_sqrt.append((x, *measure_time(floor_sqrt, x)))
    plot_results(results_sqrt, "Floor Square Root", "Input (x)", "Time (s)")

if __name__ == "__main__":
    main()