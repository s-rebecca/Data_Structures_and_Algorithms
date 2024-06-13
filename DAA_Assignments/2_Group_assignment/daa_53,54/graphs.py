import random
import timeit
import matplotlib.pyplot as plt
import signal

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("Timeout")

# Set the time limit (in seconds) for each sorting algorithm
time_limit = 5  # You can adjust this as needed

# Define a function to run a sorting algorithm within a time limit
def run_sort_algorithm(sort_func, input_data):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(time_limit)

    try:
        start_time = timeit.default_timer()
        sort_func(input_data)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        signal.alarm(0)  # Cancel the alarm
        return execution_time
    except TimeoutException:
        return float('inf')
# Define the sorting functions


def insertion_sort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return comparisons

def merge_sort(arr):
    comparisons = [0]

    def merge(arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        left_arr = [0] * n1
        right_arr = [0] * n2

        for i in range(n1):
            left_arr[i] = arr[left + i]
        for j in range(n2):
            right_arr[j] = arr[mid + 1 + j]

        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            comparisons[0] += 1
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = right_arr[j]
            j += 1
            k += 1

    def merge_sort_helper(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid + 1, right)
            merge(arr, left, mid, right)

    merge_sort_helper(arr, 0, len(arr) - 1)
    return comparisons[0]

def partition(arr, p, r):
    global comparison_count, swap_count  # Declare them as global

    x = arr[r]  # Choose pivot
    i = p - 1

    for j in range(p, r):
        # Increment comparison count
        comparison_count += 1

        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
            swap_count += 1  # Increment swap count

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    swap_count += 1  # Increment swap count

    return i + 1

def inPlaceQuickSort(arr):
    first = arr[0]
    last = arr[-1]
    stack = [(first, last)]
    
    

    while stack:
        first, last = stack.pop()

        if first < last:
            pivotIndex = partition(arr, first, last)
        

            # Push subproblems onto the stack
            stack.append((first, pivotIndex - 1))
            stack.append((pivotIndex + 1, last))


def radix_sort(arr):
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            arr[i] = output[i]

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Implement Bucket Sort
def bucket_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    bucket_range = (max_val - min_val) / len(arr)
    buckets = [[] for _ in range(len(arr))]

    for i in range(len(arr)):
        index = int((arr[i] - min_val) / bucket_range)
        if index != len(arr):
            buckets[index].append(arr[i])
        else:
            buckets[len(arr) - 1].append(arr[i])

    k = 0
    for i in range(len(arr)):
        insertion_sort(buckets[i])
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1

# Generate worst-case input data
def generate_worst_case_data(size):
    return list(range(size, 0, -1))

# Define sorting functions to test
sorting_functions = [
   
    insertion_sort,
    merge_sort,
    inPlaceQuickSort,
    radix_sort,
    bucket_sort
]
if __name__ == "__main__":
    # Test different sorting algorithms for worst-case scenarios
    sizes = [100, 500, 1000]  # Adjust the input sizes as needed
    results = {}

    for sort_func in sorting_functions:
        runtimes = []
        for size in sizes:
            input_data = generate_worst_case_data(size)
            start_time = timeit.default_timer()  # Start the timer
            sort_func(input_data)
            end_time = timeit.default_timer()  # End the timer
            execution_time = end_time - start_time
            runtimes.append(execution_time)
        results[sort_func.__name__] = runtimes

    # Create a graph to compare sorting algorithms based on runtime
    plt.figure(figsize=(10, 6))

    for sort_func_name, runtimes in results.items():
        plt.plot(sizes, runtimes, marker='o', label=sort_func_name)

    plt.title('Comparison of Sorting Algorithms')
    plt.xlabel('Input Size')
    plt.ylabel('Runtime (seconds)')
    plt.yscale('log')  # Use a logarithmic scale for better visualization
    plt.legend(loc='upper left')
    plt.grid(True)

    # Show the graph
    plt.show()