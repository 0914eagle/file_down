
def count_winning_sets(N):
    dp = [0] * (1 << N)
    dp[0] = 1

    for mask in range(1, 1 << N):
        for i in range(N):
            if (mask & (1 << i)) == 0:
                continue
            for j in range(i + 1, N):
                if (mask & (1 << j)) == 0 and math.gcd(i + 1, j + 1) == 1:
                    dp[mask] += dp[mask ^ (1 << i) ^ (1 << j)]
                    dp[mask] %= 1000000000

    return dp[(1 << N) - 1]

N = int(input())
print(count_winning_sets(N))
