
def min_operations_to_withdraw(N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j*j] + 1)
            j += 1
        k = 1
        while k * k * k <= i:
            dp[i] = min(dp[i], dp[i - k*k*k] + 1)
            k += 1
    return dp[N]

N = int(input())
print(min_operations_to_withdraw(N))
