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

def partition(arr, p, r):
    count_iff=0 #1
    x = arr[r] #2
    i = p - 1 #2
    for j in range(p, r): #n
        
        if arr[j] <= x: #2n
            i = i + 1 #2n
            arr[i], arr[j] = arr[j], arr[i] #6n
    arr[i + 1], arr[r] = arr[r], arr[i + 1] #8

    return i + 1 #2

def inPlaceQuickSort(arr, first, last):
    stack = [(first, last)]
    count_if=0 #1

    start=time.perf_counter()
    
    while stack:
        
        first, last = stack.pop()
        count_if+=1 #2
        if first < last:
            pivotIndex = partition(arr, first, last)
            
            # Push subproblems onto the stack
            stack.append((first, pivotIndex - 1))
            stack.append((pivotIndex + 1, last))
    

    end=time.perf_counter()
    print("no of comparisons in sort: ", count_if)
    #print("no of comaprisons: ",count+1)
    print("no of swaps: ", count_if-1)
    print("runtime: ", (end-start)*1000)
    element_size_bytes = sys.getsizeof(0)
    print("memory used for 100 elements: ", element_size_bytes * 100)
    print("memory used for 500 elements: ", element_size_bytes * 500)
    print("memory used for 1000 elements: ", element_size_bytes * 1000)

if __name__ == "__main__":
    # Specify the sizes of test cases you want
    test_case_sizes = [100, 500, 1000]

    # Generate test cases
    test_cases = generate_test_cases(test_case_sizes)

    # Print and analyze the generated test cases
    for test_case, case_type in test_cases:
        print(f"Test Case Type: {case_type}")
        print(f"Test Case Size: {len(test_case)}")
        print(f"Test Case Contents: {test_case}\n")

    # Sort and print the generated test cases using In-Place Quick Sort
    for test_case, case_type in test_cases:
        elements = test_case[:]
        inPlaceQuickSort(elements, 0, len(elements) - 1)
        print(f"Test Case Type: {case_type}")
        print(f"Test Case Size: {len(elements)}")
        print(f"Sorted Result: {elements}\n")