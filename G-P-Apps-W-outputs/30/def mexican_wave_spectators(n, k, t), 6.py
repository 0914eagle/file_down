
def mexican_wave_spectators(n, k, t):
    if t <= k:
        return t
    elif t <= n:
        return k
    else:
        return k - (t - n)

n, k, t = map(int, input().strip().split())
print(mexican_wave_spectators(n, k, t))
```
