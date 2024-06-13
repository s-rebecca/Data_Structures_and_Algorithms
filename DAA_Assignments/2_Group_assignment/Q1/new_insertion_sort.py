import time
def insertion_sort(arr):
    start=time.perf_counter()
    for i in range(1, len(arr)): #n
        key = arr[i] #2n
        j = i - 1 #2n
        count=0 #n
        while j >= 0 and key < arr[j]: #4n^2
            arr[j + 1] = arr[j] #3n^2
            j -= 1 #2n^2
            count+=1 #2n^2
        arr[j + 1] = key #3n^2
    end=time.perf_counter()
    print("no of comaprisons: ",count+1)
    print("no of swaps: ", count)
    print("runtime: ", (end-start)*1000)

# File path
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
            insertion_sort(elements)
            
            # Print the sorted result
            print("Sorted:", elements)

except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")