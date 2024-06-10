
H, N = map(int, input().split())
spells = [tuple(map(int, input().split())) for _ in range(N)]
dp = [float("inf")] * (H + 1)
dp[0] = 0
for h in range(1, H + 1):
    for a, b in spells:
        if h - a >= 0:
            dp[h] = min(dp[h], dp[h - a] + b)
print(dp[H])

