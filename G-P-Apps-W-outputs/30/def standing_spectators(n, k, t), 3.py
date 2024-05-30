
def standing_spectators(n, k, t):
    cycle_length = min(n, k)
    time = t % cycle_length
    if time == 0:
        return 0
    elif time <= k:
        return time
    else:
        return k - (time - k)

# Input
n, k, t = map(int, input().split())

# Output
print(standing_spectators(n, k, t))
```
