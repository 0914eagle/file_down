
def calculate_overlap(A, B, C, D):
    start_time = max(A, C)
    end_time = min(B, D)
    overlap_duration = max(0, end_time - start_time)
    return overlap_duration

# Input
A, B, C, D = map(int, input().split())

# Output
print(calculate_overlap(A, B, C, D))
