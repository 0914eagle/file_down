
def max_frogs_escape(n, d, frogs):
    frogs.sort(key=lambda x: x[2], reverse=True)
    dp = [0] * (d + 1)
    for frog in frogs:
        l, w, h = frog
        for i in range(d, h - 1, -1):
            if dp[i - h] + w <= w:
                dp[i] = max(dp[i], dp[i - h] + w)
        for i in range(d, l + h, -1):
            dp[i] = max(dp[i], dp[i - l])
    return max(dp)

# Input parsing
n, d = map(int, input().split())
frogs = [list(map(int, input().split())) for _ in range(n)]

result = max_frogs_escape(n, d, frogs)
print(result)
