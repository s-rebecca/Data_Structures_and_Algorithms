def bucket_sort(arr):
    # Create empty buckets
    n = len(arr) #1
    max_val = max(arr) #1
    min_val = min(arr)#1
    bucket_range = (max_val - min_val) / n #3
    buckets = [[] for _ in range(n)] #2n

    # Put elements into buckets
    for i in range(n): #n
        index = int((arr[i] - min_val) / bucket_range) #4n
        if index != n: #n
            buckets[index].append(arr[i]) #2n
        else:
            buckets[n - 1].append(arr[i]) #3n

    # Sort each bucket using insertion sort and count comparisons and swaps
    comparisons = 0
    swaps = 0
    for i in range(n): #n
        comparisons_bucket, swaps_bucket = insertion_sort(buckets[i]) #2n
        comparisons += comparisons_bucket #2n
        swaps += swaps_bucket #2n

    # Concatenate the sorted buckets
    k = 0
    for i in range(n): #n
        for j in range(len(buckets[i])): #n^2
            arr[k] = buckets[i][j] #3n^2
            k += 1

    print(f"Comparisons: {comparisons}, Swaps: {swaps}")
