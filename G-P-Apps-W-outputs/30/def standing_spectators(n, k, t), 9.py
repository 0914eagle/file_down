
def standing_spectators(n, k, t):
    cycle_length = n + k
    standing = min(n, max(0, t - k))
    if t <= cycle_length:
        return standing
    remaining_cycles = (t - cycle_length) // (n - 1)
    remaining_t = (t - cycle_length) % (n - 1)
    if remaining_t < k:
        return n
    return min(n, standing + remaining_t - k)

# Input parsing
n, k, t = map(int, input().split())

# Call the function and print the output
print(standing_spectators(n, k, t))
```
