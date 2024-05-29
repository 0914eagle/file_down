
def time_to_make_takoyaki(N, X, T):
    full_sets = N // X
    leftover = N % X
    if leftover != 0:
        return (full_sets + 1) * T
    else:
        return full_sets * T

# Read input
N, X, T = map(int, input().split())

# Calculate and output result
print(time_to_make_takoyaki(N, X, T))
```
