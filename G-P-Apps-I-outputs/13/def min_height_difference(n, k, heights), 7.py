
def min_height_difference(n, k, heights):
    heights.sort()
    min_diff = float('inf')
    for i in range(n - k + 1):
        diff = heights[i + k - 1] - heights[i]
        min_diff = min(min_diff, diff)
    return min_diff

# Sample Input
n, k = 10, 2
heights = [1, 3, 5, 7, 9, 11, 13, 15, 17, 16]

# Output
print(min_height_difference(n, k, heights))
```
