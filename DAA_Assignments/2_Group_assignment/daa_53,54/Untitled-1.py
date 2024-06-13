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
        test_cases.append((best_case, "Best Case"))

        # Worst case: Reverse sorted array
        worst_case = generate_reverse_sorted_array(size)
        test_cases.append((worst_case, "Worst Case"))

        # Average case: Random array
        average_case = generate_random_array(size)
        test_cases.append((average_case, "Average Case"))

    return test_cases

comparison_count = 0
swap_count = 0

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

def inPlaceQuickSort(arr, first, last):
    stack = [(first, last)]
    
    start=time.perf_counter()

    while stack:
        first, last = stack.pop()

        if first < last:
            pivotIndex = partition(arr, first, last)
        

            # Push subproblems onto the stack
            stack.append((first, pivotIndex - 1))
            stack.append((pivotIndex + 1, last))

    
    end = time.perf_counter()
    
   
    element_size_bytes = sys.getsizeof(0)
    total_memory_used = sum([element_size_bytes * len(test_case) for test_case, _ in generate_test_cases([100, 500, 1000])])
    
    print(f"Total Memory Used: {total_memory_used} bytes")
  
    return (end - start) * 1000
    
if __name__ == "__main__":
    # Specify the sizes of test cases you want
    test_case_sizes = [100, 500, 1000]
    runtimes = []

    # Generate test cases
    test_cases = generate_test_cases(test_case_sizes)

    # Sort and print the generated test cases using In-Place Quick Sort
    for test_case, case_type in test_cases:
        elements = test_case[:]
      
        print(f"Test Case Type: {case_type}")
      
        print(f"Test Case Size: {len(elements)}")
      
        print(f"Test Case Contents: {elements}")
      
        inPlaceQuickSort(elements, 0, len(elements) - 1) 
        runtime = inPlaceQuickSort(elements, 0, len(elements) - 1)
        runtimes.append(runtime)
# Scatter plot the input data
        

        
        
      
        print(f"Comparisons: {comparison_count}")
        print(f"Swaps: {swap_count}")
        print(f"Runtime: {runtime} milliseconds")
      
        print(f"Sorted Result: {elements}\n")
        print("------------------------")

    plt.plot(runtimes, test_case_sizes, color='red', label='Linear Regression Line')  # 1 mark

    plt.show()