
def min_xor_max(n, arr):
    max_xor = max(arr)
    msb = 1 << (len(bin(max_xor))-2)
    for i in range(n):
        if (arr[i] ^ msb) < arr[i]:
            arr[i] ^= msb
    return max(arr)

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(min_xor_max(n, arr))
```
