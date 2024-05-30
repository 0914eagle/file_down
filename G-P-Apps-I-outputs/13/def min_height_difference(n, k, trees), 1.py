
def min_height_difference(n, k, trees):
    min_diff = float('inf')
    for i in range(n - k + 1):
        subrange = trees[i:i+k]
        diff = max(subrange) - min(subrange)
        min_diff = min(min_diff, diff)
    return min_diff

# Input parsing
n, k = map(int, input().split())
trees = list(map(int, input().split()))

result = min_height_difference(n, k, trees)
print(result)
```
