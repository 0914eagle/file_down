
def min_stool_height(N, heights):
    stools = [0] * N
    for i in range(N):
        stools[i] = max(0, heights[i] - sum(stools[:i]))
    return sum(stools)

# Read input
N = int(input())
heights = list(map(int, input().split()))

# Call the function and print the result
print(min_stool_height(N, heights))
