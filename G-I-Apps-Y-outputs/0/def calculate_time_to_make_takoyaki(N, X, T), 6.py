
def calculate_time_to_make_takoyaki(N, X, T):
    batches = N // X
    remainder = N % X
    if remainder == 0:
        return batches * T
    else:
        return (batches + 1) * T

# Input
N, X, T = map(int, input().split())

# Output
print(calculate_time_to_make_takoyaki(N, X, T))
```
