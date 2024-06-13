def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Counting array for digits 0-9

    # Count occurrences of each digit at the current exp position
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count to store the position of the next occurrence
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array using the count array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the sorted elements back to the original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1  # Initialize the current digit position

    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10  # Move to the next digit position

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
            elements = [int(x) for x in line.strip().split()]
            
            # Sort the elements using radix sort
            radix_sort(elements)
            
            # Print the sorted result
            print("Sorted:", elements)

except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
