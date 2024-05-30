
def min_height_difference(n, k, heights):
    min_diff = float('inf')
    
    for i in range(n - k + 1):
        subrange = heights[i:i+k]
        diff = max(subrange) - min(subrange)
        min_diff = min(min_diff, diff)
    
    return min_diff

# Input parsing
n, k = map(int, input().split())
heights = list(map(int, input().split()))

# Call the function and output the result
result = min_height_difference(n, k, heights)
print(result)
