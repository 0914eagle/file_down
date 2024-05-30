
def calculate_overlap_time(A, B, C, D):
    start_overlap = max(A, C)
    end_overlap = min(B, D)
    
    overlap_time = max(0, end_overlap - start_overlap)
    
    return overlap_time

# Reading input
A, B, C, D = map(int, input().split())

# Calculating overlap time
result = calculate_overlap_time(A, B, C, D)
print(result)
