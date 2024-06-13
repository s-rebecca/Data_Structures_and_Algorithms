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
    """Generate test cases for best, worst, and average cases of Quick Sort."""
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

# Threshold for switching to Insertion Sort
INSERTION_SORT_THRESHOLD = 10

def quick_sort(arr, low, high):
    if low < high:
        # Optimize pivot selection (median of three)
        median_of_three(arr, low, high)

        # If the size of the subarray is below the threshold, switch to Insertion Sort
        if high - low + 1 <= INSERTION_SORT_THRESHOLD:
            insertion_sort(arr, low, high)
            
        else:
            # Partition the array and get the pivot index and swaps count
            pivot_index, swaps = partition(arr, low, high)

            # Recursively sort the subarrays on both sides of the pivot
            quick_sort(arr, low, pivot_index - 1)
            quick_sort(arr, pivot_index + 1, high)

def median_of_three(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
              
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
        
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
        
    # Place the median value at the last index
    arr[mid], arr[high] = arr[high], arr[mid]
    
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    swaps = 0

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps += 1

    return i + 1, swaps

def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    # Specify the sizes of test cases you want
    test_case_sizes = [100, 500, 1000]

    # Generate test cases
    test_cases = generate_test_cases(test_case_sizes)

    for test_case, case_type in test_cases:
        elements = test_case[:]
        arr_copy = elements.copy()  # Make a copy of the input array to avoid modification
        quick_sort(arr_copy, 0, len(arr_copy) - 1)
        
        print(" ")
        print(f"Test Case Type: {case_type}")
        print(" ")
        print(f"Test Case Size: {len(elements)}")
        print(" ")
        print(f"Test Case Contents: {elements}")
        print(" ")
      
        
        # Measure runtime
        start_time = time.perf_counter()
        quick_sort(elements, 0, len(elements) - 1)
        end_time = time.perf_counter()
        runtime_ms = (end_time - start_time) * 1000
        print("Runtime: {:.6f} milliseconds".format(runtime_ms))
        
        # Measure memory usage
        memory_usage = sys.getsizeof(elements)
        print("Memory Usage: {:.2f} KB".format(memory_usage / 1024.0))
        
        print(f"Sorted Result: {elements}\n")
        print("------------------------")
