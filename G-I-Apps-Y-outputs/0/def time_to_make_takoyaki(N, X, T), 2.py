
def time_to_make_takoyaki(N, X, T):
    full_batches = N // X
    remaining = N % X
    time = full_batches * T
    if remaining > 0:
        time += T
    return time

# Read input
N, X, T = map(int, input().split())

# Calculate and print output
print(time_to_make_takoyaki(N, X, T))
```
