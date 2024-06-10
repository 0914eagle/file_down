
def solve(n, a):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i % 2 == 0:
            dp[i] = max(dp[i - 1], dp[i - 2] + a[i - 1])
        else:
            dp[i] = dp[i - 1]
    return dp[n]


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))


if __name__ == '__main__':
    main()

