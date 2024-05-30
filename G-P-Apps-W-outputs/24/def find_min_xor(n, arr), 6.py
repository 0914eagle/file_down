
def find_min_xor(n, arr):
    max_val = max(arr)
    msb = 1
    while msb <= max_val:
        msb <<= 1
    msb >>= 1
    best = msb
    for i in range(n):
        if (arr[i] & msb) != 0:
            best = max(best, msb | (msb - 1))
    return best

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(find_min_xor(n, arr))
```
