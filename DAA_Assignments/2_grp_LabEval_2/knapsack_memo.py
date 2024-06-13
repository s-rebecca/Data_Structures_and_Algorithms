import time

def knapsack_01_memoization(values, weights, capacity, n, memo, calls):
    if n == 0 or capacity == 0:
        return 0

    if memo[n][capacity] != -1:
        return memo[n][capacity]

    calls[0] += 1

    if weights[n - 1] > capacity:
        memo[n][capacity] = knapsack_01_memoization(values, weights, capacity, n - 1, memo, calls)
        return memo[n][capacity]
    else:
        a = values[n - 1] + knapsack_01_memoization(values, weights, capacity - weights[n - 1], n - 1, memo, calls)
        b = knapsack_01_memoization(values, weights, capacity, n - 1, memo, calls)
        memo[n][capacity] = max(a, b)
        return memo[n][capacity]

def knapsack_01(values, weights, capacity):
    n = len(values)
    memo = [[-1] * (capacity + 1) for _ in range(n + 1)]
    calls = [0]
    
    start_time = time.time()
    max_value = knapsack_01_memoization(values, weights, capacity, n, memo, calls)
    end_time = time.time()

    running_time_ms = (end_time - start_time) * 1000
    return max_value, calls[0], running_time_ms

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
knapsack_capacity = 50

max_value, num_calls, time_taken = knapsack_01(values, weights, knapsack_capacity)
print("Maximum value that can be obtained:", max_value)
print("Number of function calls:", num_calls)
print("Running time:", time_taken, "milliseconds")
