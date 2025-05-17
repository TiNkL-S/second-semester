import time
import random
from math import gcd
from collections import Counter

# Алгоритм Евклида (вычитание)
def gcd_subtraction(a, b):
    while b != 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a

# Алгоритм Евклида (остаток от деления)
def gcd_mod(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# НОД через разложение на множители
def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def gcd_factors(a, b):
    factors_a = Counter(prime_factors(a))
    factors_b = Counter(prime_factors(b))
    common_factors = factors_a & factors_b
    gcd_result = 1
    for factor, count in common_factors.items():
        gcd_result *= factor ** count
    return gcd_result

# Тестирование производительности
def measure_time(func, a, b, iterations=100):
    start_time = time.time()
    for _ in range(iterations):
        func(a, b)
    return (time.time() - start_time) / iterations

if __name__ == "__main__":
    # Генерация случайных чисел
    test_cases = [(random.randint(10, 1_000_000), random.randint(10, 1_000_000)) for _ in range(10)]

    # Сравнение времени работы
    for a, b in test_cases:
        time_subtraction = measure_time(gcd_subtraction, a, b)
        time_mod = measure_time(gcd_mod, a, b)
        time_factors = measure_time(gcd_factors, a, b)

        print(f"Числа: {a}, {b}")
        print(f"Вычитание: {time_subtraction:.6f} сек")
        print(f"Остаток от деления: {time_mod:.6f} сек")
        print(f"Разложение на множители: {time_factors:.6f} сек")
        print("-" * 40)