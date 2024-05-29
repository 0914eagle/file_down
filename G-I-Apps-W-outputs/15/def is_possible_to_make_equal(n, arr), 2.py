
def is_possible_to_make_equal(n, arr):
    total_sum = sum(arr)
    if total_sum % n != 0:
        return "NO"
    target = total_sum // n
    max_diff = max(arr) - target
    if max_diff % 2 != 0:
        return "NO"
    for num in arr:
        if (num - target) % (max_diff // 2) != 0:
            return "NO"
    return "YES"

# Reading input
n = int(input())
arr = list(map(int, input().split()))

# Outputting result
print(is_possible_to_make_equal(n, arr))
```
