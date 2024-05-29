
def min_additional_marks(n, k, marks):
    total_marks = sum(marks)
    total_marks_needed = n * k
    
    additional_marks = max(0, (total_marks_needed - total_marks + n - 1) // n)
    
    return additional_marks

# Input
n, k = map(int, input().split())
marks = list(map(int, input().split()))

# Output
print(min_additional_marks(n, k, marks))
```
