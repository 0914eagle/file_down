
def min_stool_height(N, heights):
    stools = [0] * N
    for i in range(N-1):
        if heights[i] < heights[i+1]:
            stools[i+1] = max(stools[i], heights[i+1] - heights[i])
    for i in range(N-2, -1, -1):
        if heights[i] < heights[i+1]:
            stools[i] = max(stools[i+1], stools[i])
    return sum(stools)

# Input reading
N = int(input())
heights = list(map(int, input().split()))

# Call the function and print the result
print(min_stool_height(N, heights))
