
def overlapping_seconds(A, B, C, D):
    start = max(A, C)
    end = min(B, D)
    overlap = max(0, end - start)
    return overlap

# Read input values
A, B, C, D = map(int, input().split())

# Calculate overlapping time
result = overlapping_seconds(A, B, C, D)

# Print the result
print(result)
