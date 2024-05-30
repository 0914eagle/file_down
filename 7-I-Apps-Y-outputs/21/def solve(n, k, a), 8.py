

def solve(n, k, a):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + a[j - 1])
    return dp[k][n]


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))
    print(*[k for k in range(1, n + 1) if dp[k][n] == dp[k][n - 1] + a[n - 1]], sep=" ")

