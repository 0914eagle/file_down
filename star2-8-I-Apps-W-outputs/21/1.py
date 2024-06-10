
import sys

def solve(n, p):
    prob = [pi / 100 for pi in p]
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1 - prob[0]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] * (1 - prob[i])
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j - 1] * prob[i] + dp[i - 1][j] * (1 - prob[i])
    for i in range(n):
        if dp[n - 1][i] == 1:
            return i + 1
    return n

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    p = [int(x) for x in sys.stdin.readline().strip().split()]
    print(solve(n, p))

