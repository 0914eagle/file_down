
def max_value(A, B, N):
    max_val = 0
    for x in range(N+1):
        value = A * (x // B) - A * (x // B)
        max_val = max(max_val, value)
    return max_val

# Read input from Standard Input
A, B, N = map(int, input().split())

# Call the function and print the output
print(max_value(A, B, N))
```
