
def min_operations_to_withdraw(N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for i in range(1, N + 1):
        for j in [1, 6, 36, 216, 9, 81, 729]:
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + 1)

    return dp[N]

N = int(input())
print(min_operations_to_withdraw(N))