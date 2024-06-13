import time

def knapsack_recursive(values, weights, capacity, n, calls):
    if n == 0 or capacity == 0:
        return 0

    if weights[n - 1] > capacity:
        calls[0] += 1
        return knapsack_recursive(values, weights, capacity, n - 1, calls)

    else:
        calls[0] += 1
        a = values[n - 1] + knapsack_recursive(values, weights, capacity - weights[n - 1], n - 1, calls)
        b = knapsack_recursive(values, weights, capacity, n - 1, calls)
        return max(a, b)

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
knapsack_capacity = 50
n = len(values)
calls = [0]

start_time = time.time()
result = knapsack_recursive(values, weights, knapsack_capacity, n, calls)
end_time = time.time()

running_time_ms = (end_time - start_time) * 1000
print("Maximum value that can be obtained:", result)
print("Running time:", running_time_ms, "milliseconds")
print("Number of recursive calls:", calls[0])
