
def min_total_stool_height(N, heights):
    total_height = 0
    max_height = 0
    
    for height in reversed(heights):
        total_height += max(0, max_height - height + 1)
        max_height = max(max_height, height)
    
    return total_height

# Input processing
N = int(input())
heights = list(map(int, input().split()))

# Call the function and print the result
print(min_total_stool_height(N, heights))
