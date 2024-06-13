def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # calculate the middle of the array
        left_half = arr[:mid]  # divide the array into two halves
        right_half = arr[mid:]

        #recursive call to merge_sort for both halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        #merge the two sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # check if any elements were left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

#input
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)

merge_sort(arr)

print("Sorted array:", arr)
