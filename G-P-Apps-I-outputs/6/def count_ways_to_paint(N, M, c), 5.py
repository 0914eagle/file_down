
def count_ways_to_paint(N, M, c):
    mod = 100003
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(M + 1):
            dp[i][j] = dp[i - 1][j]  # Do not paint this column
            if j >= c[i - 1]:  # Paint this column
                dp[i][j] += dp[i - 1][j - c[i - 1]]
            dp[i][j] %= mod

    X = dp[N][M]  # Total number of ways to paint the picture
    Y = X % mod
    X = X // mod

    return X, Y

# Read input
N, M = map(int, input().split())
c = list(map(int, input().split()))

# Call the function and output the result
X, Y = count_ways_to_paint(N, M, c)
print(X, Y)
```
