
N, K = map(int, input().split())

dp = [0] * (N+1)
dp[0] = K
dp[1] = K * (K-1)

for i in range(2, N+1):
    dp[i] = dp[i-1] * (K-1) + dp[i-2] * (K-1)

print(dp[N])

