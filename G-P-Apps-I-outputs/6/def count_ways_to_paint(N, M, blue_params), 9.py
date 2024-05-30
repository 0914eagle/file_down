
def count_ways_to_paint(N, M, blue_params):
    MOD = 100003

    # Initialize a 3D array to store the number of ways to paint up to a certain cell
    dp = [[[0 for _ in range(M+1)] for _ in range(blue_params[0]+1)] for _ in range(blue_params[1]+1)]

    # Base case: initialize the first cell
    dp[1][1][1] = 1

    # Fill in the rest of the array using dynamic programming
    for i in range(1, blue_params[0]+1):
        for j in range(1, blue_params[1]+1):
            for k in range(1, M+1):
                if i == 1 and j == 1 and k == 1:
                    continue
                if k >= 2 and i >= 1:
                    dp[i][j][k] += dp[i-1][j][k-2]
                if k >= 1 and j >= 1:
                    dp[i][j][k] += dp[i][j-1][k-1]
                dp[i][j][k] %= MOD

    total_ways = dp[blue_params[0]][blue_params[1]][M]
    X = total_ways // MOD
    Y = total_ways % MOD

    return X, Y

# Read input
N, M = map(int, input().split())
blue_params = list(map(int, input().split()))

# Calculate and output the result
X, Y = count_ways_to_paint(N, M, blue_params)
print(X, Y)
```
