import random
import time
import sys
import matplotlib.pyplot as plt

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
        test_cases.append((best_case, "Sorted Case"))

        # Worst case: Reverse sorted array
        worst_case = generate_reverse_sorted_array(size)
        test_cases.append((worst_case, "Reverse Sorted Case"))

        # Average case: Random array
        average_case = generate_random_array(size)
        test_cases.append((average_case, "Random Case"))

    return test_cases

def insertion_sort(arr):
    comparisons_count = 0
    swaps_count = 0
    start = time.perf_counter()
    for i in range(1, len(arr)):   #n 
        key = arr[i]    #2n
        j = i - 1   #2n
        while j >= 0 and key < arr[j]:  #4n^2
            comparisons_count += 1  #2n^2
            arr[j + 1] = arr[j]  #3n^2
            swaps_count += 1    #2n^2
            j -= 1  #2n^2
        arr[j + 1] = key    #3n^2
        swaps_count += 1
    end = time.perf_counter()
    runtime_ms = (end - start) * 1000
    memory_usage = sys.getsizeof(arr) / 1024.0  # In KB
    
    print("No. of Comparisons: ", comparisons_count)
    print("No. of Swaps: ", swaps_count)
    print("Runtime: {:.6f} milliseconds".format(runtime_ms))
    print("Memory Usage: {:.2f} KB".format(memory_usage))
    print("Sorted Result: ", arr)

# ... (previous code)

if __name__ == "__main__":
    # Specify the sizes of test cases you want
    test_case_sizes = [100, 500, 1000]
    test_cases = generate_test_cases(test_case_sizes)
    # Initialize lists to store data for the line graph
    test_case_types = []
    test_case_sizes = []
    running_times = []

    for test_case, case_type in test_cases:
        elements = test_case[:]
        arr_copy = elements.copy()  # Make a copy of the input array to avoid modification
        
        print(f"Test Case Type: {case_type}")
        print(f"Test Case Size: {len(elements)}")
        print(f"Test Case Contents: {elements}")
       
        # Measure the time taken for Insertion Sort
        start_time = time.perf_counter()
        insertion_sort(arr_copy)  # Sort the copy of the input array
        end_time = time.perf_counter()
        running_time_ms = (end_time - start_time) * 1000

        # Append the test case size and running time for the line graph
        test_case_types.append(case_type)
        test_case_sizes.append(len(elements))
        running_times.append(running_time_ms)

        print("------------------------")

    # Create a line graph
    plt.figure(figsize=(10, 6))
    print(test_case_sizes,running_times)
    plt.plot(test_case_sizes[0:3], running_times[0:3], marker='o', linestyle='-', color='b')
    plt.plot(test_case_sizes[3:6], running_times[3:6], marker='o', linestyle='-', color='b')
    plt.plot(test_case_sizes[6:], running_times[6:], marker='o', linestyle='-', color='b')
    plt.title('Running Time vs. Test Case Size')
    plt.xlabel('Test Case Size')
    plt.ylabel('Running Time (milliseconds)')
    plt.grid(True)

    # Annotate data points with test case types
    for i, case_type in enumerate(test_case_types):
        plt.annotate(case_type, (test_case_sizes[i], running_times[i]))

    # Show the line graph
    plt.show()
