
def minimal_marks_to_add(n, k, marks):
    current_average = sum(marks) / n
    target_average = k
    additional_marks = 0

    while current_average < target_average:
        marks.append(k)
        current_average = sum(marks) / len(marks)
        additional_marks += 1

    return additional_marks

# Input
n, k = map(int, input().split())
marks = list(map(int, input().split()))

# Output
print(minimal_marks_to_add(n, k, marks))
```
