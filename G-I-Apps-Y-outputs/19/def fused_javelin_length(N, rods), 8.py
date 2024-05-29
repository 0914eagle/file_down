
def fused_javelin_length(N, rods):
    total_length = sum(rods)
    return total_length - (N - 1)

# Read input
N = int(input())
rods = [int(input()) for _ in range(N)]

# Calculate the length of the fused javelin
result = fused_javelin_length(N, rods)

# Print the result
print(result)
