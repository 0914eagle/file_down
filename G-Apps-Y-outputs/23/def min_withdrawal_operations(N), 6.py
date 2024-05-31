
def min_withdrawal_operations(N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    coins = [1]
    x, y = 6, 9
    while x <= N:
        coins.append(x)
        x *= 6
    while y <= N:
        coins.append(y)
        y *= 9

    for i in range(1, N + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[N]

N = int(input())
print(min_withdrawal_operations(N))
