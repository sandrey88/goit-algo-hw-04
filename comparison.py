import random
import timeit
from merge_sort import merge_sort
from insertion_sort import insertion_sort

# Функція генерації випадкового масиву заданого розміру
def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]

# 
def compare_sorting_algorithms():
    sizes = [100, 1000, 5000, 10000]  # Розміри тестових масивів
    for size in sizes:
        arr = generate_random_array(size)
        
        # Вимірювання часу виконання для сортування злиттям
        merge_sort_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)
        
        # Вимірювання часу виконання для сортування вставками
        insertion_sort_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
        
        # Вимірювання часу виконання для вбудованого алгоритму сортування Python
        python_sorted_time = timeit.timeit(lambda: sorted(arr.copy()), number=1)
        
        # Вивід результатів тестування
        print(f"Розмір масиву: {size}")
        print(f"Сортування злиттям: {merge_sort_time} сек")
        print(f"Сортування вставками: {insertion_sort_time} сек")
        print(f"Timsort (вбудований алгоритм Python): {python_sorted_time} сек")
        print("-" * 40)

# Викликаємо функцію для порівняння алгоритмів
compare_sorting_algorithms()
