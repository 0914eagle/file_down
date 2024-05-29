
def max_frogs_escape_pit(n, d, frogs):
    frogs.sort(key=lambda x: x[2], reverse=True)
    dp = [0] * (d + 1)
    for i in range(n):
        leap, weight, height = frogs[i]
        for j in range(d, height - 1, -1):
            if dp[j - height] + weight <= leap and dp[j - height] + weight < dp[j]:
                dp[j] = dp[j - height] + weight
    escape_count = 0
    for i in range(d + 1):
        if dp[i] > 0:
            escape_count += 1
    return escape_count

# Input
n, d = map(int, input().split())
frogs = []
for _ in range(n):
    l, w, h = map(int, input().split())
    frogs.append((l, w, h))

# Output
print(max_frogs_escape_pit(n, d, frogs))
```
