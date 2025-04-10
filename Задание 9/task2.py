def nearest_smaller_elements(arr):
    lenght = len(arr)
    result = [0] * lenght
    stack = []

    for i in range(lenght):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        
        if stack:
            result[i] = stack[-1]
        else:
            result[i] = 0
        
        stack.append(i)

    return result

# Пример использования
arr = [4, 5, 2, 10, 8]
print(nearest_smaller_elements(arr))