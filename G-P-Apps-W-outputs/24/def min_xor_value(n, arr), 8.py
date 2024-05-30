
def min_xor_value(n, arr):
    max_val = max(arr)
    msb = 1 << (len(bin(max_val)) - 2)
    res = 0
    for i in range(n):
        if (arr[i] & msb) != 0:
            res |= arr[i]
    return res

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(min_xor_value(n, arr))
```
