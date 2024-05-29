
def max_value(A, B, N):
    max_val = 0
    for x in range(N+1):
        val = (A*x)//B - A*(x//B)
        max_val = max(max_val, val)
    return max_val

# Read input
A, B, N = map(int, input().split())
result = max_value(A, B, N)
print(result)
```
