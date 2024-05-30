
def min_xor_max(n, arr):
    max_val = max(arr)
    msb_pos = 30
    while msb_pos >= 0:
        count = sum((x >> msb_pos) & 1 for x in arr)
        if count > n // 2:
            break
        msb_pos -= 1
    
    mask = (1 << (msb_pos + 1)) - 1
    return mask

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(min_xor_max(n, arr))
```
