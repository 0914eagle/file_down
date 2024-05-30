
def min_worst_case_time(n, r, p):
    left = 0
    right = n * p
    while left < right:
        mid = (left + right) // 2
        if mid//p * (mid//p + 1) // 2 * p > r:
            right = mid
        else:
            left = mid + 1
    return left

# Input
n, r, p = map(int, input().split())

# Output
print(min_worst_case_time(n, r, p))
```
