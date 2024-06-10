

import sys

def readline():
    return sys.stdin.readline().strip()

def readvalues(t):
    return map(t, readline().split())


def solve(n, k, p):
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(n):
        w = p[i]
        for j in range(k - w, -1, -1):
            dp[j + w] += dp[j]
            dp[j + w] %= MOD
    return dp[k]


MOD = 10**9 + 7
n, k = readvalues(int)
p = list(readvalues(int))
res = solve(n, k, p)
if res == 0:
    print(-1)
    print(0)
else:
    print(res)
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(n):
        w = p[i]
        for j in range(k - w, -1, -1):
            dp[j + w] += dp[j]
            dp[j + w] %= MOD
    print(dp[k])


