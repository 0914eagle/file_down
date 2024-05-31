
def count_winning_sets(N):
    dp = [0] * (1 << N)
    dp[0] = 1

    for i in range(1, 1 << N):
        pairs = []
        for j in range(N):
            if i & (1 << j):
                pairs.append(j + 1)

        for j in range(len(pairs)):
            for k in range(j + 1, len(pairs)):
                if math.gcd(pairs[j], pairs[k]) == 1:
                    dp[i] = (dp[i] + dp[i ^ (1 << pairs[j] - 1) ^ (1 << pairs[k] - 1)]) % 1000000000

    return dp[(1 << N) - 1]

N = int(input())
print(count_winning_sets(N))
