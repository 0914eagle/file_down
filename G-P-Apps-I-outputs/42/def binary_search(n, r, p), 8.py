
def binary_search(n, r, p):
    left = 0
    right = r - 1
    result = 0
    
    while left <= right:
        mid = left + (right - left) // 2
        if mid * p + (n - 1 - mid) * r <= r:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result * p

# Input parsing
n, r, p = map(int, input().split())

# Calculate and output the result
print(binary_search(n, r, p))
```
