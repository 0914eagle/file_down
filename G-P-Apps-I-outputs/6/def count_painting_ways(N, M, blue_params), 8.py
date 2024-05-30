
def count_painting_ways(N, M, blue_params):
    mod = 100003
    dp = [[0] * (M+1) for _ in range(N+1)]
    
    dp[0][0] = 1
    
    for i in range(1, N+1):
        for j in range(M+1):
            if j < blue_params[i-1]:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod
    
    total_ways = dp[N][M]
    X = total_ways // mod
    Y = total_ways % mod
    
    return X, Y

# Read input
N, M = map(int, input().split())
blue_params = list(map(int, input().split()))

# Calculate and print the output
X, Y = count_painting_ways(N, M, blue_params)
print(X, Y)
```
