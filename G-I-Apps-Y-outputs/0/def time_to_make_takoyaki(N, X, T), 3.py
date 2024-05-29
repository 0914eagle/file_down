
def time_to_make_takoyaki(N, X, T):
    full_cycles = N // X
    remaining = N % X
    if remaining == 0:
        return full_cycles * T
    else:
        return (full_cycles + 1) * T

# Input
input_values = input().split()
N = int(input_values[0])
X = int(input_values[1])
T = int(input_values[2])

# Output
print(time_to_make_takoyaki(N, X, T))
```
