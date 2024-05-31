
def min_height_difference(N, K, heights):
    heights.sort()
    min_diff = float('inf')
    for i in range(N - K + 1):
        diff = heights[i + K - 1] - heights[i]
        min_diff = min(min_diff, diff)
    return min_diff

# Read input
N, K = map(int, input().split())
heights = [int(input()) for _ in range(N)]

# Call the function and print the result
result = min_height_difference(N, K, heights)
print(result)
