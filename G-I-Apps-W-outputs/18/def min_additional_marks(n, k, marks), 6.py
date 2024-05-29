
def min_additional_marks(n, k, marks):
    current_total = sum(marks)
    desired_total = n * k
    additional_marks = max(0, -(-(desired_total - current_total) // k))
    return additional_marks

# Read input
n, k = map(int, input().split())
marks = list(map(int, input().split()))

# Calculate and print minimal number of additional marks
print(min_additional_marks(n, k, marks))
```
