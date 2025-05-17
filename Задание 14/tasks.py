import math
import time

# Задача 1: Рекурсивное вычисление логарифма факториала
def log_factorial(n):
    """
    Вычисляет логарифм факториала числа N рекурсивно.
    Сложность: O(n)
    """
    if n == 0 or n == 1:
        return 0
    return math.log(n) + log_factorial(n - 1)

# Задача 2: Рекурсивное изменение порядка узлов в односвязном списке
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"

def print_list(head):
    """
    Выводит элементы односвязного списка.
    """
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

def reverse_list(head):
    """
    Рекурсивно изменяет порядок узлов в односвязном списке.
    Сложность: O(n)
    """
    if head is None or head.next is None:
        return head
    new_head = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return new_head

# Задача 3: Обход дерева
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(root):
    """
    Прямой обход дерева (Preorder).
    Сложность: O(n)
    """
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root):
    """
    Внутренний обход дерева (Inorder).
    Сложность: O(n)
    """
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

def postorder_traversal(root):
    """
    Обратный обход дерева (Postorder).
    Сложность: O(n)
    """
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

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
    n = 5
    avg_time_task1 = measure_time(log_factorial, n)
    print(f"log({n}!) = {log_factorial(n):.6f}")
    print(f"Среднее время работы задачи 1: {avg_time_task1:.6f} секунд")

    # Задача 2
    head = Node(3)
    head.next = Node(2)
    head.next.next = Node(0)
    head.next.next.next = Node(-4)
    print("\nИсходный список:")
    print_list(head)
    avg_time_task2 = measure_time(reverse_list, head)
    reversed_head = reverse_list(head)
    print("Перевернутый список:")
    print_list(reversed_head)
    print(f"Среднее время работы задачи 2: {avg_time_task2:.6f} секунд")

    # Задача 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("\nПрямой обход дерева (Preorder):")
    avg_time_preorder = measure_time(preorder_traversal, root)
    preorder_traversal(root)
    print(f"\nСреднее время работы прямого обхода: {avg_time_preorder:.6f} секунд")

    print("\nВнутренний обход дерева (Inorder):")
    avg_time_inorder = measure_time(inorder_traversal, root)
    inorder_traversal(root)
    print(f"\nСреднее время работы внутреннего обхода: {avg_time_inorder:.6f} секунд")

    print("\nОбратный обход дерева (Postorder):")
    avg_time_postorder = measure_time(postorder_traversal, root)
    postorder_traversal(root)
    print(f"\nСреднее время работы обратного обхода: {avg_time_postorder:.6f} секунд")