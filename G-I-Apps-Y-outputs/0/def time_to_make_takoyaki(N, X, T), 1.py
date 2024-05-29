
def time_to_make_takoyaki(N, X, T):
    if N <= X:
        return T
    else:
        full_cycles = N // X
        remaining_takoyaki = N % X
        time_needed = T * full_cycles
        if remaining_takoyaki > 0:
            time_needed += T
        return time_needed

# Read input
N, X, T = map(int, input().split())

# Calculate and print the result
print(time_to_make_takoyaki(N, X, T))
```
