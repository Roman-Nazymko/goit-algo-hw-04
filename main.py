import timeit
import random 

from insertion_sort import insertion_sort
from merge_sort import merge_sort

# Функція для вимірювання часу сортування
def measure_time(sort_func, data):
    start_time = timeit.default_timer()
    sorted_data = sort_func(data[:])  # Робимо копію даних перед сортуванням
    execution_time = timeit.default_timer() - start_time
    return sorted_data, execution_time

# Використання вбудованого сортування Python
def built_in_sort(arr):
    arr.sort()
    return arr

# Генеруємо випадкові дані для тестування
data_smallest = [random.randint(0, 1_000) for _ in range(10)]
data_small = [random.randint(0, 1_000) for _ in range(100)]
data_big = [random.randint(0, 1_000) for _ in range(1_000)]
data_largest = [random.randint(0, 10_000) for _ in range(10_000)]

test_data = [
    ("Smallest (10)", data_smallest),
    ("Small (100)", data_small),
    ("Big (1,000)", data_big),
    ("Largest (10,000)", data_largest)
]

sorting_functions = [
    ("Insertion Sort", insertion_sort),
    ("Merge Sort", merge_sort),
    ("Timsort (Python's sorted)", sorted),
    ("Timsort (Python's sort)", built_in_sort)
]

def main():
    results = []
    headers = ["Array Size"] + [name for name, _ in sorting_functions]

    for size_name, data in test_data:
        row = [size_name]
        for name, func in sorting_functions:
            _, exec_time = measure_time(func, data)
            row.append(f"{exec_time:.6f} s")
        results.append(row)

    col_widths = [max(len(str(cell)) for cell in column) for column in zip(*([headers] + results))]

    header_row = " | ".join(f"{headers[i]:<{col_widths[i]}}" for i in range(len(headers)))
    separator_row = " | ".join('-' * col_widths[i] for i in range(len(headers)))
    print(header_row)
    print(separator_row)

    for row in results:
        print(" | ".join(f"{row[i]:<{col_widths[i]}}" for i in range(len(row))))

if __name__ == "__main__":
    main()