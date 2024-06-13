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
    """Generate test cases for best, worst, and average cases of Bucket Sort."""
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
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort(arr):
    # Create empty buckets
    n = len(arr) #1
    max_val = max(arr) #1
    min_val = min(arr)#1
    bucket_range = (max_val - min_val) / n  #3
    buckets = [[] for _ in range(n)]    #2n

    # Put elements into buckets
    for i in range(n):  #n
        index = int((arr[i] - min_val) / bucket_range)  #4n
        if index != n:
            buckets[index].append(arr[i]) #2n
        else:
            buckets[n - 1].append(arr[i])    #3n

    # Sort each bucket using insertion sort
    for i in range(n): #n
        insertion_sort(buckets[i])  #2n

    # Concatenate the sorted buckets
    k = 0
    for i in range(n):  #n
        for j in range(len(buckets[i])):    #n^2
            arr[k] = buckets[i][j]  #3n^2
            k += 1

if __name__ == "__main__":
    # Specify the sizes of test cases you want
    test_case_sizes = [100, 500, 1000]

    # Generate test cases
    test_cases = generate_test_cases(test_case_sizes)

    test_case_types = []
    test_case_sizes = []
    running_times = []


    for test_case, case_type in test_cases:
        elements = test_case[:]
        arr_copy = elements.copy()  # Make a copy of the input array to avoid modification
        bucket_sort(arr_copy)
        
       
        print(f"Test Case Type: {case_type}")
        
        print(f"Test Case Size: {len(elements)}")
   
        print(f"Test Case Contents: {elements}")
      
        
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
        test_case_types.append(case_type)
        test_case_sizes.append(len(elements))
        running_times.append(runtime_ms)
        print("------------------------")

    plt.figure(figsize=(10, 6))
    print(test_case_sizes,runtime_ms)
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