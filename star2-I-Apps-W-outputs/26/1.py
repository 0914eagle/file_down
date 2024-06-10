
def solve(n, q, painters):
    painters.sort(key=lambda x: x[1])
    dp = [0] * (q + 1)
    for i in range(q - 2, 0, -1):
        dp[i] = max(dp[i + 1], painters[i][1] - painters[i][0] + 1)
    for i in range(q - 3, -1, -1):
        dp[i] = max(dp[i + 1], painters[i][1] - painters[i][0] + 1)
    return max(dp)

n, q = map(int, input().split())
painters = [list(map(int, input().split())) for _ in range(q)]
print(solve(n, q, painters))

