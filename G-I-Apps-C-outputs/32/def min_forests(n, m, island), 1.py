
def min_forests(n, m, island):
    dp = [[float("inf")] * m for _ in range(n)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(m):
            if island[i][j] == '#':
                dp[i][j] = float("inf")
                continue
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1])
            dp[i][j] += island[i][j] == '#'

    return dp[n-1][m-1]

# Input reading and function call
n, m = map(int, input().split())
island = [input() for _ in range(n)]
result = min_forests(n, m, island)
print(result)
```
