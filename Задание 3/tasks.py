import numpy as np
import time
import random

# Создадим тестовую матрицу для всех задач
N, M = 1000, 1000  # Размер матрицы
A_np = np.random.rand(N, M) * 100  # Матрица NumPy
A_list = A_np.tolist()  # Обычный список списков

# Задача 1: Наибольшее значение среди средних значений строк
def task1_numpy(matrix):
    row_means = np.mean(matrix, axis=1)
    return np.max(row_means)

def task1_python(matrix):
    max_mean = -float('inf')
    for row in matrix:
        row_mean = sum(row) / len(row)
        if row_mean > max_mean:
            max_mean = row_mean
    return max_mean

# Замер времени для задачи 1
start = time.time()
result_np1 = task1_numpy(A_np)
time_np1 = time.time() - start

start = time.time()
result_py1 = task1_python(A_list)
time_py1 = time.time() - start

print(f"1. Наибольшее среднее по строкам (numpy): {result_np1:.4f}, время: {time_np1:.6f} сек")
print(f"1. Наибольшее среднее по строкам (python): {result_py1:.4f}, время: {time_py1:.6f} сек")
print(f"Разница во времени: {time_py1/time_np1:.1f}x\n")

# Задача 2: Наименьший элемент строки с максимальной суммой модулей
def task2_numpy(matrix):
    sum_abs = np.sum(np.abs(matrix), axis=1)
    row_idx = np.argmax(sum_abs)
    return np.min(matrix[row_idx])

def task2_python(matrix):
    max_sum = -float('inf')
    target_row = None
    for row in matrix:
        current_sum = sum(abs(x) for x in row)
        if current_sum > max_sum:
            max_sum = current_sum
            target_row = row
    return min(target_row)

# Замер времени для задачи 2
start = time.time()
result_np2 = task2_numpy(A_np)
time_np2 = time.time() - start

start = time.time()
result_py2 = task2_python(A_list)
time_py2 = time.time() - start

print(f"2. Наименьший элемент в строке с макс суммой (numpy): {result_np2:.4f}, время: {time_np2:.6f} сек")
print(f"2. Наименьший элемент в строке с макс суммой (python): {result_py2:.4f}, время: {time_py2:.6f} сек")
print(f"Разница во времени: {time_py2/time_np2:.1f}x\n")

# Задача 3: Наименьшее значение среди средних значений столбцов
def task3_numpy(matrix):
    col_means = np.mean(matrix, axis=0)
    return np.min(col_means)

def task3_python(matrix):
    min_mean = float('inf')
    for col in zip(*matrix):  # Транспонирование для итерации по столбцам
        col_mean = sum(col) / len(col)
        if col_mean < min_mean:
            min_mean = col_mean
    return min_mean

# Замер времени для задачи 3
start = time.time()
result_np3 = task3_numpy(A_np)
time_np3 = time.time() - start

start = time.time()
result_py3 = task3_python(A_list)
time_py3 = time.time() - start

print(f"3. Наименьшее среднее по столбцам (numpy): {result_np3:.4f}, время: {time_np3:.6f} сек")
print(f"3. Наименьшее среднее по столбцам (python): {result_py3:.4f}, время: {time_py3:.6f} сек")
print(f"Разница во времени: {time_py3/time_np3:.1f}x\n")

# Задача 4: Средние значения по строкам, столбцам и всей матрице
def task4_numpy(matrix):
    row_means = np.mean(matrix, axis=1)
    col_means = np.mean(matrix, axis=0)
    total_mean = np.mean(matrix)
    return row_means, col_means, total_mean

def task4_python(matrix):
    # Среднее по строкам
    row_means = [sum(row)/len(row) for row in matrix]
    
    # Среднее по столбцам
    col_means = []
    for col in zip(*matrix):
        col_means.append(sum(col)/len(col))
    
    # Среднее по всей матрице
    total_sum = sum(sum(row) for row in matrix)
    total_mean = total_sum / (len(matrix) * len(matrix[0]))
    
    return row_means, col_means, total_mean

# Замер времени для задачи 4
start = time.time()
row_np, col_np, total_np = task4_numpy(A_np)
time_np4 = time.time() - start

start = time.time()
row_py, col_py, total_py = task4_python(A_list)
time_py4 = time.time() - start

print(f"4. Среднее по всей матрице (numpy): {total_np:.4f}, время: {time_np4:.6f} сек")
print(f"4. Среднее по всей матрице (python): {total_py:.4f}, время: {time_py4:.6f} сек")
print(f"Разница во времени: {time_py4/time_np4:.1f}x\n")

# Задача 5: Умножение подматрицы на число
def task5_numpy(matrix, k, start_row, end_row, start_col, end_col):
    submatrix = matrix[start_row:end_row, start_col:end_col]
    matrix[start_row:end_row, start_col:end_col] = submatrix * k
    return matrix

def task5_python(matrix, k, start_row, end_row, start_col, end_col):
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            matrix[i][j] *= k
    return matrix

# Параметры подматрицы
k = 2.5
start_r, end_r = N//4, 3*N//4
start_c, end_c = M//4, 3*M//4

# Замер времени для задачи 5
start = time.time()
result_np5 = task5_numpy(A_np.copy(), k, start_r, end_r, start_c, end_c)
time_np5 = time.time() - start

start = time.time()
result_py5 = task5_python([row.copy() for row in A_list], k, start_r, end_r, start_c, end_c)
time_py5 = time.time() - start

print(f"5. Умножение подматрицы на {k} (numpy), время: {time_np5:.6f} сек")
print(f"5. Умножение подматрицы на {k} (python), время: {time_py5:.6f} сек")
print(f"Разница во времени: {time_py5/time_np5:.1f}x")