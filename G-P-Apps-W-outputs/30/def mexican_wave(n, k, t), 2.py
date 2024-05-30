
def mexican_wave(n, k, t):
    if t <= k:
        return t
    elif t <= n:
        return k
    else:
        return max(n - t + k, 0)

# Input parsing
n, k, t = map(int, input().split())

# Output
print(mexican_wave(n, k, t))
```
