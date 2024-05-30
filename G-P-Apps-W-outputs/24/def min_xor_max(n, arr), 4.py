
def min_xor_max(n, arr):
    max_val = max(arr)
    bit_len = len(bin(max_val)) - 2
    ans = 0
    for i in range(bit_len):
        mask = 1 << i
        candidates = ans | mask
        possible = set()
        for a in arr:
            possible.add(a & candidates)
        for p in possible:
            if ans | (1 << i) in possible:
                ans |= (1 << i)
                break
    return ans

# Reading input
n = int(input())
arr = list(map(int, input().split()))

# Calling the function and printing the result
print(min_xor_max(n, arr))
```
