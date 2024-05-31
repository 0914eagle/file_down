
def min_stool_height(N, heights):
    total_height = 0
    max_height = 0

    for height in reversed(heights):
        if height > max_height:
            max_height = height
        else:
            stool_height = max_height - height + 1
            total_height += stool_height
            max_height = height - 1

    return total_height

# Reading input
N = int(input())
heights = list(map(int, input().split()))

# Calling the function and printing the result
result = min_stool_height(N, heights)
print(result)
