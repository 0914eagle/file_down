
def duration_overlap(A, B, C, D):
    start = max(A, C)
    end = min(B, D)
    overlap = max(0, end - start)
    return overlap

# Read input
A, B, C, D = map(int, input().split())

# Calculate duration of overlap
result = duration_overlap(A, B, C, D)

# Print the result
print(result)
```
