
def max_frogs_escape(n, d, frogs):
    frogs.sort(key=lambda x: x[2], reverse=True)
    dp = [0] * (d + 1)
    for frog in frogs:
        l, w, h = frog
        for i in range(d, h - 1, -1):
            if i - h >= 0 and dp[i - h] + w <= w:
                dp[i] = max(dp[i], dp[i - h] + w)
        for i in range(d, l - 1, -1):
            if i - l >= 0 and dp[i - l] + w <= w:
                dp[i] = max(dp[i], dp[i - l] + w)
    return sum(1 for x in dp if x > 0)

# Input parsing
n, d = map(int, input().split())
frogs = []
for _ in range(n):
    l, w, h = map(int, input().split())
    frogs.append((l, w, h))

print(max_frogs_escape(n, d, frogs))
