import random
import time
import sys  # Import the sys module to measure memory usage

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
    comparisons_count = 0  # Initialize the total comparisons count
    swaps_count = 0  # Initialize the total swaps count

    if low < high: #1
        # Optimize pivot selection (median of three)
        comparisons, swaps = median_of_three(arr, low, high)
        comparisons_count += comparisons
        swaps_count += swaps

        # If the size of the subarray is below the threshold, switch to Insertion Sort
        if high - low + 1 <= INSERTION_SORT_THRESHOLD:
            comparisons, swaps = insertion_sort(arr, low, high)
            comparisons_count += comparisons
            swaps_count += swaps
        else:
            # Partition the array and get the pivot index
            pivot_index, pivot_swaps = partition(arr, low, high)
            swaps_count += pivot_swaps

            # Recursively sort the subarrays on both sides of the pivot
            left_comparisons, left_swaps = quick_sort(arr, low, pivot_index - 1)
            right_comparisons, right_swaps = quick_sort(arr, pivot_index + 1, high)

            # Accumulate comparisons and swaps counts
            comparisons_count += left_comparisons + right_comparisons
            swaps_count += left_swaps + right_swaps

    return comparisons_count, swaps_count

def median_of_three(arr, low, high):
    comparisons_count = 0
    mid = (low + high) // 2   #3
    if arr[low] > arr[mid]:   #3
        arr[low], arr[mid] = arr[mid], arr[low]  #6
        comparisons_count += 1     #3  
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]   #6
        comparisons_count += 1  #3
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]   #6
        comparisons_count += 1  #3
    # Place the median value at the last index
    arr[mid], arr[high] = arr[high], arr[mid]   #6
    return comparisons_count, 3  # Three comparisons were made

def partition(arr, low, high):
    swaps_count = 0  # Initialize the total swaps count
    pivot = arr[high]   #3
    i = low - 1 #2

    for j in range(low, high):  #n
        if arr[j] <= pivot: #2n
            i += 1  #2n
            arr[i], arr[j] = arr[j], arr[i] #6n
            swaps_count += 1  # Increment swaps count
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]       #8n
    swaps_count += 1  # Increment swaps count   
    return i + 1, swaps_count  # Return pivot index and swaps count  #2n

def insertion_sort(arr, low, high):
    comparisons_count = 0
    swaps_count = 0
    for i in range(low + 1, high + 1):  #n
        key = arr[i]    #2n
        j = i - 1   #2n
        while j >= low and arr[j] > key:   #4n^2 
            arr[j + 1] = arr[j]     #3n^2
            j -= 1      #2n^2
            comparisons_count += 1
            swaps_count += 1
        arr[j + 1] = key        #3n^2
        swaps_count += 1
    return comparisons_count, swaps_count

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
        print("Total Comparisons: ", comparisons)
        print("Total Swaps: ", swaps)
        
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

