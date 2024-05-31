
def min_stool_height(N, heights):
    max_height = 0
    total_height = 0

    for i in range(N-1, -1, -1):
        if heights[i] > max_height:
            max_height = heights[i]
        total_height += max(0, max_height - heights[i])

    return total_height

# Input
N = int(input())
heights = list(map(int, input().split()))

# Output
print(min_stool_height(N, heights))
