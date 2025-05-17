# 1. Определение минимального количества удалений для получения правильной скобочной последовательности
def min_removals_to_valid_parentheses(s):
    """
    Определяет минимальное количество символов, которые необходимо удалить,
    чтобы строка стала правильной скобочной последовательностью (ПСП).
    Сложность: O(n)
    """
    open_count = 0
    removals = 0

    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count > 0:
                open_count -= 1
            else:
                removals += 1

    # Добавляем оставшиеся открывающие скобки, которые не закрыты
    removals += open_count
    return removals

# Пример использования
example = "(()))("
print(f"Минимальное количество удалений для строки '{example}': {min_removals_to_valid_parentheses(example)}")


# 2. Реализация очереди с использованием двух стеков
class QueueUsingTwoStacks:
    """
    Реализация очереди с использованием двух стеков.
    Операции enqueue и dequeue имеют сложность O(1) в среднем.
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

# Пример использования
queue = QueueUsingTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f"Удалённый элемент: {queue.dequeue()}")  # 1
queue.enqueue(4)
print(f"Удалённый элемент: {queue.dequeue()}")  # 2
print(f"Удалённый элемент: {queue.dequeue()}")  # 3
print(f"Удалённый элемент: {queue.dequeue()}")  # 4