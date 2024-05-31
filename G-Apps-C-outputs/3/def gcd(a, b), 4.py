
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_sets(N):
    dp = [0] * (1 << N)
    dp[0] = 1

    for mask in range(1, 1 << N):
        pairs = []
        for i in range(N):
            if (mask >> i) & 1:
                pairs.append(i)

        for i in range(len(pairs)):
            for j in range(i + 1, len(pairs)):
                if gcd(pairs[i] + 1, pairs[j] + 1) == 1:
                    dp[mask] += dp[mask ^ (1 << pairs[i]) ^ (1 << pairs[j])]

    return dp[(1 << N) - 1] % 1000000000

# Input
N = int(input())

# Output
print(count_sets(N))
