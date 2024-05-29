
def max_value(A, B, N):
    max_val = 0
    for x in range(N+1):
        val = A*x//B - A*(x//B)
        max_val = max(max_val, val)
    return max_val

# Input
A, B, N = map(int, input().split())

# Output
print(max_value(A, B, N))
```
