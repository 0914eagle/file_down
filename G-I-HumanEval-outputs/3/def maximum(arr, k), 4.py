
def maximum(arr, k):
    return sorted(arr, reverse=True)[:k]

# Test Examples
print(maximum([-3, -4, 5], 3))  # Output: [-4, -3, 5]
print(maximum([4, -4, 4], 2))    # Output: [4, 4]
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))  # Output: [2]
```
