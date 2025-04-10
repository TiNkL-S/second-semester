import os

def print_words_in_reverse(filename):
    if not os.path.exists(filename):
        print(f"Ошибка: файл '{filename}' не найден!")
        print("Текущая рабочая директория:", os.getcwd())
        return
    
    stack = []
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                stack.append(word)
    
    while stack:
        print(stack.pop())

# Пример использования
print_words_in_reverse('example.txt')