def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)  # Sort elements before pivot
        quick_sort(arr, pivot_index + 1, high)  # Sort elements after pivot

def partition(arr, low, high):
    pivot = arr[high]  # Choosing the pivot element (last element)
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot with element at correct index
    return i + 1  # Return the final position of the pivot


inp = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
quick_sort(inp, 0, len(inp) - 1)
print(inp)
