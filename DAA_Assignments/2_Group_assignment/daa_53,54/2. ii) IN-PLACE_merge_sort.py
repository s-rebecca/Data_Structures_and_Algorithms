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

def insertion_sort(arr, low, high):
    count = 0
    swap = 0

    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1

        while j >= low and arr[j] > key:
            count += 1
            arr[j + 1] = arr[j]
            swap += 1
            j -= 1

        arr[j + 1] = key
        swap += 1

    return count, swap

def inplace_merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2

        # Sort left and right halves
        inplace_merge_sort(arr, start, mid)
        inplace_merge_sort(arr, mid + 1, end)

        # Merge the sorted halves using the "two-pointer merge" technique
        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    left_end = mid
    right_start = mid + 1

    # If the last element of the left subarray is less than or equal to the first element of the right subarray,
    # it's already sorted, and we can skip the merge step.
    if arr[left_end] <= arr[right_start]:
        return

    while start <= left_end and right_start <= end:
        # If the current element in the left subarray is less than or equal to the element in the right subarray,
        # move the left pointer forward.
        if arr[start] <= arr[right_start]:
            start += 1
        else:
            value = arr[right_start]

            # Shift the elements in the left subarray to the right to make space for the current element from the right subarray.
            for i in range(right_start, start, -1):
                arr[i] = arr[i - 1]

            arr[start] = value

            start += 1
            left_end += 1
            right_start += 1


if __name__ == "__main__":
    # Specify the sizes of test cases you want
    test_case_sizes = [100, 500, 1000]

    # Generate test cases
    test_cases = generate_test_cases(test_case_sizes)

    # Sort and print the generated test cases using In-Place Merge Sort
    for test_case, case_type in test_cases:
        elements = test_case[:]
        print(" ")
        print(f"Test Case Type: {case_type}")
        print(" ")
        print(f"Test Case Size: {len(elements)}")
        print(" ")
        print(f"Test Case Contents: {elements}")
        print(" ")

        start_time = time.perf_counter()  # Start measuring runtime
        inplace_merge_sort(elements, 0, len(elements) - 1)
        end_time = time.perf_counter()  # Stop measuring runtime

        print(" ")
        print(f"Sorted Result: {elements}\n")
        print(" ")

        runtime_ms = (end_time - start_time) * 1000
        print(f"Runtime: {runtime_ms} milliseconds")

        element_size_bytes = sys.getsizeof(0)
        total_memory_used = element_size_bytes * len(elements)
        print(" ")
        print(f"Total Memory Used: {total_memory_used} bytes")
        print("------------------------")
