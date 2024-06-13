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
    """Generate test cases for best, worst, and average cases of Merge Sort."""
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
start=time.perf_counter()
def merge_sort(arr):
    
    count = 0
    swap = 0

    if len(arr) > 1: #1
        count+=1
        mid = len(arr) // 2  # calculate the middle of the array #2
        left_half = arr[:mid]  # divide the array into two halves #2
        right_half = arr[mid:] #2

        #recursive call to merge_sort for both halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0 #3

        #merge the two sorted halves
        while i < len(left_half) and j < len(right_half): #3n
            count+=1
            if left_half[i] < right_half[j]: #3n
                count+=1
                arr[k] = left_half[i] #3n
                swap+=1
                i += 1 #2n
            else:
                arr[k] = right_half[j] #3n
                swap+=1
                j += 1 #2n
            k += 1 #2n

        # check if any elements were left
        while i < len(left_half): #n
            count+=1
            arr[k] = left_half[i] #3n
            swap+=1
            i += 1 #2n
            k += 1 #2n

        while j < len(right_half): #n
            count+=1
            arr[k] = right_half[j] #3n
            swap+=1
            j += 1 #2n
            k += 1 #2n
                
    end=time.perf_counter()
    
    t = (end - start) * 1000

    return count,swap, t

if __name__ == "__main__":
    # Specify the sizes of test cases you want
    test_case_sizes = [100, 500, 1000]

    # Generate test cases
    test_cases = generate_test_cases(test_case_sizes)

    # Sort and print the generated test cases using Merge Sort
    for test_case, case_type in test_cases:
        elements = test_case[:]
        print(" ")
        print(f"Test Case Type: {case_type}")
        print(" ")
        print(f"Test Case Size: {len(elements)}")
        print(" ")
        print(f"Test Case Contents: {elements}")
        print(" ")
        p = merge_sort(elements)
        print(" ")
        print(f"Sorted Result: {elements}\n")
        
        print(" ")
        print(f"Comparisons, Swaps, Runtime: {p}")
        print(" ")
        element_size_bytes = sys.getsizeof(0)
        total_memory_used = element_size_bytes * len(elements)
        print(" ")
        print(f"Total Memory Used: {total_memory_used} bytes")
        print("------------------------")