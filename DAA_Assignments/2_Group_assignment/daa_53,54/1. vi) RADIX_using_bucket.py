import random
import time
import psutil

def bucket_sort(arr):
    max_value = max(arr)

    buckets = [[] for _ in range(10)]

    num_digits = len(str(max_value)) #number of digits in max value

    for digit_place in range(num_digits):
        #placing elements into buckets based on the current digit
        for num in arr:
            digit = (num // 10 ** digit_place) % 10
            buckets[digit].append(num)

        #merge the elements from the buckets
        arr = [num for bucket in buckets for num in bucket]

        #clear the buckets for the next pass
        buckets = [[] for _ in range(10)]

    return arr

def generate_random_array(size):
    return [random.randint(1, 100000) for _ in range(size)]

def generate_best_case_array(size):
    return list(range(1, size + 1))

def generate_worst_case_array(size):
    return list(range(size, 0, -1))

test_sizes = [100, 500, 1000]

for size in test_sizes:
    random_array = generate_random_array(size)
    print(f"Input Test Case (Size {size}):")
    print(random_array)

    start_time = time.time()
    sorted_arr = bucket_sort(random_array)
    end_time = time.time()
    running_time_ms = (end_time - start_time) * 1000
    memory_used_bytes = psutil.Process().memory_info().rss

    print("\nSorted Array:")
    print(sorted_arr)
    print("Running time (milliseconds):", running_time_ms)
    print("Memory used (bytes):", memory_used_bytes)
    print("\n" + "=" * 40 + "\n")

    best_case_array = generate_best_case_array(size)
    start_time = time.time()
    sorted_arr = bucket_sort(best_case_array)
    end_time = time.time()
    running_time_ms = (end_time - start_time) * 1000
    memory_used_bytes = psutil.Process().memory_info().rss

    print(f"Best-case Input Test Case (Size {size}):")
    print(best_case_array)
    print("Sorted Array (Best-case):")
    print(sorted_arr)
    print("Running time (milliseconds, Best-case):", running_time_ms)
    print("Memory used (bytes, Best-case):", memory_used_bytes)
    print("\n" + "=" * 40 + "\n")

    worst_case_array = generate_worst_case_array(size)
    start_time = time.time()
    sorted_arr = bucket_sort(worst_case_array)
    end_time = time.time()
    running_time_ms = (end_time - start_time) * 1000
    memory_used_bytes = psutil.Process().memory_info().rss

    print(f"Worst-case Input Test Case (Size {size}):")
    print(worst_case_array)
    print("Sorted Array (Worst-case):")
    print(sorted_arr)
    print("Running time (milliseconds, Worst-case):", running_time_ms)
    print("Memory used (bytes, Worst-case):", memory_used_bytes)
    print("\n" + "=" * 40 + "\n")
