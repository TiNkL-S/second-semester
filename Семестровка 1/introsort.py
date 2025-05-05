import random
import time
import math

def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    iterations = 0
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            iterations += 1
        arr[j + 1] = key
    return iterations

def heapify(arr, n, i, iterations):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        iterations += 1
        iterations = heapify(arr, n, largest, iterations)
    return iterations

def heapsort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    n = right - left + 1
    iterations = 0
    for i in range(n // 2 - 1, -1, -1):
        iterations = heapify(arr, n, i, iterations)
    for i in range(n - 1, 0, -1):
        arr[left], arr[left + i] = arr[left + i], arr[left]
        iterations += 1
        iterations = heapify(arr, i, 0, iterations)
    return iterations

def partition(arr, low, high, iterations):
    pivot = arr[(low + high) // 2]  # Медиана
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
            iterations += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
            iterations += 1
        if i >= j:
            return j, iterations
        arr[i], arr[j] = arr[j], arr[i]
        iterations += 1

def introsort(arr, max_depth=None, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    size = right - left + 1
    iterations = 0
    if max_depth is None:
        max_depth = 2 * math.floor(math.log2(size))
    if size < 16:
        iterations += insertion_sort(arr, left, right)
    elif max_depth == 0:
        iterations += heapsort(arr, left, right)
    else:
        p, iters = partition(arr, left, right, iterations)
        iterations += iters
        iterations += introsort(arr, max_depth - 1, left, p)
        iterations += introsort(arr, max_depth - 1, p + 1, right)
    return iterations

def measure_introsort(data):
    arr = data.copy()
    start_time = time.time()
    iterations = introsort(arr)
    end_time = time.time()
    return end_time - start_time, iterations