
n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    if a[i - 1] <= 2 * a[i - 2]:
        dp[i] = max(dp[i], dp[i - 1] + 1)
    dp[i] = max(dp[i], dp[i - 1])

print(dp[n])

