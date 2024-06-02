
def max_frogs_escape(n, d, frogs):
    frogs.sort(key=lambda x: x[0], reverse=True)
    dp = [0] * (d + 1)
    for frog in frogs:
        l, w, h = frog
        for i in range(d, h - 1, -1):
            if dp[i - h] + w <= l:
                dp[i] = max(dp[i], dp[i - h] + w)
    return sum(dp) // max(frogs, key=lambda x: x[1])[1]

# Input parsing
n, d = map(int, input().split())
frogs = [list(map(int, input().split())) for _ in range(n)]

print(max_frogs_escape(n, d, frogs))
