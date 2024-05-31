
def check_non_decreasing_height(N, heights):
    if N == 1:
        return "Yes"
    
    for i in range(N-1):
        if heights[i+1] < heights[i]:
            if heights[i+1] + 1 < heights[i]:
                return "No"
            else:
                heights[i] -= 1
    
    return "Yes"

# Reading input from Standard Input
N = int(input())
heights = list(map(int, input().split()))

# Calling the function and printing the result
print(check_non_decreasing_height(N, heights))
