
def calculate_overlap_duration(A, B, C, D):
    start = max(A, C)
    end = min(B, D)
    
    if start < end:
        return end - start
    else:
        return 0

# Input
A, B, C, D = map(int, input().split())

# Output
print(calculate_overlap_duration(A, B, C, D))
