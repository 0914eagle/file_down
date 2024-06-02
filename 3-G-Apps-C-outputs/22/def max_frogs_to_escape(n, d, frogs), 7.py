
def max_frogs_to_escape(n, d, frogs):
    frogs.sort(key=lambda x: x[2], reverse=True)
    dp = [0] * (d + 1)
    for frog in frogs:
        l, w, h = frog
        for i in range(d, h - 1, -1):
            if dp[i - h] + w <= w:
                dp[i] = max(dp[i], dp[i - h] + w)
    return min(sum(1 for x in dp if x > 0), n)

# Input parsing
n, d = map(int, input().split())
frogs = [list(map(int, input().split())) for _ in range(n)]

# Output
print(max_frogs_to_escape(n, d, frogs))
