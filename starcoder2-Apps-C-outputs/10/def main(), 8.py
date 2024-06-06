
def main():
    n = int(input())
    d = []
    for i in range(n - 1):
        d.append(list(map(int, input().split())))
    dp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n - 1):
        for j in range(n - i - 1):
            dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + d[i][j]
    print(dp[0][0])


if __name__ == '__main__':
    main()
