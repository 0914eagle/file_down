
def check_non_decreasing(N, heights):
    if N == 1:
        return "Yes"
    
    for i in range(1, N):
        if heights[i] < heights[i-1]:
            if heights[i] + 1 == heights[i-1]:
                heights[i] += 1
            else:
                return "No"
    
    return "Yes"

# Read input from Standard Input
N = int(input())
heights = list(map(int, input().split()))

# Call the function and print the result
print(check_non_decreasing(N, heights))
