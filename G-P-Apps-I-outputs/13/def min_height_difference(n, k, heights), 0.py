
def min_height_difference(n, k, heights):
    min_diff = float('inf')
    
    for i in range(n - k + 1):
        sub_range = heights[i:i+k]
        min_height = min(sub_range)
        max_height = max(sub_range)
        
        min_diff = min(min_diff, max_height - min_height)
    
    return min_diff

# Read input
n, k = map(int, input().split())
heights = list(map(int, input().split()))

# Call the function with the input
result = min_height_difference(n, k, heights)
print(result)
