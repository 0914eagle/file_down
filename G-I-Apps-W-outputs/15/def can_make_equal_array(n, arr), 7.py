
def can_make_equal_array(n, arr):
    min_val = min(arr)
    max_val = max(arr)
    diff = max_val - min_val
    for num in arr:
        if (num - min_val) % diff != 0:
            return "NO"
    return "YES"

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(can_make_equal_array(n, arr))
```
