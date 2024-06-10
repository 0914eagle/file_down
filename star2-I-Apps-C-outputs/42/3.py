
def solve(S):
    MOD = 10**9 + 7
    dp = [0] * (S + 1)
    dp[0] = 1
    for s in range(1, S + 1):
        for d in range(1, 10):
            if s - d >= 0:
                dp[s] += dp[s - d]
                dp[s] %= MOD
    return dp[S]

S = int(input())
print(solve(S))

