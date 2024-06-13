def min_coins(coins, total):
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    used_coins = [[] for _ in range(total + 1)]

    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coins[i] = used_coins[i - coin][:]
                used_coins[i].append(coin)

    if dp[total] == float('inf'):
        return -1, []
    return dp[total], used_coins[total]

coin_denominations = [1, 2, 5]
target_amount = 11
minimum_coins, coins_used = min_coins(coin_denominations, target_amount)

if minimum_coins == -1:
    print(f"Cannot make the total amount of {target_amount} with the given coins.")
else:
    print(f"Minimum number of coins to make {target_amount}: {minimum_coins}")
    print(f"Coins used: {coins_used}")
