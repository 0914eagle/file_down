
def count_subsequence_pairs(N, M, S, T):
    mod = 10**9 + 7

    # Map from element to index for each array
    s_indices = {S[i]: i for i in range(N)}
    t_indices = {T[i]: i for i in range(M)}

    # DP array to store count of common subsequences
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = (2 * dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + (s_indices[S[i - 1]] == t_indices[T[j - 1]])) % mod

    return dp[N][M]

# Input processing and calling the function
N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

print(count_subsequence_pairs(N, M, S, T))
```
