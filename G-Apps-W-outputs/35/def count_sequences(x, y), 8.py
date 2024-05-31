
def count_sequences(x, y):
    mod = 10**9 + 7
    if y % x != 0:
        return 0

    y //= x
    factors = []
    for i in range(1, int(y**0.5) + 1):
        if y % i == 0:
            factors.append(i)
            if i * i != y:
                factors.append(y // i)

    dp = [0] * (y+1)
    dp[0] = 1

    for factor in factors:
        for i in range(y, factor - 1, -1):
            dp[i] += dp[i - factor]
            dp[i] %= mod

    return dp[y]

x, y = map(int, input().split())
print(count_sequences(x, y))
