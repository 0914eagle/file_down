
def time_to_make_takoyaki(N, X, T):
    full_batches = N // X
    remaining_takoyaki = N % X

    if remaining_takoyaki > 0:
        time_needed = full_batches * T + T
    else:
        time_needed = full_batches * T

    return time_needed

# Input processing
input_values = input().split()
N, X, T = map(int, input_values)

# Calculate and print the result
result = time_to_make_takoyaki(N, X, T)
print(result)
```
