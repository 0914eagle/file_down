
def partition(d):
    n = len(d) + 1
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[0][0] = 0
    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i):
                for j in range(n):
                    if mask & (1 << j):
                        dp[mask][i] = min(dp[mask][i], dp[mask ^ (1 << i)][j] + d[j][i])
    return min(dp[(1 << n) - 1])

n = int(input())
d = [[0] * n for _ in range(n)]
for i in range(n - 1):
    d[i][i + 1:] = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        d[j][i] = d[i][j]
print(partition(d))

