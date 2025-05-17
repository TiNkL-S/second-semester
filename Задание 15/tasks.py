# Задача 1: НОД двух чисел (рекурсивно)
def gcd(a, b):
    """
    Вычисляет НОД двух чисел рекурсивно.
    Сложность: O(log(min(a, b)))
    """
    if b == 0:
        return a
    return gcd(b, a % b)

# Задача 2: Подсчет числа потомков для каждого узла
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.descendants = 0  # Количество потомков

def count_descendants(node):
    """
    Подсчитывает количество потомков для каждого узла.
    Сложность: O(n)
    """
    if node is None:
        return 0
    left_descendants = count_descendants(node.left)
    right_descendants = count_descendants(node.right)
    node.descendants = left_descendants + right_descendants
    return node.descendants + 1

def print_preorder_with_descendants(node):
    """
    Прямой обход дерева с выводом количества потомков.
    """
    if node:
        print(f"Узел {node.value}: потомков = {node.descendants}")
        print_preorder_with_descendants(node.left)
        print_preorder_with_descendants(node.right)

# Задача 3: Проверка изоморфизма двух деревьев
def is_isomorphic(node1, node2):
    """
    Проверяет, являются ли два дерева изоморфными.
    Сложность: O(n)
    """
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.value != node2.value:
        return False
    return (is_isomorphic(node1.left, node2.left) and is_isomorphic(node1.right, node2.right)) or \
           (is_isomorphic(node1.left, node2.right) and is_isomorphic(node1.right, node2.left))

# Задача 4: Подсчет высоты поддерева для каждого узла
def calculate_height(node):
    """
    Подсчитывает высоту поддерева для каждого узла.
    Сложность: O(n)
    """
    if node is None:
        return 0
    left_height = calculate_height(node.left)
    right_height = calculate_height(node.right)
    node.height = 1 + max(left_height, right_height)
    return node.height

def print_preorder_with_height(node):
    """
    Прямой обход дерева с выводом высоты поддерева.
    """
    if node:
        print(f"Узел {node.value}: высота = {node.height}")
        print_preorder_with_height(node.left)
        print_preorder_with_height(node.right)

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
    # Задача 1
    a, b = 48, 18
    avg_time_task1 = measure_time(gcd, a, b)
    print(f"НОД({a}, {b}) = {gcd(a, b)}")
    print(f"Среднее время работы задачи 1: {avg_time_task1:.6f} секунд")

    # Задача 2
    a = TreeNode('A')
    b = TreeNode('B')
    c = TreeNode('C')
    d = TreeNode('D')
    e = TreeNode('E')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    avg_time_task2 = measure_time(count_descendants, a)
    count_descendants(a)
    print("\nПрямой обход дерева с количеством потомков:")
    print_preorder_with_descendants(a)
    print(f"Среднее время работы задачи 2: {avg_time_task2:.6f} секунд")

    # Задача 3
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree2 = TreeNode(1)
    tree2.left = TreeNode(3)
    tree2.right = TreeNode(2)
    avg_time_task3 = measure_time(is_isomorphic, tree1, tree2)
    print(f"\nДеревья изоморфны: {is_isomorphic(tree1, tree2)}")
    print(f"Среднее время работы задачи 3: {avg_time_task3:.6f} секунд")

    # Задача 4
    avg_time_task4 = measure_time(calculate_height, a)
    calculate_height(a)
    print("\nПрямой обход дерева с высотой поддерева:")
    print_preorder_with_height(a)
    print(f"Среднее время работы задачи 4: {avg_time_task4:.6f} секунд")