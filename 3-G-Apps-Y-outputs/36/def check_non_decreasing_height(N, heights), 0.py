
def check_non_decreasing_height(N, heights):
    for i in range(1, N):
        if heights[i] < heights[i-1]:
            heights[i] += 1
        if heights[i] < heights[i-1]:
            return "No"
    return "Yes"

# Input
N = int(input())
heights = list(map(int, input().split()))

# Output
print(check_non_decreasing_height(N, heights))
