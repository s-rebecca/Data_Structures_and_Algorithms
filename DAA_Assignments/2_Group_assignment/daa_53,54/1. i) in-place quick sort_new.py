import random
import timeit
import matplotlib.pyplot as plt

# Define the sorting functions

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return comparisons

def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return comparisons

def insertion_sort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return comparisons

def merge_sort(arr):
    comparisons = [0]

    def merge(arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        left_arr = [0] * n1
        right_arr = [0] * n2

        for i in range(n1):
            left_arr[i] = arr[left + i]
        for j in range(n2):
            right_arr[j] = arr[mid + 1 + j]

        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            comparisons[0] += 1
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = right_arr[j]
            j += 1
            k += 1

    def merge_sort_helper(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid + 1, right)
            merge(arr, left, mid, right)

    merge_sort_helper(arr, 0, len(arr) - 1)
    return comparisons[0]

def quick_sort(arr):
    comparisons = [0]

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    quick_sort_helper(arr, 0, len(arr) - 1)
    return comparisons[0]

def radix_sort(arr):
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            arr[i] = output[i]

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Implement Bucket Sort
def bucket_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    bucket_range = (max_val - min_val) / len(arr)
    buckets = [[] for _ in range(len(arr))]

    for i in range(len(arr)):
        index = int((arr[i] - min_val) / bucket_range)
        if index != len(arr):
            buckets[index].append(arr[i])
        else:
            buckets[len(arr) - 1].append(arr[i])

    k = 0
    for i in range(len(arr)):
        insertion_sort(buckets[i])
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1

# Generate worst-case input data
def generate_worst_case_data(size):
    return list(range(size, 0, -1))

# Define sorting functions to test
sorting_functions = [
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    radix_sort,
    bucket_sort
]
if __name__ == "__main__":
    # Test different sorting algorithms for worst-case scenarios
    sizes = [100, 500, 1000]  # Adjust the input sizes as needed
    results = {}

    for sort_func in sorting_functions:
        comparisons = []
        for size in sizes:
            input_data = generate_worst_case_data(size)
            comp = sort_func(input_data.copy())
            comparisons.append(comp)
        results[sort_func.__name__] = comparisons

    # Create a graph to compare sorting algorithms
    plt.figure(figsize=(10, 6))

    for sort_func_name, comparisons in results.items():
        plt.plot(sizes, comparisons, marker='o', label=sort_func_name)

    plt.title('Comparison of Sorting Algorithms (Worst Case)')
    plt.xlabel('Input Size')
    plt.ylabel('Comparisons')
    plt.legend(loc='upper left')
    plt.grid(True)

    # Show the graph
    plt.show()
