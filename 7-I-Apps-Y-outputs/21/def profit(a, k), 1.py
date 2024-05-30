

def profit(a, k):
    n = len(a)
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + a[j - 1])
    return dp[-1][-1], dp


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans, dp = profit(a, k)
    print(ans)
    print(*[dp[i][n] for i in range(1, k + 1)])


if __name__ == '__main__':
    main()

