
def duration_of_both_buttons_held(A, B, C, D):
    start_time = max(A, C)
    end_time = min(B, D)
    
    duration = max(0, end_time - start_time)
    
    return duration

# Read input values
A, B, C, D = map(int, input().split())

# Calculate and print the duration
result = duration_of_both_buttons_held(A, B, C, D)
print(result)
```
