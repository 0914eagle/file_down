
def min_xor_max(n, arr):
    ans = 0
    for i in range(29, -1, -1):
        prefix_set = set()
        ans <<= 1
        temp = ans | 1
        for a in arr:
            prefix_set.add(a >> i)
        for p in prefix_set:
            if temp ^ p not in prefix_set:
                ans |= 1
                break
    return ans

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Call the function and output the result
print(min_xor_max(n, arr))
```
