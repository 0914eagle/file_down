
def holding_buttons_duration(A, B, C, D):
    start_time = max(A, C)
    end_time = min(B, D)
    
    if end_time <= start_time:
        return 0
    
    return end_time - start_time

# Read input
A, B, C, D = map(int, input().split())

# Call the function and output the result
print(holding_buttons_duration(A, B, C, D))
