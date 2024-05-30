
import itertools

def get_max_profit(a, k):
    n = len(a)
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i == 1:
                dp[i][j] = a[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], a[i - 1] + dp[i - j][j - 1])
    return dp[n][k]


def get_solution(a, k):
    n = len(a)
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = max(dp[i - 1][j], 1 + dp[i - j][j - 1])
    ans = []
    i, j = n, k
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            ans.append(i)
            i -= j
            j -= j
    return ans[::-1]


def solve(n, k, a):
    profit = get_max_profit(a, k)
    solution = get_solution(a, k)
    print(profit)
    print(*solution)

