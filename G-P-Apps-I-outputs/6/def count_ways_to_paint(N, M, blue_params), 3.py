
def count_ways_to_paint(N, M, blue_params):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    for j in range(blue_params[0], M + 1):
        dp[1][j] = 1
    
    for i in range(2, N + 1):
        s = 0
        for j in range(M, blue_params[i-1] - 1, -1):
            s = (s + dp[i-1][j]) % 100003
            dp[i][j] = s
    
    total_ways = sum(dp[N]) % 100003
    X = total_ways // 100003
    Y = total_ways % 100003
    
    return X, Y

# Read input
N, M = map(int, input().split())
blue_params = list(map(int, input().split()))

# Calculate and output result
X, Y = count_ways_to_paint(N, M, blue_params)
print(X, Y)
```
