import time
import matplotlib.pyplot as plt

# 1. Вычисление значения выражения в постфиксной записи
def evaluate_postfix(expression):
    """
    Вычисляет значение выражения в постфиксной записи.
    Сложность: O(n)
    """
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():  # Если число, кладем в стек
            stack.append(int(token))
        elif token in "+-*":  # Если оператор, выполняем операцию
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)

    return stack[0]  # Результат остается в стеке

# Пример использования
postfix_expression = "5 3 2 + 3 * +"
print(f"Результат выражения '{postfix_expression}': {evaluate_postfix(postfix_expression)}")


# 2. Проверка правильности скобочной структуры
def is_valid_parentheses(s):
    """
    Проверяет, является ли скобочная структура правильной.
    Сложность: O(n)
    """
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

# Пример использования
parentheses_string = "(()())"
print(f"Строка '{parentheses_string}' является правильной: {is_valid_parentheses(parentheses_string)}")


# 3. Удаление дубликатов из отсортированного списка
def remove_duplicates(sorted_list):
    """
    Удаляет дубликаты из отсортированного списка.
    Сложность: O(n)
    """
    if not sorted_list:
        return []

    unique_list = [sorted_list[0]]
    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[i - 1]:
            unique_list.append(sorted_list[i])

    return unique_list

# Замер времени выполнения функции
def measure_time(func, *args, iterations=10):
    times = []
    for _ in range(iterations):
        start = time.time()
        func(*args)
        end = time.time()
        times.append(end - start)
    return sum(times) / len(times)

# Построение графика зависимости времени работы от размера списка
def plot_performance():
    sizes = [10**i for i in range(1, 6)]  # Размеры списков: 10, 100, 1000, 10000, 100000
    times = []

    for size in sizes:
        sorted_list = list(range(size)) * 2  # Создаем отсортированный список с дубликатами
        avg_time = measure_time(remove_duplicates, sorted_list)
        times.append(avg_time)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker="o")
    plt.xlabel("Размер списка")
    plt.ylabel("Среднее время работы (сек)")
    plt.title("Зависимость времени работы от размера списка")
    plt.grid()
    plt.show()

# Пример использования
plot_performance()