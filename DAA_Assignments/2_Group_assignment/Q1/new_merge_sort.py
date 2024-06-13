import time
start=time.perf_counter()
def merge_sort(arr):
    count=0
    swap=0
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
    t=(end-start)*1000
    return count,swap,t

# Function to read data from a file and return it as a list of integers
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
            
            # Sort the elements using insertion sort
            res=merge_sort(elements)
            
            # Print the sorted result
            print("comparisons, swaps, time used: ",res)
            print("Sorted:", elements)

except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")