
def min_stool_height(N, heights):
    total_height = 0
    max_height = 0
    for i in range(N-1, -1, -1):
        total_height += max(0, max_height - heights[i])
        max_height = max(max_height, heights[i])
    return total_height

# Read input
N = int(input())
heights = list(map(int, input().split()))

# Call the function and print the result
print(min_stool_height(N, heights))
