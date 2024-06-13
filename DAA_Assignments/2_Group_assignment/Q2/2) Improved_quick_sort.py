import random
import time

# Threshold for switching to Insertion Sort
INSERTION_SORT_THRESHOLD = 10

def quick_sort(arr, low, high):
    count=0
    start=time.perf_counter()
    if low < high: #1
        # Optimize pivot selection (median of three)
        count1_total=median_of_three(arr, low, high)
        count+=1
        
        # If the size of the subarray is below the threshold, switch to Insertion Sort
        if high - low + 1 <= INSERTION_SORT_THRESHOLD:
            count+=1
            count2_total_swap_total=insertion_sort(arr, low, high)
        else:
            # Partition the array and get the pivot index
            pivot_index = partition(arr, low, high)
            
            # Recursively sort the subarrays on both sides of the pivot
            quick_sort(arr, low, pivot_index['part_val'] - 1)
            quick_sort(arr, pivot_index['part_val'] + 1, high)
    end=time.perf_counter()
    print("runtime: ", (end-start)*1000)
    print("total comparisons: ",count+count1_total+count2_total_swap_total['count2_val'])
    print("no of swaps: ", pivot_index['swap_val']+count2_total_swap_total['swap_val'])

def median_of_three(arr, low, high):
    count1=0
    mid = (low + high) // 2 #3
    if arr[low] > arr[mid]: #3
        count1+=1
        arr[low], arr[mid] = arr[mid], arr[low] #6
    if arr[low] > arr[high]: #3
        count1+=1
        arr[low], arr[high] = arr[high], arr[low] #6
    if arr[mid] > arr[high]: #3
        count1+=1
        arr[mid], arr[high] = arr[high], arr[mid] #6
    # Place the median value at the last index
    arr[mid], arr[high] = arr[high], arr[mid] #6
    return count1 #number of comparisons in the function

def partition(arr, low, high):
    swap1=0
    pivot = arr[high] #3 # Pivot is now the median value
    i = low - 1  #2 # Index of the smaller element

    for j in range(low, high):#n
        if arr[j] <= pivot: #2n
            i += 1 #2n
            
            arr[i], arr[j] = arr[j], arr[i]  #6n # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  #8 # Swap pivot with the element at (i + 1)
    swap1+=1
    return {'part_val':i + 1, 'swap_val':swap1} #2

def insertion_sort(arr, low, high):
    count2=0
    swap2=0
    for i in range(low + 1, high + 1): #n
        key = arr[i] #2n
        j = i - 1 #2n
        while j >= low and arr[j] > key: #4n^2
            count2+=1
            swap2+=1
            arr[j + 1] = arr[j] #3n^2
            j -= 1 #2n^2
        arr[j + 1] = key #3n^2
    return {'count2_val':count2, 'swap_val':swap2} #number of comparisons in the function

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
            
            # Sort the elements using quick sort with insertion sort for small subarrays
            quick_sort(elements, 0, len(elements) - 1)
            
            # Print the sorted result
            print("Sorted:", elements)

except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
