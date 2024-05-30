
def min_height_difference(n, k, heights):
    min_diff = float('inf')

    for i in range(n - k + 1):
        min_height = min(heights[i:i+k])
        max_height = max(heights[i:i+k])
        min_diff = min(min_diff, max_height - min_height)

    return min_diff

# Input
n, k = map(int, input().split())
heights = list(map(int, input().split()))

# Output
print(min_height_difference(n, k, heights))
```
