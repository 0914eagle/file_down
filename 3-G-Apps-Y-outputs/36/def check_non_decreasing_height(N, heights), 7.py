
def check_non_decreasing_height(N, heights):
    for i in range(1, N):
        if heights[i] < heights[i-1]:
            heights[i] += 1
        if heights[i] < heights[i-1]:
            return "No"
    return "Yes"

# Read input
N = int(input())
heights = list(map(int, input().split()))

# Check if heights can be made non-decreasing
result = check_non_decreasing_height(N, heights)
print(result)
