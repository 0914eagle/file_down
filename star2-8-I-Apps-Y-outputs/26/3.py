
import sys


def solve(s, k):
    n = len(s)
    rgb = ['R', 'G', 'B']
    dp = [[sys.maxsize for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(k + 1):
        dp[0][i] = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if s[i - 1] in rgb:
                dp[i][j] = min(dp[i][j], dp[i - 1][j])
            for c in rgb:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + (s[i - 1] != c))
    return dp[n][k]


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        s = input()
        print(solve(s, k))

