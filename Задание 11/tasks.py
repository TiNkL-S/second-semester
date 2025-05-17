from collections import deque
import time
import matplotlib.pyplot as plt

# 1. Объединение двух очередей с использованием deque
def merge_queues_deque(q1, q2):
    """
    Объединяет две очереди, упорядоченные по возрастанию, с использованием deque.
    Сложность: O(n + m), где n и m — размеры очередей.
    """
    result = deque()
    while q1 and q2:
        if q1[0] < q2[0]:
            result.append(q1.popleft())
        else:
            result.append(q2.popleft())
    result.extend(q1)
    result.extend(q2)
    return result

# 2. Реализация очереди с использованием двух стеков
class QueueUsingTwoStacks:
    """
    Реализация очереди с использованием двух стеков.
    """
    def __init__(self):
        self.stack_in = []  # Стек для добавления элементов
        self.stack_out = []  # Стек для удаления элементов

    def enqueue(self, value):
        """
        Добавляет элемент в очередь.
        Сложность: O(1)
        """
        self.stack_in.append(value)

    def dequeue(self):
        """
        Удаляет элемент из очереди.
        Сложность: O(1) в среднем, O(n) в худшем случае (когда stack_out пуст).
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if self.stack_out:
            return self.stack_out.pop()
        else:
            raise IndexError("Очередь пуста")

    def is_empty(self):
        """
        Проверяет, пуста ли очередь.
        """
        return not self.stack_in and not self.stack_out

    def peek(self):
        """
        Возвращает первый элемент очереди без удаления.
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if self.stack_out:
            return self.stack_out[-1]
        else:
            raise IndexError("Очередь пуста")

# 3. Объединение двух очередей с использованием очереди на двух стеках
def merge_queues_two_stacks(q1, q2):
    """
    Объединяет две очереди, упорядоченные по возрастанию, с использованием очереди на двух стеках.
    Сложность: O(n + m), где n и m — размеры очередей.
    """
    result = QueueUsingTwoStacks()
    while not q1.is_empty() and not q2.is_empty():
        if q1.peek() < q2.peek():
            result.enqueue(q1.dequeue())
        else:
            result.enqueue(q2.dequeue())
    while not q1.is_empty():
        result.enqueue(q1.dequeue())
    while not q2.is_empty():
        result.enqueue(q2.dequeue())
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

# Построение графика зависимости времени работы от размера очередей
def plot_performance():
    sizes = [10**i for i in range(1, 5)]  # Размеры очередей: 10, 100, 1000, 10000
    times_deque = []
    times_two_stacks = []

    for size in sizes:
        q1 = deque(range(1, size + 1, 2))  # Очередь с нечетными числами
        q2 = deque(range(2, size + 1, 2))  # Очередь с четными числами

        # Замер времени для deque
        avg_time_deque = measure_time(merge_queues_deque, q1.copy(), q2.copy())
        times_deque.append(avg_time_deque)

        # Замер времени для очереди на двух стеках
        q1_stack = QueueUsingTwoStacks()
        q2_stack = QueueUsingTwoStacks()
        for elem in q1:
            q1_stack.enqueue(elem)
        for elem in q2:
            q2_stack.enqueue(elem)
        avg_time_two_stacks = measure_time(merge_queues_two_stacks, q1_stack, q2_stack)
        times_two_stacks.append(avg_time_two_stacks)

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_deque, label="Deque", marker="o")
    plt.plot(sizes, times_two_stacks, label="Two Stacks", marker="o")
    plt.xlabel("Размер очередей")
    plt.ylabel("Среднее время работы (сек)")
    plt.title("Зависимость времени работы от размера очередей")
    plt.legend()
    plt.grid()
    plt.show()

# Пример использования
if __name__ == "__main__":
    # Пример с небольшими очередями
    q1 = deque([1, 4, 6, 9])
    q2 = deque([2, 3, 7, 10])
    print(f"Объединение с deque: {list(merge_queues_deque(q1, q2))}")

    q1_stack = QueueUsingTwoStacks()
    q2_stack = QueueUsingTwoStacks()
    for elem in [1, 4, 6, 9]:
        q1_stack.enqueue(elem)
    for elem in [2, 3, 7, 10]:
        q2_stack.enqueue(elem)
    merged_stack_queue = merge_queues_two_stacks(q1_stack, q2_stack)
    merged_result = []
    while not merged_stack_queue.is_empty():
        merged_result.append(merged_stack_queue.dequeue())
    print(f"Объединение с двумя стеками: {merged_result}")

    # Построение графика производительности
    plot_performance()