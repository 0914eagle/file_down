
def min_height_difference(N, K, heights):
    heights.sort()
    min_diff = float('inf')
    for i in range(N - K + 1):
        diff = heights[i + K - 1] - heights[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

# Reading input
N, K = map(int, input().split())
heights = [int(input()) for _ in range(N)]

# Calling the function and printing the result
print(min_height_difference(N, K, heights))
