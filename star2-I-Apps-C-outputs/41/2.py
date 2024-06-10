
from sys import stdin
s = stdin.readline().strip()
t = stdin.readline().strip()

def solve(s, t):
    n = len(s)
    m = len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    res = ""
    i = n
    j = m
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            res = s[i - 1] + res
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return res

res = solve(s, t)
if len(res) == len(t):
    print(res)
else:
    print("IMPOSSIBLE")

