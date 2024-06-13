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
    comparisons, swaps = 0, 0
    if low < high: #1
        # Optimize pivot selection (median of three)
        median_of_three(arr, low, high) #1

        # If the size of the subarray is below the threshold, switch to Insertion Sort
        if high - low + 1 <= INSERTION_SORT_THRESHOLD: #2
            comparisons_insertion, swaps_insertion = insertion_sort(arr, low, high) #2
            comparisons += comparisons_insertion #2
            swaps += swaps_insertion #2
        else:
            # Partition the array and get the pivot index and swaps count
            pivot_index, swaps_partition = partition(arr, low, high) #2
            comparisons += (pivot_index - low) + (high - pivot_index) #2
            swaps += swaps_partition #2

            # Recursively sort the subarrays on both sides of the pivot
            comparisons_left, swaps_left = quick_sort(arr, low, pivot_index - 1) #2
            comparisons_right, swaps_right = quick_sort(arr, pivot_index + 1, high) #3
            comparisons += comparisons_left + comparisons_right #2
            swaps += swaps_left + swaps_right #2

    return comparisons, swaps #1

def median_of_three(arr, low, high):
    mid = (low + high) // 2     #3
    if arr[low] > arr[mid]:     #3
        arr[low], arr[mid] = arr[mid], arr[low]  #6
              
    if arr[low] > arr[high]: #3
        arr[low], arr[high] = arr[high], arr[low] #6
        
    if arr[mid] > arr[high]: #3
        arr[mid], arr[high] = arr[high], arr[mid] #6
        
    # Place the median value at the last index
    arr[mid], arr[high] = arr[high], arr[mid] #6
    
    return arr #1

def partition(arr, low, high):
    pivot = arr[high] #2
    i = low - 1 #2
    swaps = 0

    for j in range(low, high): #n
        if arr[j] <= pivot: #2n
            i += 1 #2n
            arr[i], arr[j] = arr[j], arr[i] #6n
            swaps += 1 

    arr[i + 1], arr[high] = arr[high], arr[i + 1] #8n
    swaps += 1

    return i + 1, swaps #n

def insertion_sort(arr, low, high)
    comparisons = 0
    swaps = 0
    for i in range(low + 1, high + 1): #n
        key = arr[i] #2n
        j = i - 1 #2n
        while j >= low and arr[j] > key: #4n^2
            comparisons += 1
            arr[j + 1] = arr[j] #4n^2
            swaps += 1
            j -= 1 #2n^2
        arr[j + 1] = key #3n
    return comparisons, swaps #1

if __name__ == "__main__":
    # Specify the sizes of test cases you want
    test_case_sizes = [100, 500, 1000]

    # Generate test cases
    test_cases = generate_test_cases(test_case_sizes)

    for test_case, case_type in test_cases:
        elements = test_case[:]
        arr_copy = elements.copy()  # Make a copy of the input array to avoid modification
        comparisons, swaps = quick_sort(arr_copy, 0, len(arr_copy) - 1)
        
        print(" ")
        print(f"Test Case Type: {case_type}")
        print(" ")
        print(f"Test Case Size: {len(elements)}")
        print(" ")
        print(f"Test Case Contents: {elements}")
        print(" ")
      
        print(f"Comparisons: {comparisons}, Swaps: {swaps}")
        
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
