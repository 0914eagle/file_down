
def standing_spectators(n, k, t):
    cycle_len = min(n, k)
    if t <= cycle_len:
        return t
    elif t <= n:
        return cycle_len
    else:
        return n + k - t

n, k, t = map(int, input().split())
print(standing_spectators(n, k, t))
```
