"""

Cортування злиттям

"""

# Функція сортування масиву за допомогою алгоритму сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Рекурсивне ділення масиву навпіл
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Застосування сортування злиттям до кожної половини масиву
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Злиття двох відсортованих підмасивів
    return merge(left_half, right_half)

# Фукція злиття двох відсортованих масивів
def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    
    # Перевірка кожного елементу з обох масивів і додавання меншого елементу до результату
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    # Додавання залишкових елементів, якщо вони є
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    
    return result
