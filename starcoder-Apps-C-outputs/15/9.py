
import sys
n, c = map(int, input().split())
dp = [[0]*(n+1) for _ in range(c+1)]
dp[0][0] = 1
for i in range(c):
    for j in range(n):
        dp[i+1][j+1] = (dp[i+1][j] + dp[i][j] * (n-j) % 1000000007) % 1000000007
print(dp[c][n] % 1000000007)
