
def make_takoyaki(N, X, T):
    num_batches = N // X
    leftover = N % X if N % X != 0 else 0
    time_needed = num_batches * T
    if leftover > 0:
        time_needed += T
    return time_needed

# Input processing
N, X, T = map(int, input().split())

# Calculate and print the result
print(make_takoyaki(N, X, T))
```
