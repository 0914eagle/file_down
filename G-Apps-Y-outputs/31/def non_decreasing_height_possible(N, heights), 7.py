
def non_decreasing_height_possible(N, heights):
    for i in range(1, N):
        if heights[i] < heights[i-1]:
            heights[i] += 1
        if heights[i] < heights[i-1]:
            return "No"
    return "Yes"

# Input processing
N = int(input())
heights = list(map(int, input().split()))

# Output
print(non_decreasing_height_possible(N, heights))