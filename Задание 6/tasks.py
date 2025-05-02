import time
import matplotlib.pyplot as plt
import math

def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == n:
            return True
        elif square < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Альтернативная реализация для сравнения (использует встроенную функцию sqrt)
def is_perfect_square_sqrt(n):
    if n < 0:
        return False
    root = math.isqrt(n)
    return root * root == n

# Функция для измерения времени выполнения
def measure_time(func, n):
    start = time.perf_counter()
    func(n)
    return time.perf_counter() - start

# Тестирование на разных размерах входных данных
sizes = [10**i for i in range(1, 8)]  # От 10 до 10^7
binary_times = []
sqrt_times = []

for size in sizes:
    # Для точности измеряем среднее время по 1000 выполнений
    binary_time = sum(measure_time(is_perfect_square, size) for _ in range(1000)) / 1000
    sqrt_time = sum(measure_time(is_perfect_square_sqrt, size) for _ in range(1000)) / 1000
    
    binary_times.append(binary_time)
    sqrt_times.append(sqrt_time)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(sizes, binary_times, label='Бинарный поиск (O(log n))', marker='o')
plt.plot(sizes, sqrt_times, label='Метод с sqrt (O(1))', marker='x')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Значение n (логарифмическая шкала)')
plt.ylabel('Время выполнения (секунды, логарифмическая шкала)')
plt.title('Сравнение времени проверки полного квадрата')
plt.legend()
plt.grid(True, which="both", ls="-")
plt.show()