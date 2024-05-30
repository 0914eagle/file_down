
def min_height_difference(n, k, heights):
    heights.sort()
    min_diff = float('inf')
    for i in range(n-k+1):
        diff = heights[i+k-1] - heights[i]
        min_diff = min(min_diff, diff)
    return min_diff

n, k = map(int, input().split())
heights = list(map(int, input().split()))

result = min_height_difference(n, k, heights)
print(result)
```
