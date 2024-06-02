
def max_frogs_to_escape(n, d, frogs):
    frogs.sort(key=lambda x: x[2], reverse=True)
    dp = [0] * (d + 1)
    max_frogs = 0

    for frog in frogs:
        l, w, h = frog
        if l >= d:
            max_frogs += 1
        else:
            for i in range(d, h + l - 1, -1):
                dp[i] = max(dp[i], dp[i - h] + w)
            for i in range(h + l, d + 1):
                max_frogs = max(max_frogs, dp[i])

    return max_frogs

# Input parsing
n, d = map(int, input().split())
frogs = []
for _ in range(n):
    l, w, h = map(int, input().split())
    frogs.append((l, w, h))

result = max_frogs_to_escape(n, d, frogs)
print(result)
