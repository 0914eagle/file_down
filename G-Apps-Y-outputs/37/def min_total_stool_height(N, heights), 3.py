
def min_total_stool_height(N, heights):
    max_height = 0
    total_height = 0
    
    for height in reversed(heights):
        if height > max_height:
            max_height = height
        else:
            stool_height = max_height - height + 1
            total_height += stool_height
            max_height = height - 1
    
    return total_height

# Input
N = int(input())
heights = list(map(int, input().split()))

# Output
print(min_total_stool_height(N, heights))
