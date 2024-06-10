
from sys import stdin

s = stdin.readline().strip()
t = stdin.readline().strip()

def solve(s, t):
    n = len(s)
    m = len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    i = n
    j = m
    res = ''
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            res += s[i - 1]
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
    res = res[::-1]
    return res

res = solve(s, t)
print(res)

