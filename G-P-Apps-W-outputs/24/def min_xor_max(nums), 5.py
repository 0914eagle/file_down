
def min_xor_max(nums):
    result = 0
    for i in range(30, -1, -1):
        prefixes = set()
        result <<= 1
        candidate = result | 1
        for num in nums:
            prefixes.add(num >> i)
        for prefix in prefixes:
            if (result ^ prefix) in prefixes:
                result |= 1
                break
    return result

n = int(input())
nums = list(map(int, input().split()))
print(min_xor_max(nums))
```
