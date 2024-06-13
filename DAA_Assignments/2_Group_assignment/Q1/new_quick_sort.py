def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)
        
        # Recursively sort the subarrays on both sides of the pivot
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Choose the rightmost element as the pivot
    i = low - 1  # Index of the smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot with the element at (i + 1)
    return i + 1

file_path = r'C:\Users\HP\OneDrive - Amrita Vishwa Vidyapeetham\5th sem\19CSE302 DAA\Assignments\2_Group_assignment\input.txt'

try:
    with open(file_path, 'r') as file:
        # Read the data
        data = file.readlines()

        print(data)

        # Process each test case
        for line in data:
            # Convert the line to a list of integers
            elements = [int(x) for x in line.strip().split()]
            
            # Sort the elements using quick sort
            quick_sort(elements, 0, len(elements) - 1)
            
            # Print the sorted result
            print("Sorted:", elements)

except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
