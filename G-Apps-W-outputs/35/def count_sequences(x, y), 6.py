
def count_sequences(x, y):
    MOD = 10**9 + 7

    # Compute the divisors of y that are multiples of x
    divisors = []
    for i in range(1, int(y**0.5) + 1):
        if y % i == 0:
            if i % x == 0:
                divisors.append(i)
            if i != y // i and (y // i) % x == 0:
                divisors.append(y // i)

    # Dynamic programming approach to count sequences
    dp = [0] * (y + 1)
    dp[0] = 1

    for i in divisors:
        for j in range(y, i - 1, -1):
            dp[j] = (dp[j] + dp[j - i]) % MOD

    return dp[y]

# Input
x, y = map(int, input().split())

# Output
print(count_sequences(x, y))
