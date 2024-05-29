
def find_max_value(A, B, N):
    max_val = 0
    for x in range(N+1):
        val = (A*x) // B - A*(x // B)
        max_val = max(max_val, val)
    return max_val

A, B, N = map(int, input().split())
result = find_max_value(A, B, N)
print(result)
```
