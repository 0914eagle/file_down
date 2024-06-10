
def solve(A):
    N = len(A)
    dp = [[0] * 2 for _ in range(N)]
    dp[0][0] = 0
    dp[0][1] = A[0]
    for i in range(1, N):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = dp[i - 1][0] + A[i]
    return max(dp[-1][0], dp[-1][1])


N = int(input())
A = list(map(int, input().split()))
print(solve(A))

