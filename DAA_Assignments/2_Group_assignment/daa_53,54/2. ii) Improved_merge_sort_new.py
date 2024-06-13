import random
import time
import sys

def generate_sorted_array(size):
    """Generate a sorted array."""
    return list(range(1, size + 1))

def generate_reverse_sorted_array(size):
    """Generate a reverse sorted array."""
    return list(range(size, 0, -1))

def generate_random_array(size, min_value=1, max_value=1000):
    """Generate an array with random elements."""
    return [random.randint(min_value, max_value) for _ in range(size)]

def generate_test_cases(test_case_sizes):
    """Generate test cases for best, worst, and average cases of Merge Sort."""
    test_cases = []

    for size in test_case_sizes:
        # Best case: Sorted array
        best_case = generate_sorted_array(size)
        test_cases.append((best_case, "Best Case"))

        # Worst case: Reverse sorted array
        worst_case = generate_reverse_sorted_array(size)
        test_cases.append((worst_case, "Worst Case"))

        # Average case: Random array
        average_case = generate_random_array(size)
        test_cases.append((average_case, "Average Case"))

    return test_cases

def insertion_sort(arr, low, high):
    count = 0
    swap = 0

    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1

        while j >= low and arr[j] > key:
            count += 1
            arr[j + 1] = arr[j]
            swap += 1
            j -= 1

        arr[j + 1] = key
        swap += 1

    return count, swap

def merge_sort(arr):
    count = 0
    swap = 0

    n = len(arr)
    threshold = 10  # Threshold for using insertion sort

    if n <= threshold:
        # Use insertion sort for small arrays
        return insertion_sort(arr, 0, n - 1)

    # Split the array into two halves
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    count_left, swap_left = merge_sort(left)
    count_right, swap_right = merge_sort(right)

    count += count_left + count_right
    swap += swap_left + swap_right

    # Merge the sorted halves
    count_merge, swap_merge = merge(arr, left, right)
    count += count_merge
    swap += swap_merge

    return count, swap

def merge(arr, left, right):  #different function for merging(conquering) unlike the simple merge sort
    count = 0
    swap = 0

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  #ie; if a<b, add a to sorted array
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            swap += 1  # Update swap count when elements are swapped
        k += 1
        count += 1  # Update comparison count
# check if any elements were left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        swap += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        swap += 1

    return count, swap

if __name__ == "__main__":
    # Specify the sizes of test cases you want
    test_case_sizes = [100, 500, 1000]

    # Generate test cases
    test_cases = generate_test_cases(test_case_sizes)

    # Sort and print the generated test cases using In-Place Merge Sort
    for test_case, case_type in test_cases:
        elements = test_case[:]
        print(" ")
        print(f"Test Case Type: {case_type}")
        print(" ")
        print(f"Test Case Size: {len(elements)}")
        print(" ")
        print(f"Test Case Contents: {elements}")
        print(" ")

        start_time = time.perf_counter()  # Start measuring runtime
        comparisons, swaps = merge_sort(elements)
        end_time = time.perf_counter()  # Stop measuring runtime

        print(" ")
        print(f"Sorted Result: {elements}\n")
        print(" ")
        print(f"Comparisons, Swaps: {comparisons, swaps}")
        print(" ")

        runtime_ms = (end_time - start_time) * 1000
        print(f"Runtime: {runtime_ms} milliseconds")

        element_size_bytes = sys.getsizeof(0)
        total_memory_used = element_size_bytes * len(elements)
        print(" ")
        print(f"Total Memory Used: {total_memory_used} bytes")
        print("------------------------")
