
class Solution:
    def solve(self, A, B):
        n = len(A)
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
        for i in range(1, n+1):
            dp[0][i] = 1
        for i in range(1, n+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1] * A[i-1]
        ans = 1e9
        for i in range(1, n+1):
            if dp[n][i] >= B:
                ans = min(ans, i)
        return ans
