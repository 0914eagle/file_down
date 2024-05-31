
def count_winning_sets(N):
    dp = [[0] * (1 << N) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for mask in range(1 << N):
            for j in range(N):
                if mask & (1 << j):
                    continue
                valid = True
                for k in range(j):
                    if mask & (1 << k) and not math.gcd(j + 1, k + 1) == 1:
                        valid = False
                        break
                if valid:
                    dp[i][mask | (1 << j)] += dp[i - 1][mask]
    
    ans = sum(dp[N])
    return ans % 1000000000

# Taking input
N = int(input().strip())

# Getting the result
result = count_winning_sets(N)
print(result)
