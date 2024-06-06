

import sys
import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, s, m, k = map(int, input().split())
a = list(map(int, input().split()))
segment = [[] for _ in range(n)]
for _ in range(s):
    l, r = map(int, input().split())
    for i in range(l - 1, r):
        segment[i].append(_)

dp = [[10 ** 9] * (s + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(s + 1):
        if j > 0:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - 1] + a[i])
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        if segment[i]:
            for x in segment[i]:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j + 1])

if dp[n][m] >= 10 ** 9:
    print(-1)
else:
    print(dp[n][m])
