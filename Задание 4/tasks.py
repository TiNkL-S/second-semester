import time
import random
import matplotlib.pyplot as plt
import numpy as np

# Функции для проверки дубликатов
def has_duplicates_set(lst):
    return len(lst) != len(set(lst))

def has_duplicates_nested(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

# Функции для нахождения пересечения
def intersection_set(lst1, lst2):
    return list(set(lst1) & set(lst2))

def intersection_nested(lst1, lst2):
    result = []
    for item in lst1:
        if item in lst2 and item not in result:
            result.append(item)
    return result

# Функции для удаления дубликатов
def remove_duplicates_set(lst):
    return list(set(lst))

def remove_duplicates_loop(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# Функции для нахождения первого повторяющегося элемента
def first_duplicate_set(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return item
        seen.add(item)
    return None

def first_duplicate_nested(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return lst[i]
    return None

# Функции для нахождения суммы двух чисел
def two_sum_set(lst, target):
    nums = set()
    for num in lst:
        complement = target - num
        if complement in nums:
            return (complement, num)
        nums.add(num)
    return None

def two_sum_nested(lst, target):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                return (lst[i], lst[j])
    return None

# Размеры списков для тестирования
sizes = [10, 100, 500, 1000, 2000, 5000]

# Результаты времени выполнения
results = {
    'has_duplicates_set': [],
    'has_duplicates_nested': [],
    'intersection_set': [],
    'intersection_nested': [],
    'remove_duplicates_set': [],
    'remove_duplicates_loop': [],
    'first_duplicate_set': [],
    'first_duplicate_nested': [],
    'two_sum_set': [],
    'two_sum_nested': []
}

# Проведение замеров
for size in sizes:
    print(f"Testing size: {size}")
    
    # Генерация тестовых данных
    lst1 = [random.randint(0, size//2) for _ in range(size)]
    lst2 = [random.randint(0, size//2) for _ in range(size)]
    target = random.randint(0, size)
    
    # Замер времени для has_duplicates
    start = time.time()
    has_duplicates_set(lst1)
    results['has_duplicates_set'].append(time.time() - start)
    
    start = time.time()
    has_duplicates_nested(lst1)
    results['has_duplicates_nested'].append(time.time() - start)
    
    # Замер времени для intersection
    start = time.time()
    intersection_set(lst1, lst2)
    results['intersection_set'].append(time.time() - start)
    
    start = time.time()
    intersection_nested(lst1, lst2)
    results['intersection_nested'].append(time.time() - start)
    
    # Замер времени для remove_duplicates
    start = time.time()
    remove_duplicates_set(lst1)
    results['remove_duplicates_set'].append(time.time() - start)
    
    start = time.time()
    remove_duplicates_loop(lst1)
    results['remove_duplicates_loop'].append(time.time() - start)
    
    # Замер времени для first_duplicate
    start = time.time()
    first_duplicate_set(lst1)
    results['first_duplicate_set'].append(time.time() - start)
    
    start = time.time()
    first_duplicate_nested(lst1)
    results['first_duplicate_nested'].append(time.time() - start)
    
    # Замер времени для two_sum
    start = time.time()
    two_sum_set(lst1, target)
    results['two_sum_set'].append(time.time() - start)
    
    start = time.time()
    two_sum_nested(lst1, target)
    results['two_sum_nested'].append(time.time() - start)

# Построение графиков
plt.figure(figsize=(15, 10))

# 1. Проверка дубликатов
plt.subplot(2, 3, 1)
plt.plot(sizes, results['has_duplicates_set'], label='С множеством (O(n))')
plt.plot(sizes, results['has_duplicates_nested'], label='Без множества (O(n²))')
plt.title('Проверка дубликатов')
plt.xlabel('Размер списка')
plt.ylabel('Время (сек)')
plt.legend()
plt.grid()

# 2. Пересечение списков
plt.subplot(2, 3, 2)
plt.plot(sizes, results['intersection_set'], label='С множеством (O(n+m))')
plt.plot(sizes, results['intersection_nested'], label='Без множества (O(n*m))')
plt.title('Пересечение списков')
plt.xlabel('Размер списка')
plt.ylabel('Время (сек)')
plt.legend()
plt.grid()

# 3. Удаление дубликатов
plt.subplot(2, 3, 3)
plt.plot(sizes, results['remove_duplicates_set'], label='С множеством (O(n))')
plt.plot(sizes, results['remove_duplicates_loop'], label='Без множества (O(n²))')
plt.title('Удаление дубликатов')
plt.xlabel('Размер списка')
plt.ylabel('Время (сек)')
plt.legend()
plt.grid()

# 4. Первый дубликат
plt.subplot(2, 3, 4)
plt.plot(sizes, results['first_duplicate_set'], label='С множеством (O(n))')
plt.plot(sizes, results['first_duplicate_nested'], label='Без множества (O(n²))')
plt.title('Первый повторяющийся элемент')
plt.xlabel('Размер списка')
plt.ylabel('Время (сек)')
plt.legend()
plt.grid()

# 5. Сумма двух чисел
plt.subplot(2, 3, 5)
plt.plot(sizes, results['two_sum_set'], label='С множеством (O(n))')
plt.plot(sizes, results['two_sum_nested'], label='Без множества (O(n²))')
plt.title('Сумма двух чисел')
plt.xlabel('Размер списка')
plt.ylabel('Время (сек)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()