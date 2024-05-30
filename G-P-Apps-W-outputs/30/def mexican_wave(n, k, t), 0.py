
def mexican_wave(n, k, t):
    cycle_length = min(n, k)
    standing_spectators = min(t, cycle_length) if t <= n else max(0, n - (t - n))
    return standing_spectators

# Input parsing
n, k, t = map(int, input().split())

# Call the function and print the output
print(mexican_wave(n, k, t))
```
