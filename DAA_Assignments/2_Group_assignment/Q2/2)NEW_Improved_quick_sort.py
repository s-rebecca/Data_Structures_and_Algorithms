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

def insertion_sort(arr, low, high):
    count1=0
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            count1+=1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    #return count1
    

def median_of_three(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    return mid

def partition(arr, low, high):
    pivot_index = median_of_three(arr, low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    count_partition=0
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            count_partition+=1
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1, count_partition

def quick_sort(arr, low, high, threshold=10):
    #count1=0
    if low < high:
        #count1+=1
        if high - low <= threshold:
            insertion_sort(arr, low, high)
        else:
            pivot_index, count_partition = partition(arr, low, high)
            quick_sort(arr, low, pivot_index - 1, threshold)
            quick_sort(arr, pivot_index + 1, high, threshold)
    print("comparisons: ", count_partition)

if __name__ == "__main__":
    test_case_sizes = [100, 500, 1000]
    
    for size in test_case_sizes:
        best_case = generate_sorted_array(size)
        worst_case = generate_reverse_sorted_array(size)
        average_case = generate_random_array(size)
        
        test_cases = [
            (best_case, "Best Case"),
            (worst_case, "Worst Case"),
            (average_case, "Average Case")
        ]
        
        for test_case, case_type in test_cases:
            elements = test_case[:]
            start_time = time.perf_counter()
            quick_sort(elements, 0, len(elements) - 1)
            end_time = time.perf_counter()
            
            print(f"Test Case Type: {case_type}")
            print(f"Test Case Size: {len(elements)}")
            print(f"Runtime: {(end_time - start_time) * 1000} milliseconds")
            total_memory_used = sys.getsizeof(elements)
            print(f"Total Memory Used: {total_memory_used} bytes")
            print(f"Sorted Result: {elements}\n")
