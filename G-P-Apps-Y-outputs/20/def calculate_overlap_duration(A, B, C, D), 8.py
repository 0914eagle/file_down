
def calculate_overlap_duration(A, B, C, D):
    start_time = max(A, C)
    end_time = min(B, D)
    
    overlap_duration = max(0, end_time - start_time)
    
    return overlap_duration

# Input
A, B, C, D = map(int, input().split())

# Calculate and output the result
result = calculate_overlap_duration(A, B, C, D)
print(result)
