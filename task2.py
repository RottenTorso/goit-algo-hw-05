def binary_search(arr, target):
    # Ініціалізуємо ліву та праву межі пошуку
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        # Обчислюємо середній індекс
        mid = (left + right) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    # Якщо верхня межа не знайдена і ліва межа в межах масиву
    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]

    # Повертаємо кількість ітерацій та верхню межу
    return (iterations, upper_bound)

# Приклад використання:
sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
target_value = 4.0
result = binary_search(sorted_array, target_value)
print(result)  # Повинно повернути (кількість ітерацій, верхня межа)