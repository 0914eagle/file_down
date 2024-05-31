
def is_non_decreasing_squares_possible(N, heights):
    for i in range(1, N):
        if heights[i] < heights[i-1]:
            if heights[i] + 1 < heights[i-1]:
                return "No"
            else:
                heights[i] += 1
    return "Yes"

# Input processing
N = int(input())
heights = list(map(int, input().split()))

# Check if it is possible to make the squares non-decreasing
result = is_non_decreasing_squares_possible(N, heights)
print(result)
