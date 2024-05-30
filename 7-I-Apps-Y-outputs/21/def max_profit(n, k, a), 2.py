
def max_profit(n, k, a):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + a[i - 1])
    ans = dp[n][k]
    res = [0] * k
    i, j = n, k
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            res[j - 1] = i
            i -= 1
            j -= 1
    return ans, res


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans, res = max_profit(n, k, a)
    print(ans)
    print(*res)


if __name__ == "__main__":
    main()

