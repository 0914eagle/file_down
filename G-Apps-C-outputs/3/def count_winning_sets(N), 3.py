
def count_winning_sets(N):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    dp = [0] * (1 << N)
    dp[0] = 1

    for mask in range(1, 1 << N):
        pairs = []
        for i in range(N):
            if mask & (1 << i):
                pairs.append(i + 1)

        for i, x in enumerate(pairs):
            for y in pairs[i + 1:]:
                if gcd(x, y) == 1:
                    dp[mask] += dp[mask ^ (1 << x - 1) ^ (1 << y - 1)]

    return dp[(1 << N) - 1] % 1000000000

# Input
N = int(input())

# Output
print(count_winning_sets(N))
