
# https://codeforces.com/contest/1093/problem/D
# D. Almost Equal
# solution using DP

from sys import stdin
input = stdin.readline

n, m, k = map(int, input().split())

if n <= k:
    print(0)
    exit(0)

dp = [[0 for i in range(k + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if i < j * m:
            dp[i][j] = 0
            continue

        ans = 0
        for l in range(1, i + 1):
            ans = max(ans, dp[i - l][j - 1] + max(l - m + 1, 0))
        dp[i][j] = ans

print(dp[n][k])

