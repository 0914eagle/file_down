
def non_decreasing_heights(N, heights):
    for i in range(1, N):
        if heights[i] < heights[i - 1]:
            if heights[i] + 1 < heights[i - 1]:
                return "No"
            else:
                heights[i] += 1
    return "Yes"

# Input processing
N = int(input())
heights = list(map(int, input().split()))

# Output
print(non_decreasing_heights(N, heights))
