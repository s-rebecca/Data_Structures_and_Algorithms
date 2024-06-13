import time

def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    comparisons = 0

    start_time = time.time()

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            comparisons += 1
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    end_time = time.time()
    running_time_ms = (end_time - start_time) * 1000
    num_entries = len(dp) * len(dp[0])

    # Reconstructing the items selected
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    selected_items = selected_items[::-1]  # Reversing the list to get the correct order of items

    return dp[n][capacity], selected_items, comparisons, num_entries, running_time_ms

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
knapsack_capacity = 50

max_value, items_selected, comparisons, num_entries, time_taken = knapsack_01(values, weights, knapsack_capacity)
print("Maximum value that can be obtained:", max_value)
print("Selected items:", items_selected)
print("Number of entries in DP table:", num_entries)
print("Running time:", time_taken, "milliseconds")
