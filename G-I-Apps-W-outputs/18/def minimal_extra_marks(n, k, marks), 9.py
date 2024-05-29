
def minimal_extra_marks(n, k, marks):
    current_sum = sum(marks)
    current_average = current_sum / n
    additional_marks = 0
    
    while current_average < k - 0.5:
        additional_marks += 1
        current_sum += k
        n += 1
        current_average = current_sum / n
    
    return additional_marks

# Input
n, k = map(int, input().split())
marks = list(map(int, input().split()))

# Output
print(minimal_extra_marks(n, k, marks))
```
