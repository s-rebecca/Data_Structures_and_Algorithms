import random
import time
import psutil

# Function to perform MAX_HEAPIFY with counting comparisons and swaps
def MAX_HEAPIFY(A, i, heap_size, comparisons, swaps, primitive_operations):
    left = 2 * i
    right = 2 * i + 1
    largest = i

    if left <= heap_size:
        comparisons[0] += 1  # Increment comparisons count (O(1) operation)
        primitive_operations[0] += 1  # Increment primitive operations count
        if A[left - 1] > A[largest - 1]:
            largest = left

    if right <= heap_size:
        comparisons[0] += 1  # Increment comparisons count (O(1) operation)
        primitive_operations[0] += 1  # Increment primitive operations count
        if A[right - 1] > A[largest - 1]:
            largest = right

    if largest != i:
        A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1]
        swaps[0] += 1  # Increment swaps count (O(1) operation)
        primitive_operations[0] += 3  # Increment primitive operations count by 3 (two assignments and a swap)
        MAX_HEAPIFY(A, largest, heap_size, comparisons, swaps, primitive_operations)

# Function to build a max heap with counting comparisons and swaps
def BUILD_MAX_HEAP(A, comparisons, swaps, primitive_operations):
    heap_size = len(A)
    for i in range(heap_size // 2, 0, -1):
        MAX_HEAPIFY(A, i, heap_size, comparisons, swaps, primitive_operations)

# Function to perform inplace heap sort with counting comparisons and swaps
def inplace_heapsort(A, comparisons, swaps, primitive_operations):
    BUILD_MAX_HEAP(A, comparisons, swaps, primitive_operations)
    heap_size = len(A)
    for i in range(heap_size, 1, -1):
        A[0], A[i - 1] = A[i - 1], A[0]
        swaps[0] += 1  # Increment swaps count (O(1) operation)
        primitive_operations[0] += 3  # Increment primitive operations count by 3 (two assignments and a swap)
        heap_size -= 1
        MAX_HEAPIFY(A, 1, heap_size, comparisons, swaps, primitive_operations)

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
    


# ... (previous code for heap sort and utility functions)

if __name__ == "__main__":
    # Specify the sizes of test cases you want
    test_case_sizes = [100, 500, 1000]

    # Generate test cases
    test_cases = generate_test_cases(test_case_sizes)

    # Sort and print the generated test cases using In-Place Heap Sort
    for test_case, case_type in test_cases:
        elements = test_case[:]
        print(" ")
        print(f"Test Case Type: {case_type}")
        print(" ")
        print(f"Test Case Size: {len(elements)}")
        print(" ")
        print(f"Test Case Contents: {elements}")
        print(" ")

        # Initialize counters for comparisons, swaps, and primitive operations
        comparisons = [0]
        swaps = [0]
        primitive_operations = [0]

        # Measure running time
        start_time = time.time()

        # Perform Inplace Heap Sort with counting
        inplace_heapsort(elements, comparisons, swaps, primitive_operations)  # Overall time complexity: O(n log n)

        # Calculate running time in milliseconds
        end_time = time.time()
        running_time_ms = (end_time - start_time) * 1000

        # Calculate memory usage
        memory_used_bytes = psutil.Process().memory_info().rss

        # Display the sorted array, metrics, and memory usage for the current test case
        print("\nSorted Array:")
        print(elements)
        print("Number of comparisons (Θ(n log n)): O(n log n):", comparisons[0])
        print("Number of swaps (Θ(n log n)): O(n log n):", swaps[0])
        print("Number of primitive operations:", primitive_operations[0])
        print("Running time (milliseconds):", running_time_ms)
        print("Memory used (bytes):", memory_used_bytes)
        print("\n------------------------")

