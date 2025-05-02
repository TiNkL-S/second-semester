import numpy as np

# 1. Создание одномерного массива из чисел от 1 до 10
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("1. Массив от 1 до 10:", arr1)

# 2. Массив из 7 нулей
arr2 = np.zeros(7)
print("2. Массив из 7 нулей:", arr2)

# 3. Массив из 5 единиц
arr3 = np.ones(5)
print("3. Массив из 5 единиц:", arr3)

# 4. Массив от 10 до 50 с шагом 5
arr4 = np.arange(10, 51, 5)
print("4. Массив от 10 до 50 с шагом 5:", arr4)

# 5. 6 чисел, равномерно распределенных от 0 до 100
arr5 = np.linspace(0, 100, 6)
print("5. 6 чисел от 0 до 100:", arr5)

# 6. Индексация массива
arr6 = np.array([2, 4, 6, 8, 10, 12, 14, 16])
print("6. Второй элемент:", arr6[1])
print("   Последний элемент:", arr6[-1])
print("   Элементы с 3 по 6:", arr6[3:7])

# 7. Итерация по массиву
arr7 = np.array([1, 3, 5, 7, 9])
print("7. Итерация по массиву:")
for element in arr7:
    print(element, end=' ')
print()

# 8. Сложение двух массивов
arr8_1 = np.array([1, 2, 3])
arr8_2 = np.array([4, 5, 6])
arr8_sum = arr8_1 + arr8_2
print("8. Сумма массивов:", arr8_sum)

# 9. Умножение массива на число
arr9 = np.array([1, 2, 3, 4])
arr9_mult = arr9 * 2
print("9. Массив умноженный на 2:", arr9_mult)

# 10. Возведение элементов в квадрат
arr10 = np.array([1, 2, 3, 4])
arr10_sq = arr10 ** 2
print("10. Квадраты элементов:", arr10_sq)

# 11. Поиск минимума и максимума
arr11 = np.array([5, 2, 9, 1, 7])
print("11. Минимум:", np.min(arr11), "Максимум:", np.max(arr11))

# 12. Среднее значение и стандартное отклонение
arr12 = np.array([1, 2, 3, 4, 5])
print("12. Среднее:", np.mean(arr12), "Стандартное отклонение:", np.std(arr12))

# 13. Логарифм, экспонента и синус
arr13 = np.array([1, 2, 3])
print("13. Логарифм:", np.log(arr13))
print("   Экспонента:", np.exp(arr13))
print("   Синус:", np.sin(arr13))

# 14. 10 случайных чисел от 0 до 1
arr14 = np.random.rand(10)
print("14. 10 случайных чисел [0,1]:", arr14)

# 15. 6 случайных целых от 1 до 100
arr15 = np.random.randint(1, 101, 6)
print("15. 6 случайных целых [1,100]:", arr15)

# 16. Преобразование в двумерный массив 2x5
arr16 = np.arange(1, 11)
arr16_2d = arr16.reshape(2, 5)
print("16. Двумерный массив 2x5:\n", arr16_2d)

# 17. Изменение формы на 3x3
arr17 = np.arange(1, 10)
arr17_3x3 = arr17.reshape(3, 3)
print("17. Массив 3x3:\n", arr17_3x3)

# 18. Фильтрация (элементы > 5)
arr18 = np.array([3, 6, 2, 8, 4, 9])
filtered = arr18[arr18 > 5]
print("18. Элементы > 5:", filtered)

# 19. vectorize для возведения в куб
def cube(x):
    return x ** 3

arr19 = np.array([1, 2, 3, 4])
vectorized_cube = np.vectorize(cube)
arr19_cubed = vectorized_cube(arr19)
print("19. Элементы в кубе:", arr19_cubed)

# 20. Сохранение и загрузка массива
arr20 = np.array([1, 2, 3, 4, 5])
np.save('array20.npy', arr20)
loaded_arr = np.load('array20.npy')
print("20. Загруженный массив:", loaded_arr)