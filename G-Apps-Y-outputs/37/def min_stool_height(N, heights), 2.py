
def min_stool_height(N, heights):
    total_height = 0
    max_height = 0
    for height in reversed(heights):
        stool_height = max(0, max_height - height + 1)
        total_height += stool_height
        max_height = max(max_height, height + stool_height)
    return total_height

# Reading input
N = int(input())
heights = list(map(int, input().split()))

# Calling the function and printing the result
print(min_stool_height(N, heights))
