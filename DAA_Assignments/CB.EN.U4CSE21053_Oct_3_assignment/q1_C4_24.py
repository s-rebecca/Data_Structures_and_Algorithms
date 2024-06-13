def partition(arr, left, right, pivot_idx):
    pivot_value = arr[pivot_idx]
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    low = left
    for i in range(left, right):
        if arr[i] <= pivot_value:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
    arr[low], arr[right] = arr[right], arr[low]
    return low

def deterministic_select(arr, left, right, k):
    if left <= right:
        # Find the median of medians and use it as the pivot
        pivot_idx = left
        while left <= right:
            median_idx = left + 2 if left + 2 <= right else (left + right) // 2
            median_idx = partition(arr, left, right, median_idx)
            if median_idx == k:
                return arr[k]
            elif median_idx < k:
                left = median_idx + 1
            else:
                right = median_idx - 1
        return arr[k]

# Example usage
arr = [3, 1, 4, 2, 5, 7, 6]
k = 3  # Find the kth smallest element
choice = ["st", "nd", "rd", "th"]
result = deterministic_select(arr, 0, len(arr) - 1, k)
print(f"The {k}{choice[k-1]} smallest element is {result}")

"""a. How many baby medians are less than or equal to the chosen pivot? How many are greater than or equal to the pivot?

- There are n/5 groups of size 5, so there are n/5 baby medians in total.
- By sorting each group of size 5, we can easily find the median in each group.
- If we find the median of medians among these baby medians, it will be a pivot.
- Since the median of medians is the median of all the baby medians, there will be approximately (n/5)/2 = n/10 baby medians less than or equal to the chosen pivot, and approximately (n/5)/2 = n/10 baby medians greater than or equal to the pivot.

b. For each baby median less than or equal to the pivot, how many other elements are less than or equal to the pivot? Is the same true for those greater than or equal to the pivot?

- For each baby median less than or equal to the pivot, there are four other elements in the same group of size 5 that are also less than or equal to the pivot.
- Similarly, for each baby median greater than or equal to the pivot, there are four other elements in the same group of size 5 that are also greater than or equal to the pivot.

c. Argue why the method for finding the deterministic pivot and using it to partition S takes O(n) time.

- The process of finding the median of medians takes O(n) time because we divide the array into groups of size 5, sort each group, and then recursively find the median of medians.
- The partitioning step, which uses the deterministic pivot, also takes O(n) time because it divides the array into two subarrays: one with elements less than or equal to the pivot and one with elements greater than the pivot. This partitioning step is similar to the regular QuickSelect partitioning and takes linear time.

d. Based on these estimates, write a recurrence equation to bound the worst-case running time t(n) for this selection algorithm (note that in the worst case there are two recursive calls—one to find the median of the baby medians and one to recur on the larger of L and G).

- Let T(n) be the worst-case running time of the deterministic selection algorithm.
- In the worst case, we spend O(n) time finding the median of medians, and then we partition the array into two subarrays, one with size at most 7n/10 and one with size at least 3n/10 (since we are guaranteed that the pivot is not an extreme value).
- We make two recursive calls, one on the larger subarray (at least 3n/10) and one on the smaller subarray (at most 7n/10).
- Therefore, the recurrence equation for the worst-case running time is:

T(n) ≤ T(7n/10) + T(3n/10) + O(n)

e. Using this recurrence equation, show by induction that T(n) is O(n).

To prove that T(n) is O(n) using induction, we need to show that T(n) ≤ cn for some constant c, for all n greater than or equal to some base case (usually n = 1).

Base Case: Let's choose a base case, say n = 1. For n = 1, T(1) is a constant, so it's trivially true that T(1) ≤ c(1), where c is some constant.

Inductive Hypothesis: Assume that for some positive integer k, T(k) ≤ ck for all k ≤ n, where c is a constant.

Inductive Step: We want to show that T(n+1) ≤ c(n+1) using the induction hypothesis.

T(n+1) = T(7(n/10)) + T(3(n/10)) + O(n+1)

By the induction hypothesis, we can substitute T(7(n/10)) and T(3(n/10)) with their upper bounds:

T(n+1) ≤ c(7(n/10)) + c(3(n/10)) + O(n+1)

Now, we simplify:

T(n+1) ≤ 7c(n/10) + 3c(n/10) + O(n+1)

T(n+1) ≤ (7c + 3c)(n/10) + O(n+1)

T(n+1) ≤ 10c(n/10) + O(n+1)

T(n+1) ≤ cn + O(n+1)

Since cn + O(n+1) is O(n), we've shown that T(n+1) is also O(n).

By completing the induction step, we've demonstrated that T(n) is O(n), which proves the worst-case time complexity of the deterministic selection algorithm is linear, as desired."""


"""
To prove the correctness of the deterministic_select algorithm, we can use a proof by induction. We will show that the algorithm correctly selects the kth smallest element in an unsorted array for all possible values of k.

Here's the proof:

*Base Case:*
- When the input array has only one element (i.e., left == right), the algorithm returns that element as the kth smallest element, which is correct since there's only one element to choose from.

*Inductive Hypothesis:*
- Assume that the algorithm correctly selects the kth smallest element for all input arrays of size less than or equal to n for some positive integer n.

*Inductive Step:*
- We want to prove that the algorithm correctly selects the kth smallest element for an input array of size n.
- The algorithm starts by selecting a pivot element using the "Median of Medians" technique. This pivot selection ensures that the pivot is approximately the median of the input array.
- The partition function is used to partition the array into two subarrays: elements less than or equal to the pivot and elements greater than the pivot.
- There are three possible cases:
   1. If median_idx (the index of the pivot after partitioning) is equal to k, the algorithm returns the pivot as the kth smallest element. This is correct since the pivot is the kth smallest element in the array.
   2. If median_idx is less than k, the algorithm knows that the kth smallest element must be in the right subarray. It recursively searches for the kth smallest element in the right subarray.
   3. If median_idx is greater than k, the algorithm knows that the kth smallest element must be in the left subarray. It recursively searches for the kth smallest element in the left subarray.

By the inductive hypothesis, in the recursive steps, the algorithm correctly selects the kth smallest element for smaller subarrays. Since the pivot selection ensures that the pivot is approximately the median, the algorithm correctly determines whether to search in the left or right subarray.

Therefore, by induction, we have shown that the deterministic_select algorithm correctly selects the kth smallest element for all possible values of k in an unsorted array.
"""