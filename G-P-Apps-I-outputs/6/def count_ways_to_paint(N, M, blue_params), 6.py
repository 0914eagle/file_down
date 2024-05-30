
# Function to calculate the number of ways to create the painting
def count_ways_to_paint(N, M, blue_params):
    mod = 100003

    # Calculate the total blue cells
    total_blue = sum(blue_params)

    # Calculate the total red cells
    total_red = M * N - total_blue

    # Calculate the number of ways
    if total_red == 0 or total_blue == 0:
        return 0, total_blue % mod

    # Initialize dp array
    dp = [[0] * (total_red + 1) for _ in range(total_blue + 1)]
    dp[0][0] = 1

    # Populate dp array
    for i in range(total_blue + 1):
        for j in range(total_red + 1):
            if i + j == 0:
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= mod

    return dp[total_blue][total_red], total_blue % mod

# Reading input
N, M = map(int, input().split())
blue_params = list(map(int, input().split()))

# Calculate and print the result
result_X, result_Y = count_ways_to_paint(N, M, blue_params)
print(result_X, result_Y)
```
