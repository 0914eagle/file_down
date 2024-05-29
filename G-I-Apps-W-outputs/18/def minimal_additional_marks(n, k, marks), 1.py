
def minimal_additional_marks(n, k, marks):
    current_sum = sum(marks)
    target_sum = n * k
    additional_marks = (target_sum - current_sum) // (k - 1)
    if additional_marks * (k - 1) < target_sum - current_sum:
        additional_marks += 1
    return additional_marks

# Input reading
n, k = map(int, input().split())
marks = list(map(int, input().split()))

# Output
print(minimal_additional_marks(n, k, marks))
```
