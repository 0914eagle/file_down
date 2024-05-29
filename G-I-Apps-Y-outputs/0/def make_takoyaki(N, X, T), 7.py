
def make_takoyaki(N, X, T):
    full_batches = N // X
    remaining_pieces = N % X
    
    if remaining_pieces == 0:
        return full_batches * T
    else:
        return (full_batches + 1) * T

# Input
input_values = input().split()
N = int(input_values[0])
X = int(input_values[1])
T = int(input_values[2])

# Output
print(make_takoyaki(N, X, T))
```
