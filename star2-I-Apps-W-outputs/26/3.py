
def solve(n, q, painters):
    painters.sort(key=lambda x: x[1])
    dp = [0] * (q + 1)
    for i in range(1, q + 1):
        dp[i] = max(dp[i - 1], painters[i - 1][1])
        for j in range(i - 2, 0, -1):
            dp[i] = max(dp[i], dp[j] + painters[i - 1][1] - painters[j - 1][0] + 1)
    return dp[q]

n, q = map(int, input().split())
painters = [tuple(map(int, input().split())) for _ in range(q)]
print(solve(n, q, painters))

