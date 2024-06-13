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
    """Generate test cases for best, worst, and average cases of Bucket Sort."""
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

def insertion_sort(arr):
    count=0
    swap=0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            #count+=1
            arr[j + 1] = arr[j]
            #swap+=1
            j -= 1
        arr[j + 1] = key
    return count,swap

def bucket_sort(arr):
    # Create empty buckets
    n = len(arr)
    max_val = max(arr)
    min_val = min(arr)
    bucket_range = (max_val - min_val) / n
    buckets = [[] for _ in range(n)]

    # Put elements into buckets
    for i in range(n):
        index = int((arr[i] - min_val) / bucket_range)
        if index != n:
            buckets[index].append(arr[i])
        else:
            buckets[n - 1].append(arr[i])

    # Sort each bucket using insertion sort
    for i in range(n):
        insertion_sort(buckets[i])

    swaps=0
    # Concatenate the sorted buckets
    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            #swaps+=1
            arr[k] = buckets[i][j]
            k += 1
    #print("comparisons: ", c)
    #print("swaps: ", swaps+s)

if __name__ == "__main__":
    # Specify the sizes of test cases you want
    test_case_sizes = [100, 500, 1000]

    # Generate test cases
    test_cases = generate_test_cases(test_case_sizes)

    for test_case, case_type in test_cases:
        elements = test_case[:]
        arr_copy = elements.copy()  # Make a copy of the input array to avoid modification
        bucket_sort(arr_copy)
        
        print(" ")
        print(f"Test Case Type: {case_type}")
        print(" ")
        print(f"Test Case Size: {len(elements)}")
        print(" ")
        print(f"Test Case Contents: {elements}")
        print(" ")
      
        
        # Measure runtime
        start_time = time.perf_counter()
        bucket_sort(elements)
        end_time = time.perf_counter()
        runtime_ms = (end_time - start_time) * 1000
        print("Runtime: {:.6f} milliseconds".format(runtime_ms))
        
        # Measure memory usage
        memory_usage = sys.getsizeof(elements)
        print("Memory Usage: {:.2f} KB".format(memory_usage / 1024.0))
        
        print(f"Sorted Result: {elements}\n")
        print("------------------------")
