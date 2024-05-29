
def count_special_numbers(n, k):
    mod = 10**9 + 7

    dp = [[0] * (k + 1) for _ in range(1010)]
    dp[0][0] = 1

    for i in range(1, 1010):
        dp[i][0] = 1
        for m in range(1, k + 1):
            dp[i][m] = (dp[i - 1][m] + dp[i - 1][m - 1]) % mod

    ans = 0
    bit = []
    while n:
        bit.append(n)
        n &= n - 1

    bit.reverse()

    for i in range(1, len(bit) + 1):
        for m in range(k + 1):
            if m == 0:
                continue
            ans = (ans + dp[i - 1][m - 1] * pow(2, i - m, mod) % mod) % mod

    if k == 0:
        ans = (ans + 1) % mod

    return ans

n = int(input(), 2)
k = int(input())

print(count_special_numbers(n, k))
