
def min_operations_to_withdraw(N):
    coins = [1]
    for i in range(1, 10):
        coins.append(6 ** i)
        coins.append(9 ** i)
    
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    
    for i in range(1, N + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[N]

N = int(input())
print(min_operations_to_withdraw(N))
