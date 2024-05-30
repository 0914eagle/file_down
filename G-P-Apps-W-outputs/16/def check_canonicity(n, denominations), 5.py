
def check_canonicity(n, denominations):
    if n < 2 or n > 100:
        return "Invalid input"

    if denominations[0] != 1:
        return "non-canonical"

    sum_two_largest = denominations[-1] + denominations[-2]

    for x in range(1, sum_two_largest):
        min_coins_greedy = 0
        remaining = x
        for i in range(n-1, -1, -1):
            min_coins_greedy += remaining // denominations[i]
            remaining %= denominations[i]

        min_coins_optimal = float('inf')
        dp = [float('inf')] * (x + 1)
        dp[0] = 0
        for i in range(1, x+1):
            for j in range(n):
                if denominations[j] <= i:
                    dp[i] = min(dp[i], dp[i - denominations[j]] + 1)
            min_coins_optimal = min(min_coins_optimal, dp[i])

        if min_coins_greedy != min_coins_optimal:
            return "non-canonical"

    return "canonical"

# Read input
n = int(input())
denominations = list(map(int, input().split()))

# Check canonicity and print output
print(check_canonicity(n, denominations))
```
