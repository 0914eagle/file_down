
def max_frogs_escape(n, d, frogs):
    frogs.sort(key=lambda x: x[2], reverse=True)
    dp = [0] * (d + 1)
    for i in range(n):
        l, w, h = frogs[i]
        for j in range(d, h - 1, -1):
            if j - h >= l:
                dp[j] = max(dp[j], dp[j - h] + 1)
            elif w <= j:
                dp[j] = max(dp[j], dp[j - w])
    return dp[d]

# Input parsing
n, d = map(int, input().split())
frogs = [list(map(int, input().split())) for _ in range(n)]

# Output
print(max_frogs_escape(n, d, frogs))
