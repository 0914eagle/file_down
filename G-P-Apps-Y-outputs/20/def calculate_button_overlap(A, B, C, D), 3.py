
def calculate_button_overlap(A, B, C, D):
    start = max(A, C)
    end = min(B, D)
    
    if end <= start:
        return 0
    else:
        return end - start

# Read input values
A, B, C, D = map(int, input().split())

# Calculate the duration of button overlap
duration = calculate_button_overlap(A, B, C, D)

print(duration)
```
