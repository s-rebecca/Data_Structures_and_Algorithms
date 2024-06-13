def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr, num_buckets):
    min_val = min(arr)
    max_val = max(arr)
    
    bucket_range = (max_val - min_val) / num_buckets
    buckets = [[] for _ in range(num_buckets)]
    
    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index >= num_buckets:  # Handle the case where the index goes beyond the last bucket
            index = num_buckets - 1
        buckets[index].append(num)
    
    for bucket in buckets:
        insertion_sort(bucket)
    
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)
    
    return sorted_array

# Example usage
input_list = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
num_buckets = 5
sorted_list = bucket_sort(input_list, num_buckets)
print(sorted_list)
