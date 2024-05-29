
def min_operations(N, x, a):
    ops = 0
    for i in range(1, N):
        total = a[i] + a[i-1]
        if total > x:
            diff = total - x
            ops += diff
            a[i] -= diff
    return ops

# Read input
N, x = map(int, input().split())
a = list(map(int, input().split()))

# Calculate and print the result
print(min_operations(N, x, a))
```
