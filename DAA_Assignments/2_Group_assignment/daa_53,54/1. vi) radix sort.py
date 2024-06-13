import random
import time
import psutil

# Function to perform counting sort on a specific digit (exp)
def counting_sort(arr, exp, comparisons, basic_operations):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
        basic_operations[0] += 1  # Increment basic operations count (for the index calculation)

    for i in range(1, 10):
        count[i] += count[i - 1]
        basic_operations[0] += 1  # Increment basic operations count (for count array updates)

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
        basic_operations[0] += 3  # Increment basic operations count (for assignments, decrements, and comparisons)

    for i in range(n):
        arr[i] = output[i]
        basic_operations[0] += 1  # Increment basic operations count (for assignments)
        comparisons[0] += 1  # Increment comparisons count (for comparing elements in the array)

# Function to perform Radix Sort
def radix_sort(arr):
    max_value = max(arr)
    exp = 1
    comparisons = [0]
    basic_operations = [0]

    while max_value // exp > 0:
        counting_sort(arr, exp, comparisons, basic_operations)
        exp *= 10

    return arr, comparisons[0], basic_operations[0]

# Function to generate a random array of a given size
def generate_random_array(size):
    return [random.randint(1, 100000) for _ in range(size)]

# Function to generate a sorted array in the best-case scenario
def generate_best_case_array(size):
    return list(range(1, size + 1))

# Function to generate a reverse-sorted array in the worst-case scenario
def generate_worst_case_array(size):
    return list(range(size, 0, -1))

# Sizes for test cases
test_sizes = [100, 500, 1000]

for size in test_sizes:
    # Generate random input test case
    random_array = generate_random_array(size)
    
    # Display the input test case
    print(f"Input Test Case (Size {size}):")
    print(random_array)

    # Measure running time
    start_time = time.time()

    # Perform Radix Sort
    sorted_arr, comparisons, basic_operations = radix_sort(random_array)

    # Calculate running time in milliseconds
    end_time = time.time()
    running_time_ms = (end_time - start_time) * 1000

    # Calculate memory usage
    memory_used_bytes = psutil.Process().memory_info().rss

    # Display the sorted array, metrics, and memory usage for the current test case
    print("\nSorted Array:")
    print(sorted_arr)
    print("Running time (milliseconds):", running_time_ms)
    print("Memory used (bytes):", memory_used_bytes)
    print("Number of comparisons:", comparisons)
    print("Number of basic operations:", basic_operations)
    print("\n" + "=" * 40 + "\n")

    # Generate best-case input test case
    best_case_array = generate_best_case_array(size)
    
    # Measure running time for best-case scenario
    start_time = time.time()

    # Perform Radix Sort for best-case scenario
    sorted_arr, comparisons, basic_operations = radix_sort(best_case_array)

    # Calculate running time in milliseconds for best-case scenario
    end_time = time.time()
    running_time_ms = (end_time - start_time) * 1000

    # Calculate memory usage for best-case scenario
    memory_used_bytes = psutil.Process().memory_info().rss

    # Display the sorted array, metrics, and memory usage for the best-case scenario
    print(f"Best-case Input Test Case (Size {size}):")
    print(best_case_array)
    print("Sorted Array (Best-case):")
    print(sorted_arr)
    print("Running time (milliseconds, Best-case):", running_time_ms)
    print("Memory used (bytes, Best-case):", memory_used_bytes)
    print("Number of comparisons:", comparisons)
    print("Number of basic operations:", basic_operations)
    print("\n" + "=" * 40 + "\n")

    # Generate worst-case input test case
    worst_case_array = generate_worst_case_array(size)
    
    # Measure running time for worst-case scenario
    start_time = time.time()

    # Perform Radix Sort for worst-case scenario
    sorted_arr, comparisons, basic_operations = radix_sort(worst_case_array)

    # Calculate running time in milliseconds for worst-case scenario
    end_time = time.time()
    running_time_ms = (end_time - start_time) * 1000

    # Calculate memory usage for worst-case scenario
    memory_used_bytes = psutil.Process().memory_info().rss

    # Display the sorted array, metrics, and memory usage for the worst-case scenario
    print(f"Worst-case Input Test Case (Size {size}):")
    print(worst_case_array)
    print("Sorted Array (Worst-case):")
    print(sorted_arr)
    print("Running time (milliseconds, Worst-case):", running_time_ms)
    print("Memory used (bytes, Worst-case):", memory_used_bytes)
    print("Number of comparisons:", comparisons)
    print("Number of basic operations:", basic_operations)
    print("\n" + "=" * 40 + "\n")


