
def min_forests_to_block_treasure(n, m, island):
    dp = [[float('inf')] * m for _ in range(n)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(m):
            if island[i][j] == '#':
                continue
            if i + 1 < n:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + (island[i + 1][j] == '#'))
            if j + 1 < m:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + (island[i][j + 1] == '#'))

    return dp[n - 1][m - 1]

# Input parsing
n, m = map(int, input().split())
island = [input() for _ in range(n)]

result = min_forests_to_block_treasure(n, m, island)
print(result)
```
