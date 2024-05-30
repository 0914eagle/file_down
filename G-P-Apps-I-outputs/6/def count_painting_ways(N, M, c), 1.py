
def count_painting_ways(N, M, c):
    mod_value = 100003
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(M+1):
            if j >= c[i-1]:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod_value
            else:
                dp[i][j] = dp[i-1][j]
    
    total_ways = dp[N][M]
    X = total_ways // mod_value
    Y = total_ways % mod_value
    
    return X, Y

# Input parsing
input_line1 = input().strip().split()
N = int(input_line1[0])
M = int(input_line1[1])

input_line2 = input().strip().split()
c = [int(x) for x in input_line2]

X, Y = count_painting_ways(N, M, c)
print(X, Y)
```
