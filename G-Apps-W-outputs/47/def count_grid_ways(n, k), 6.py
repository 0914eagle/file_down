
def count_grid_ways(n, k):
    MOD = 10**9 + 7

    # Initialize a 2D array to store the number of ways for each cell
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Initialize the base cases
    for num in range(1, k + 1):
        dp[1][num] = 1

    # Iterate over rows and columns to calculate the number of ways
    for i in range(2, n + 1):
        for j in range(1, k + 1):
            for num in range(1, j + 1):
                dp[i][j] = (dp[i][j] + dp[i - 1][num]) % MOD

    # Calculate the total number of ways by summing up the last row
    total_ways = sum(dp[n]) % MOD

    return total_ways

# Read input values
n, k = map(int, input().split())

# Calculate and print the answer modulo (10^9 + 7)
print(count_grid_ways(n, k))
