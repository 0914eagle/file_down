

def alice_minus_bob(a):
    n = len(a)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = a[i]
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            for k in range(i, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j])
    return dp[0][n-1]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(alice_minus_bob(a))

