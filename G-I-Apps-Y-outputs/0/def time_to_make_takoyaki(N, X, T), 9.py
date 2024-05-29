
def time_to_make_takoyaki(N, X, T):
    full_batches = N // X
    remaining_takoyaki = N % X
    if remaining_takoyaki > 0:
        return (full_batches + 1) * T
    else:
        return full_batches * T

# Read input from Standard Input
N, X, T = map(int, input().split())

result = time_to_make_takoyaki(N, X, T)
print(result)
```
