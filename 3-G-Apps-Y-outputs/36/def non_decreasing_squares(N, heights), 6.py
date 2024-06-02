
def non_decreasing_squares(N, heights):
    for i in range(1, N):
        if heights[i] < heights[i-1]:
            heights[i] += 1
        if heights[i] < heights[i-1]:
            return "No"
    return "Yes"

# Input processing
N = int(input())
heights = list(map(int, input().split()))

# Call the function and print the result
result = non_decreasing_squares(N, heights)
print(result)
