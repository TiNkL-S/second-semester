import time
import random
import math
import matplotlib.pyplot as plt
from collections import Counter

# Реализация алгоритма Евклида (вычитание)
def gcd_subtraction(a, b):
    while b != 0:
        if a < b:
            a, b = b, a
        a = a - b
    return a

# Реализация алгоритма Евклида (остаток от деления)
def gcd_mod(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Реализация НОД через разложение на множители
def gcd_prime_factors(a, b):
    def prime_factors(n):
        factors = []
        for i in range(2, int(math.sqrt(n)) + 1):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n > 1:
            factors.append(n)
        return factors

    factors_a = Counter(prime_factors(a))
    factors_b = Counter(prime_factors(b))
    common_factors = factors_a & factors_b
    gcd = 1
    for factor, count in common_factors.items():
        gcd *= factor ** count
    return gcd

# Замер времени выполнения функции
def measure_time(func, a, b, iterations=10):
    times = []
    for _ in range(iterations):
        start = time.time()
        func(a, b)
        end = time.time()
        times.append(end - start)
    return min(times), max(times), sum(times) / len(times)

# Построение графиков
def plot_results(results, title):
    x = [r[0] for r in results]
    y_min = [r[1] for r in results]
    y_max = [r[2] for r in results]
    y_avg = [r[3] for r in results]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y_min, label="Min Time", marker="o")
    plt.plot(x, y_max, label="Max Time", marker="o")
    plt.plot(x, y_avg, label="Average Time", marker="o")
    plt.xlabel("Numbers (a, b)")
    plt.ylabel("Time (s)")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

# Генерация данных и выполнение замеров
def main():
    results_subtraction = []
    results_mod = []
    results_prime_factors = []

    for _ in range(10):
        a = random.randint(10, 1_000_000)
        b = random.randint(10, 1_000_000)

        results_subtraction.append((a, *measure_time(gcd_subtraction, a, b)))
        results_mod.append((a, *measure_time(gcd_mod, a, b)))
        results_prime_factors.append((a, *measure_time(gcd_prime_factors, a, b)))

    plot_results(results_subtraction, "GCD (Subtraction Method)")
    plot_results(results_mod, "GCD (Modulo Method)")
    plot_results(results_prime_factors, "GCD (Prime Factors Method)")

if __name__ == "__main__":
    main()