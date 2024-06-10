
import sys


def solve(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(2)]
    for i in range(n):
        dp[0][i] = dp[1][i] = 1
        if i > 0:
            if s[i] == s[i - 1]:
                dp[0][i] = dp[1][i] = 0
            else:
                dp[0][i] = dp[1][i - 1] + 1
                dp[1][i] = dp[0][i - 1] + 1
    return max(max(dp[0]), max(dp[1]))


def main():
    n = int(input())
    s = sys.stdin.readline().strip()
    print(solve(s))


if __name__ == "__main__":
    main()


