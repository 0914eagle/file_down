
h, n = map(int, input().split())
spells = [list(map(int, input().split())) for _ in range(n)]
dp = [float('inf')] * (h + 1)
dp[0] = 0
for i in range(h):
    for a, b in spells:
        if i + a <= h:
            dp[i + a] = min(dp[i + a], dp[i] + b)
print(dp[h])

