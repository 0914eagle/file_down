
def max_f(N, arr):
    max_val = 0
    for m in range(1, max(arr)*2):
        val = sum(m % ai for ai in arr)
        max_val = max(max_val, val)
    return max_val

# Get input
N = int(input())
arr = list(map(int, input().split()))

# Get the maximum value of f
result = max_f(N, arr)
print(result)
```
