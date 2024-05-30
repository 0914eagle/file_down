
def mexican_wave_spectators(n, k, t):
    if t <= k:
        return t
    elif t <= n:
        return k
    else:
        return max(0, k - (t - n))

# Input
n, k, t = map(int, input().split())

# Output
print(mexican_wave_spectators(n, k, t))
```
