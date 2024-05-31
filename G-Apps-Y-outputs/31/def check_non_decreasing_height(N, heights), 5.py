
def check_non_decreasing_height(N, heights):
    if N == 1:
        return "Yes"
    
    for i in range(1, N):
        if heights[i] < heights[i-1]:
            if heights[i] == heights[i-1] - 1:
                heights[i] += 1
            else:
                return "No"
    
    return "Yes"

# Reading input from Standard Input
N = int(input())
heights = list(map(int, input().split()))

# Calling the function and printing the result
result = check_non_decreasing_height(N, heights)
print(result)
