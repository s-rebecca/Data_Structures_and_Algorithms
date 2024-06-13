def insertion_sort(arr):
    count=0
    swap=0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            count+=1
            arr[j + 1] = arr[j]
            swap+=1
            j -= 1
        arr[j + 1] = key

def bucket_sort(arr):
    # Create empty buckets
    n = len(arr)
    max_val = max(arr)
    min_val = min(arr)
    bucket_range = (max_val - min_val) / n
    buckets = [[] for _ in range(n)]

    # Put elements into buckets
    for i in range(n):
        index = int((arr[i] - min_val) / bucket_range)
        if index != n:
            buckets[index].append(arr[i])
        else:
            buckets[n - 1].append(arr[i])

    # Sort each bucket using insertion sort
    for i in range(n):
        insertion_sort(buckets[i])

    # Concatenate the sorted buckets
    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1

# Your input file path
file_path = r'C:\Users\HP\OneDrive - Amrita Vishwa Vidyapeetham\5th sem\19CSE302 DAA\Assignments\2_Group_assignment\input.txt'

try:
    with open(file_path, 'r') as file:
        # Read the data
        data = file.readlines()

        print(data)

        # Process each test case
        for line in data:
            # Convert the line to a list of integers
            elements = [float(x) for x in line.strip().split()]
            
            # Sort the elements using bucket sort
            bucket_sort(elements)
            
            # Print the sorted result
            print("Sorted:", elements)

except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
