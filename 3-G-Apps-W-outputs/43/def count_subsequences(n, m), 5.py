
MOD = 10**9 + 7

def count_subsequences(n, m):
    dp = [0] * (m + 1)
    dp[1] = 1

    for i in range(2, m + 1):
        dp[i] = (dp[i - 1] * 2 + 1) % MOD

    result = dp[m]
    for i in range(2, n + 1):
        result = (result * dp[m] + 1) % MOD

    return result

n, m = map(int, input().split())
print(count_subsequences(n, m))
