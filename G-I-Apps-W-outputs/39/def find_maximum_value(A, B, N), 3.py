
def find_maximum_value(A, B, N):
    max_value = 0
    for x in range(N+1):
        value = A*x//B - A*(x//B)
        max_value = max(max_value, value)
    return max_value

# Input
A, B, N = map(int, input().split())

# Output
print(find_maximum_value(A, B, N))
```
