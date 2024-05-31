
def min_height_difference(N, K, heights):
    heights.sort()
    min_diff = float('inf')
    
    for i in range(N - K + 1):
        min_diff = min(min_diff, heights[i + K - 1] - heights[i])
    
    return min_diff

# Reading input
N, K = map(int, input().split())
heights = [int(input()) for _ in range(N)]

# Calling the function and printing the result
result = min_height_difference(N, K, heights)
print(result)
