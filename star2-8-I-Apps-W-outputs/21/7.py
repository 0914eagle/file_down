
n = int(input())
p = list(map(int, input().split()))

M = 998244353

def inverse(a):
    return pow(a, M - 2, M)

def prob(i, j):
    if i == j:
        return p[i]
    else:
        return 100 - p[i]

def solve(n, p):
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 100

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1

            res = 0
            for k in range(i, j + 1):
                res += prob(k, i) * dp[k + 1][j]

            dp[i][j] = res / l

    return int(dp[0][n - 1] * inverse(100) % M)

print(solve(n, p))

