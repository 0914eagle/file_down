
def minimal_additional_marks(n, k, marks):
    current_avg = sum(marks) / n
    needed_marks = (n + 1) * k - sum(marks)
    if current_avg >= k:
        return 0
    else:
        return needed_marks

# Input
n, k = map(int, input().split())
marks = list(map(int, input().split()))

# Output
print(minimal_additional_marks(n, k, marks))
```
