
MOD = 10**9 + 7

def count_same_subsequences(S, T):
    dp = [[0 for j in range(len(T) + 1)] for i in range(len(S) + 1)]

    for i in range(len(S) + 1):
        for j in range(len(T) + 1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            elif S[i - 1] == T[j - 1]:
                dp[i][j] = (2 * dp[i - 1][j - 1]) % MOD + dp[i - 1][j] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

            dp[i][j] %= MOD

    return dp[len(S)][len(T)]

# Reading input from Standard Input
N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

# Output the result
print(count_same_subsequences(S, T))
