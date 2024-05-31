
def count_sets(N):
    dp = [[0] * (1 << N) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for mask in range(1 << N):
            for j in range(N):
                if (mask & (1 << j)) == 0 and math.gcd(i, j + 1) == 1:
                    dp[i][mask | (1 << j)] += dp[i - 1][mask]

    total_sets = sum(dp[N])
    return total_sets % 1000000000

# Read input
N = int(input())

# Calculate and output the result
print(count_sets(N))
