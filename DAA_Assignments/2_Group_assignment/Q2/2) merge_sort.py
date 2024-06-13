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

    for i in range(low + 1, high + 1): #2n
        key = arr[i] #2n
        j = i - 1 #2n

        while j >= low and arr[j] > key: #4n^2
            count += 1 #2n^2
            arr[j + 1] = arr[j] #4n^2
            swap += 1 #2n^2
            j -= 1 #2n^2

        arr[j + 1] = key #3n
        #swap += 1 #2n

    return count, swap #n

def merge_sort(arr):
    count = 0
    swap = 0

    n = len(arr)
    threshold = 10  # Threshold for using insertion sort

    for low in range(0, n, threshold): #n
        high = min(low + threshold - 1, n - 1) #n
        count_insert, swap_insert = insertion_sort(arr, low, high) #n
        count += count_insert #2n
        swap += swap_insert #2n

    for size in range(threshold, n, 2 * threshold): 
        for low in range(0, n - size, 2 * threshold):
            mid = min(low + size - 1, n - 1)
            high = min(low + 2 * size - 1, n - 1)

            count_merge, swap_merge = merge(arr, low, mid, high)
            count += count_merge
            swap += swap_merge

    return count, swap

def merge(arr, low, mid, high):
    count = 0
    swap = 0

    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]

    i = j = 0
    k = low

    while i < len(left) and j < len(right): #n
        
        if left[i] <= right[j]: #3n
            count+=1
            arr[k] = left[i] #3n
            #swap+=1
            i += 1 #2n
        else:
            arr[k] = right[j]
            #swap+=1 
            j += 1 
        k += 1 #2n

    while i < len(left): #2n
        arr[k] = left[i] #3n
        swap+=1
        i += 1 #2n
        k += 1 #2n

    while j < len(right): #2n
        arr[k] = right[j] #3n
        swap+=1
        j += 1 #2n 
        k += 1 #2n

    return count, swap

if __name__ == "__main__":
    # Specify the sizes of test cases you want
    test_case_sizes = [100, 500, 1000]

    # Generate test cases
    test_cases = generate_test_cases(test_case_sizes)

    # Sort and print the generated test cases using Merge Sort
    for test_case, case_type in test_cases:
        elements = test_case[:]
        print(" ")
        print(f"Test Case Type: {case_type}")
        print(" ")
        print(f"Test Case Size: {len(elements)}")
        print(" ")
        print(f"Test Case Contents: {elements}")
        print(" ")
        p = merge_sort(elements)
        print(" ")
        print(f"Sorted Result: {elements}\n")
        
        print(" ")
        print(f"Comparisons, Swaps: {p}")
        print(" ")
        element_size_bytes = sys.getsizeof(0)
        total_memory_used = element_size_bytes * len(elements)
        print(" ")
        print(f"Total Memory Used: {total_memory_used} bytes")
        print("------------------------")
