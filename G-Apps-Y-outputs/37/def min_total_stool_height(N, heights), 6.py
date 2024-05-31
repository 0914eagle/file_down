
def min_total_stool_height(N, heights):
    total_height = 0
    max_height = 0
    
    for height in heights[::-1]:
        total_height += max(0, max_height - height)
        max_height = max(max_height, height)
    
    return total_height

# Input
N = int(input())
heights = list(map(int, input().split()))

# Output
print(min_total_stool_height(N, heights))
