
def count_ways_to_paint(N, M, blue_params):
    MOD = 100003

    # Initialize a 3D array to store the number of ways to paint each cell
    dp = [[[0 for _ in range(M+1)] for _ in range(M+1)] for _ in range(N+1)]

    # Initialize the base case
    dp[0][0][0] = 1

    # Iterate over each column
    for i in range(1, N+1):
        for b in range(M+1):
            for r in range(M+1):
                # Calculate the number of ways to paint the current cell blue
                dp[i][b][r] += dp[i-1][b][r]
                if b > 0:
                    dp[i][b][r] += dp[i-1][b-1][r]

                # Calculate the number of ways to paint the current cell red
                dp[i][b][r] += dp[i-1][b][r]
                if r > 0:
                    dp[i][b][r] += dp[i-1][b][r-1]

                # Apply modulo operation
                dp[i][b][r] %= MOD

    # Calculate the total number of ways to paint the entire picture
    total_ways = dp[N][blue_params[0]][M-blue_params[0]]

    # Return X and Ym as described in the output format
    return total_ways // MOD, total_ways % MOD

# Read input
N, M = map(int, input().split())
blue_params = list(map(int, input().split()))

# Calculate and print the result
X, Ym = count_ways_to_paint(N, M, blue_params)
print(X, Ym)
