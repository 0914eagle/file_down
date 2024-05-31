
def min_height_difference(N, K, heights):
    heights.sort()
    min_diff = float('inf')
    for i in range(N - K + 1):
        diff = heights[i + K - 1] - heights[i]
        min_diff = min(min_diff, diff)
    return min_diff

# Input
N, K = map(int, input().split())
heights = [int(input()) for _ in range(N)]

# Output
print(min_height_difference(N, K, heights))
