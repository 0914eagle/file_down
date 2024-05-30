
def find_min_xor(n, array):
    max_num = max(array)
    msb_pos = 31 - len(bin(max_num)[2:])
    
    res = 0
    for i in range(msb_pos, -1, -1):
        bit = 1 << i
        res_temp = res | bit
        candidates = [res_temp ^ num for num in array]
        if any(candidate > max_num for candidate in candidates):
            res = res_temp
    
    return res

# Input
n = int(input())
array = list(map(int, input().split()))

# Output
print(find_min_xor(n, array))
```
