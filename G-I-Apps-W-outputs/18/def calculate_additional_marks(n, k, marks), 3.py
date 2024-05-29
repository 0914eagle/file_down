
def calculate_additional_marks(n, k, marks):
    current_average = sum(marks) / n
    additional_marks = 0
    
    while current_average < k - 0.5:
        additional_marks += 1
        total_marks = n + additional_marks
        current_average = (sum(marks) + additional_marks * k) / total_marks

    return additional_marks

# Reading input
n, k = map(int, input().split())
marks = list(map(int, input().split()))

# Output
print(calculate_additional_marks(n, k, marks))
```
